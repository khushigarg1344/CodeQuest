const API_BASE = "http://127.0.0.1:8000";
const TOKEN_KEY = "codequest_access_token";

const state = {
  xp: 0,
  solved: 0,
  streak: 0,
  badges: 0,
  badgeList:[],
  problems: [],
  dailyChallenge: null,
  activeProblem: null,
  user: null,
  lastExecution: null,
  chatHistory: [],
  dailyProgress: null,
  calendarMonth: new Date().getMonth(),
  calendarYear: new Date().getFullYear()
};

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];

let accountMode = "login";

// --------------------------------------------------
// TOAST
// --------------------------------------------------

function showToast(message) {
  const toast = $("#toast");
  if (!toast) return;

  toast.textContent = message;
  toast.classList.add("visible");

  window.setTimeout(() => {
    toast.classList.remove("visible");
  }, 2600);
}

// --------------------------------------------------
// API AND AUTHENTICATION
// --------------------------------------------------

function getToken() {
  return sessionStorage.getItem(TOKEN_KEY);
}

async function apiRequest(path, options = {}) {
  const headers = {
    "Content-Type": "application/json",
    ...(options.headers || {})
  };

  if (getToken()) {
    headers.Authorization = `Bearer ${getToken()}`;
  }

  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers
  });

  const body = await response.json().catch(() => ({}));

  if (!response.ok) {
    if (response.status === 401 && getToken()) {
      logout(false);
    }

    const detail = body.detail;

    throw new Error(
      typeof detail === "string"
        ? detail
        : `Request failed (${response.status})`
    );
  }

  return body;
}

// --------------------------------------------------
// USER PROFILE AND XP
// --------------------------------------------------

function updateStats() {
  const level = Math.floor(state.xp / 100) + 1;
  const currentLevelXP = state.xp % 100;

  if ($("#xp-value")) $("#xp-value").textContent = state.xp;
  if ($("#stat-xp")) $("#stat-xp").textContent = state.xp;
  if ($("#stat-solved")) $("#stat-solved").textContent = state.solved;
  if ($("#stat-streak")) $("#stat-streak").textContent = `${state.streak} days`;
  if ($("#stat-badges")) $("#stat-badges").textContent = state.badges;
  if ($("#leader-xp")) $("#leader-xp").textContent = `${state.xp} XP`;

  if ($("#level-label")) {
    $("#level-label").textContent =
      `LEVEL ${String(level).padStart(2, "0")}`;
  }

  if ($("#rank-label")) {
    $("#rank-label").textContent =
      level < 3 ? "Beginner" :
      level < 6 ? "Explorer" :
      "Code Master";
  }

  if ($("#next-rank")) {
    $("#next-rank").textContent =
      `Level ${String(level + 1).padStart(2, "0")} →`;
  }

  if ($("#xp-progress")) {
    $("#xp-progress").style.width = `${currentLevelXP}%`;
  }

  if (state.user) {
    if ($("#profile-name")) {
      $("#profile-name").textContent = state.user.name;
    }

    if ($("#profile-level")) {
      $("#profile-level").textContent =
        `Level ${String(level).padStart(2, "0")} · ${$("#rank-label")?.textContent || ""}`;
    }

    if ($("#side-streak")) {
      $("#side-streak").textContent =
        state.streak ? `${state.streak}-day streak` : "Start a streak";
    }

    if ($("#account-button")) {
      $("#account-button").innerHTML = "♙ <span>Log out</span>";
    }

  } else {
    if ($("#profile-name")) $("#profile-name").textContent = "Code Explorer";
    if ($("#profile-level")) $("#profile-level").textContent = "Level 01 · Beginner";
    if ($("#side-streak")) $("#side-streak").textContent = "Start a streak";

    if ($("#account-button")) {
      $("#account-button").innerHTML = "♙ <span>Log in / Register</span>";
    }
  }
}

function applyProfile(profile) {
  state.user = profile;
  state.xp = Number(profile.xp || 0);
  state.solved = Number(profile.solved || 0);
  state.streak = Number(profile.streak || 0);
  state.badges = Number(profile.badges || 0);

  updateStats();
}

async function loadProfile() {
  if (!getToken()) {
    state.user = null;
    state.xp = 0;
    state.solved = 0;
    state.streak = 0;
    state.badges = 0;

    updateStats();
    return;
  }

  try {
    applyProfile(await apiRequest("/api/users/me"));
  } catch (error) {
    showToast(error.message);
  }
}

// --------------------------------------------------
// HTML ESCAPING
// --------------------------------------------------

function escapeHTML(value = "") {
  return String(value).replace(
    /[&<>"']/g,
    (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[char]
  );
}

// --------------------------------------------------
// PROBLEMS
// --------------------------------------------------

function renderProblems(problems) {
  const list = $("#problem-list");
  if (!list) return;

  if (!problems.length) {
    list.innerHTML = `
      <div class="empty-state">
        No problems found. Add questions through the API
        or check that the backend is running.
      </div>
    `;
    return;
  }

  list.innerHTML = problems.map((problem) => `
    <button class="problem-row"
      data-problem-id="${Number(problem.id)}">

      <span class="problem-symbol">&lt;/&gt;</span>

      <span class="problem-info">
        <strong>${escapeHTML(problem.title)}</strong>
        <small>
          ${escapeHTML(problem.topic || "General")}
          · +${Number(problem.xp_reward || 0)} XP
        </small>
      </span>

      <span class="difficulty ${(problem.difficulty || "easy").toLowerCase()}">
        ${escapeHTML(problem.difficulty || "Easy")}
      </span>

      <span class="problem-arrow">→</span>
    </button>
  `).join("");

  $$("[data-problem-id]").forEach((button) => {
    button.addEventListener("click", () => {
      openProblem(Number(button.dataset.problemId));
    });
  });
}

async function loadProblems() {
  const list = $("#problem-list");
  if (!list) return;

  list.innerHTML = `
    <div class="empty-state">
      Loading problems from your CodeQuest API…
    </div>
  `;

  try {
    const response = await fetch(`${API_BASE}/api/problems/`);

    if (!response.ok) {
      throw new Error(`API returned ${response.status}`);
    }

    const data = await response.json();

    state.problems = Array.isArray(data) ? data : [];

    renderProblems(state.problems);

    $("#api-status")?.classList.add("connected");

    if ($("#api-status")) {
      $("#api-status").innerHTML = "<i></i> API connected";
    }

    if ($("#api-detail")) {
      $("#api-detail").textContent =
        `Connected successfully. ${state.problems.length} problem(s) loaded from FastAPI.`;
    }

  } catch (error) {
    $("#api-status")?.classList.remove("connected");

    if ($("#api-status")) {
      $("#api-status").innerHTML = "<i></i> API offline";
    }

    if ($("#api-detail")) {
      $("#api-detail").textContent =
        "Start the FastAPI backend to load database problems.";
    }

    list.innerHTML = `
      <div class="empty-state">
        <strong>Can't connect to FastAPI.</strong>
        <br>Start the backend, then click Refresh problems.
        <br><small>${escapeHTML(error.message)}</small>
      </div>
    `;
  }
}


async function loadBadges() {
    try {
        const response = await apiRequest("/api/badges/");

        state.badgeList = response.badges || [];
        state.badges = response.total_badges || 0;

        updateStats();
        renderAchievements();

    } catch (error) {
        console.error("Failed to load badges:", error);
    }
}


function createAchievementsUI() {
    const rightColumn = document.querySelector(".right-column");

    if (!rightColumn || document.querySelector("#achievements-card")) {
        return;
    }

    const achievementsHTML = `
        <section class="achievements-card" id="achievements-card">
            <div class="achievements-header">
                <div>
                    <h2>Achievements</h2>
                    <p>Complete quests and build your coding streak.</p>
                </div>
                <span id="achievement-count">0 / 9</span>
            </div>

            <div class="achievements-grid" id="achievements-grid">
                <p>Loading achievements...</p>
            </div>
        </section>
    `;

    const leaderboard = rightColumn.querySelector(".leaderboard-card");

    if (leaderboard) {
        leaderboard.insertAdjacentHTML("beforebegin", achievementsHTML);
    } else {
        rightColumn.insertAdjacentHTML("beforeend", achievementsHTML);
    }
}


const ACHIEVEMENTS = [
    {
        name: "First Quest",
        description: "Solve your first coding problem.",
        icon: "🎯",
        target: "1 problem"
    },
    {
        name: "Problem Solver",
        description: "Solve five different coding problems.",
        icon: "⚡",
        target: "5 problems"
    },
    {
        name: "Code Explorer",
        description: "Solve ten different coding problems.",
        icon: "🧭",
        target: "10 problems"
    },
    {
        name: "Rising Coder",
        description: "Solve twenty different coding problems.",
        icon: "🚀",
        target: "20 problems"
    },
    {
        name: "DSA Master",
        description: "Solve fifty different coding problems.",
        icon: "🏆",
        target: "50 problems"
    },
    {
        name: "CodeQuest Champion",
        description: "Solve one hundred different coding problems.",
        icon: "👑",
        target: "100 problems"
    },
    {
        name: "Consistency Starter",
        description: "Complete daily challenges for 3 consecutive days.",
        icon: "🔥",
        target: "3-day streak"
    },
    {
        name: "Weekly Warrior",
        description: "Complete daily challenges for 7 consecutive days.",
        icon: "🌟",
        target: "7-day streak"
    },
    {
        name: "Streak Legend",
        description: "Complete daily challenges for 30 consecutive days.",
        icon: "💎",
        target: "30-day streak"
    }
];

function renderAchievements() {
    const grid = $("#achievements-grid");
    const count = $("#achievement-count");

    if (!grid || !count) return;

    const earnedNames = new Set(
        state.badgeList.map(badge => badge.name)
    );

    const earnedCount = ACHIEVEMENTS.filter(
        badge => earnedNames.has(badge.name)
    ).length;

    count.textContent = `${earnedCount} / ${ACHIEVEMENTS.length}`;

    grid.innerHTML = ACHIEVEMENTS.map(badge => {
        const unlocked = earnedNames.has(badge.name);

        return `
            <div class="achievement-item ${unlocked ? "unlocked" : "locked"}">
                <div class="achievement-icon">
                    ${unlocked ? badge.icon : "🔒"}
                </div>

                <div class="achievement-info">
                    <h3>${badge.name}</h3>
                    <p>${badge.description}</p>
                    <span class="achievement-target">
                        ${unlocked ? "✓ Unlocked" : badge.target}
                    </span>
                </div>

                <span class="achievement-status">
                    ${unlocked ? "Earned" : "Locked"}
                </span>
            </div>
        `;
    }).join("");
}

// --------------------------------------------------
// STARTER CODE
// --------------------------------------------------

function getStarterCode(problem, language) {
  const title = (problem.title || "").toLowerCase();

  if (title.includes("reverse")) {
    if (language === "python") {
      return `n = int(input())
arr = list(map(int, input().split()))

print(*arr[::-1])`;
    }

    if (language === "java") {
      return `import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = n - 1; i >= 0; i--) {
            System.out.print(arr[i]);
            if (i > 0) System.out.print(" ");
        }
    }
}`;
    }

    return `#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i];
        if (i > 0) cout << " ";
    }

    cout << endl;
    return 0;
}`;
  }

  if (title.includes("maximum")) {
    if (language === "python") {
      return `n = int(input())
arr = list(map(int, input().split()))

print(max(arr))`;
    }

    if (language === "java") {
      return `import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            max = Math.max(max, sc.nextInt());
        }

        System.out.println(max);
    }
}`;
    }

    return `#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int x;
    int mx = INT_MIN;

    for (int i = 0; i < n; i++) {
        cin >> x;
        mx = max(mx, x);
    }

    cout << mx << endl;
    return 0;
}`;
  }

  if (language === "python") {
    return `# Write your Python solution here`;
  }

  if (language === "java") {
    return `import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Write your solution here
    }
}`;
  }

  return `#include <bits/stdc++.h>
using namespace std;

int main() {
    // Write your solution here
    return 0;
}`;
}

// --------------------------------------------------
// OPEN PROBLEM
// --------------------------------------------------

function openProblem(id) {
  const problem =
    state.problems.find(
      (item) => Number(item.id) === Number(id)
    ) ||
    (
      Number(state.dailyChallenge?.id) === Number(id)
        ? state.dailyChallenge
        : null
    );

  if (!problem) return;

  state.activeProblem = problem;
  state.lastExecution = null;

  // Reset conversation when a new problem is opened.
  state.chatHistory = [];

  $("#dialog-topic").textContent =
    `${problem.topic || "CODING"} · CHALLENGE`;

  $("#dialog-title").textContent = problem.title;

  $("#dialog-description").textContent =
    problem.description ||
    "Solve the problem using your preferred programming language.";

  $("#dialog-input").textContent =
    problem.sample_input || "No sample input available";

  $("#dialog-output").textContent =
    problem.sample_output || "No sample output available";

  const difficulty = $("#dialog-difficulty");

  difficulty.textContent = problem.difficulty || "Easy";
  difficulty.className =
    `difficulty ${(problem.difficulty || "easy").toLowerCase()}`;

  $("#language-select").value = "python";

  $("#code-editor").value =
    getStarterCode(problem, "python");

  $("#run-result").textContent =
    "Your output and test-case results will appear here.";

  $("#run-result").className = "run-result";

  if ($("#ai-tutor-panel")) {
    $("#ai-tutor-panel").hidden = true;
  }

  if ($("#ai-tutor-response")) {
    $("#ai-tutor-response").textContent = "";
  }

  if ($("#ai-question-input")) {
    $("#ai-question-input").value = "";
  }

  if ($("#ai-chat-history")) {
    $("#ai-chat-history").replaceChildren();
  }

  $("#problem-dialog").showModal();
}

// --------------------------------------------------
// CHANGE LANGUAGE
// --------------------------------------------------

$("#language-select").addEventListener("change", () => {
  if (!state.activeProblem) return;

  $("#code-editor").value =
    getStarterCode(
      state.activeProblem,
      $("#language-select").value
    );
});

// --------------------------------------------------
// RUN CODE - JUDGE0
// --------------------------------------------------

$("#run-code").addEventListener("click", async () => {
  if (!state.activeProblem) return;

  if (!getToken()) {
    $("#problem-dialog").close();
    openAccount("login");

    $("#account-error").textContent =
      "Please log in before running code.";

    return;
  }

  const button = $("#run-code");
  const resultBox = $("#run-result");

  const code = $("#code-editor").value.trim();
  const language = $("#language-select").value;

  if (!code) {
    resultBox.textContent = "Please write your code first.";
    resultBox.className = "run-result rejected";
    return;
  }

  button.disabled = true;
  button.textContent = "Running...";

  resultBox.textContent =
    "Submitting your code to Judge0. Please wait...";

  resultBox.className = "run-result";

  try {
    const result = await apiRequest(
      `/api/submissions/${state.activeProblem.id}/run`,
      {
        method: "POST",
        body: JSON.stringify({
          code,
          language
        })
      }
    );

    const passed = Boolean(result.passed);

    state.lastExecution = {
      status: passed ? "Accepted" : "Not Accepted",
      output: result.output || "",
      error: result.error || ""
    };

    resultBox.className = passed
      ? "run-result accepted"
      : "run-result rejected";

    let message = passed
      ? "ACCEPTED! All test cases passed."
      : "NOT ACCEPTED. Check your code and try again.";

    if (result.passed_test_cases !== undefined) {
      message +=
        `\n\nTest cases passed: ${result.passed_test_cases}/${result.total_test_cases}`;
    }

    if (result.output) {
      message += `\n\nOutput:\n${result.output}`;
    }

    if (result.error) {
      message += `\n\nError:\n${result.error}`;
    }

    if (result.awarded_xp) {
      message += `\n\nXP earned: +${result.awarded_xp}`;
    } else if (passed && result.already_solved) {
      message += "\n\nYou have already earned XP for this problem.";
    }

    resultBox.textContent = message;

    if (passed) {
  await loadProfile();
  await loadBadges();
  await loadDailyProgress();
  await loadLeaderboard();

  if (
    result.daily_challenge_completed ||
    result.already_completed_today
  ) {
    $("#daily-feedback").textContent =
      "✓ Today's Daily Challenge has been completed!";

    $("#daily-feedback").className =
      "challenge-feedback correct";
  }
}
  } catch (error) {
    state.lastExecution = {
      status: "Error",
      output: "",
      error: error.message
    };

    resultBox.className = "run-result rejected";
    resultBox.textContent = `Execution error:\n${error.message}`;

  } finally {
    button.disabled = false;
    button.textContent = "▶ Run Code";
  }
});

// --------------------------------------------------
// AI TUTOR - AUTOMATIC CODE ANALYSIS
// --------------------------------------------------

$("#ask-ai-tutor").addEventListener("click", async () => {
  if (!state.activeProblem) {
    showToast("Please open a coding problem first.");
    return;
  }

  if (!getToken()) {
    $("#problem-dialog").close();
    openAccount("login");

    $("#account-error").textContent =
      "Please log in before using AI Tutor.";

    return;
  }

  const code = $("#code-editor").value.trim();
  const language = $("#language-select").value;

  const button = $("#ask-ai-tutor");
  const panel = $("#ai-tutor-panel");
  const responseBox = $("#ai-tutor-response");

  if (!code) {
    showToast("Please write your code first.");
    return;
  }

  const execution = state.lastExecution || {
    status: "Not Run",
    output: "",
    error: ""
  };

  button.disabled = true;
  button.textContent = "Thinking...";

  panel.hidden = false;

  responseBox.textContent =
    "CodeQuest AI Tutor is analysing your code. Please wait...";

  try {
    const result = await apiRequest("/api/ai/tutor", {
      method: "POST",
      body: JSON.stringify({
        problem_id: Number(state.activeProblem.id),
        code,
        language,
        status: execution.status,
        output: execution.output,
        error: execution.error,
        mode: "analysis"
      })
    });

    responseBox.textContent =
      result.tutor_response ||
      "The AI Tutor returned an empty response.";

  } catch (error) {
    responseBox.textContent =
      `Unable to get AI Tutor response.\n\n${error.message}`;

  } finally {
    button.disabled = false;
    button.textContent = "✦ Ask AI Tutor";
  }
});

// --------------------------------------------------
// AI CHAT UI
// --------------------------------------------------

function addAIChatMessage(role, message) {
  const history = $("#ai-chat-history");
  if (!history) return null;

  const messageElement = document.createElement("div");
  messageElement.className = `ai-chat-message ${role}`;

  const heading = document.createElement("strong");

  heading.textContent =
    role === "user" ? "You" : "✦ CodeQuest AI Tutor";

  const content = document.createElement("div");
  content.textContent = message;

  messageElement.append(heading, content);
  history.appendChild(messageElement);

  messageElement.scrollIntoView({
    behavior: "smooth",
    block: "nearest"
  });

  return content;
}

// --------------------------------------------------
// AI TUTOR - CUSTOM QUESTIONS WITH CHAT HISTORY
// --------------------------------------------------

async function sendAIQuestion() {
  if (!state.activeProblem) {
    showToast("Please open a coding problem first.");
    return;
  }

  if (!getToken()) {
    $("#problem-dialog").close();
    openAccount("login");

    $("#account-error").textContent =
      "Please log in before using AI Tutor.";

    return;
  }

  const questionInput = $("#ai-question-input");
  const sendButton = $("#ai-send-question");
  const panel = $("#ai-tutor-panel");

  const question = questionInput.value.trim();

  if (!question) {
    showToast("Please type your question first.");
    questionInput.focus();
    return;
  }

  const code = $("#code-editor").value.trim();
  const language = $("#language-select").value;

  const execution = state.lastExecution || {
    status: "Not Run",
    output: "",
    error: ""
  };

  // Keep the current question in conversation history.
  state.chatHistory.push({
    role: "user",
    content: question
  });

  addAIChatMessage("user", question);

  questionInput.value = "";

  panel.hidden = false;

  sendButton.disabled = true;
  sendButton.textContent = "Thinking...";

  const answerElement = addAIChatMessage(
    "assistant",
    "Thinking about your question..."
  );

  try {
    const result = await apiRequest("/api/ai/tutor", {
      method: "POST",
      body: JSON.stringify({
        problem_id: Number(state.activeProblem.id),
        code,
        language,
        status: execution.status,
        output: execution.output,
        error: execution.error,
        mode: "question",
        question,

        // Send previous messages to the backend.
        conversation_history: state.chatHistory.slice(-8)
      })
    });

    const answer =
      result.tutor_response ||
      "The AI Tutor returned an empty response.";

    // Save assistant response for the next follow-up.
    state.chatHistory.push({
      role: "assistant",
      content: answer
    });

    answerElement.textContent = answer;

  } catch (error) {
    answerElement.textContent =
      `Unable to get an answer.\n\n${error.message}`;

    // Remove the unanswered question so history remains accurate.
    state.chatHistory.pop();

  } finally {
    sendButton.disabled = false;
    sendButton.textContent = "✦ Ask Question";
    questionInput.focus();
  }
}

$("#ai-send-question").addEventListener(
  "click",
  sendAIQuestion
);

// Enter sends; Shift + Enter inserts a new line.
$("#ai-question-input").addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();

    if (!$("#ai-send-question").disabled) {
      sendAIQuestion();
    }
  }
});

// --------------------------------------------------
// LOGIN / REGISTER
// --------------------------------------------------

function openAccount(mode = "login") {
  if (state.user && mode === "login") {
    logout();
    return;
  }

  accountMode = mode;

  $("#account-form").reset();
  $("#account-error").textContent = "";

  const registering = accountMode === "register";

  $("#account-title").textContent =
    registering ? "Create your account" : "Log in";

  $("#account-subtitle").textContent =
    registering
      ? "Create an account to save your coding progress."
      : "Log in to save your XP and progress.";

  $("#name-field").style.display =
    registering ? "flex" : "none";

  $("#account-name").required = registering;

  $("#account-password").autocomplete =
    registering ? "new-password" : "current-password";

  $("#account-submit").textContent =
    registering ? "Create account" : "Log in";

  $("#account-switch").textContent =
    registering
      ? "Already registered? Log in"
      : "New here? Create an account";

  $("#account-dialog").showModal();
}

function logout(showMessage = true) {
  sessionStorage.removeItem(TOKEN_KEY);

  state.user = null;
  state.xp = 0;
  state.solved = 0;
  state.streak = 0;
  state.badges = 0;
  state.chatHistory = [];
  state.dailyProgress = null;

  updateStats();
  renderDailyProgress();

  if ($("#account-dialog")?.open) {
    $("#account-dialog").close();
  }

  if (showMessage) {
    showToast("You have logged out.");
  }
}

$("#account-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const registering = accountMode === "register";

  const payload = {
    email: $("#account-email").value.trim(),
    password: $("#account-password").value
  };

  if (registering) {
    payload.name = $("#account-name").value.trim();
  }

  $("#account-submit").disabled = true;
  $("#account-error").textContent = "";

  try {
    const result = await apiRequest(
      registering ? "/api/auth/register" : "/api/auth/login",
      {
        method: "POST",
        body: JSON.stringify(payload)
      }
    );

    sessionStorage.setItem(
      TOKEN_KEY,
      result.access_token
    );

    $("#account-dialog").close();

    applyProfile(
      await apiRequest("/api/users/me")
    );

    showToast(
  registering
    ? "Account created. Your journey starts now!"
    : "Welcome back!"
);

await loadDailyProgress();
await loadLeaderboard();

  } catch (error) {
    $("#account-error").textContent = error.message;

  } finally {
    $("#account-submit").disabled = false;
  }
});

$("#account-switch").addEventListener("click", () => {
  openAccount(
    accountMode === "login" ? "register" : "login"
  );
});

$("#close-account").addEventListener("click", () => {
  $("#account-dialog").close();
});

// --------------------------------------------------
// LEADERBOARD
// --------------------------------------------------

async function loadLeaderboard() {
  try {
    const users = await apiRequest("/api/users/leaderboard");

    const card = $(".leaderboard-card");
    if (!card) return;

    const currentEmail = state.user?.email;

    const rows = users.map((user, index) => {
      const initials = user.name
        .split(/\s+/)
        .map((part) => part[0])
        .join("")
        .slice(0, 2)
        .toUpperCase();

      const current =
        user.name === state.user?.name && currentEmail;

      return `
        <div class="leader-row${current ? " current" : ""}">
          <span class="leader-rank">${index + 1}</span>

          <span class="leader-avatar${index === 1 ? " alt" : ""}">
            ${escapeHTML(initials)}
          </span>

          <span class="leader-name">
            <strong>${escapeHTML(user.name)}</strong>
            <small>Level ${String(user.level).padStart(2, "0")}</small>
          </span>

          <strong>${Number(user.xp).toLocaleString()} XP</strong>
        </div>
      `;
    }).join("");

    const heading = card.querySelector(".section-heading");

    card.querySelectorAll(".leader-row").forEach((row) => {
      row.remove();
    });

    card.querySelector(".demo-note")?.remove();

    if (heading) {
      heading.insertAdjacentHTML(
        "afterend",
        rows || '<p class="demo-note">No registered players yet.</p>'
      );
    }

  } catch {
    // Keep static demo leaderboard if API is unavailable.
  }
}

// --------------------------------------------------
// SEARCH AND REFRESH
// --------------------------------------------------

$("#refresh-problems").addEventListener(
  "click",
  loadProblems
);

$("#search-input").addEventListener("input", (event) => {
  const query = event.target.value.trim().toLowerCase();

  renderProblems(
    state.problems.filter((problem) =>
      `${problem.title} ${problem.topic} ${problem.difficulty}`
        .toLowerCase()
        .includes(query)
    )
  );
});

// --------------------------------------------------
// DAILY CHALLENGE
// --------------------------------------------------

// --------------------------------------------------
// DAILY CHALLENGE
// --------------------------------------------------

async function loadDailyChallenge() {
  const title = $("#daily-title");
  const meta = $("#daily-meta");
  const description = $("#daily-description");
  const difficulty = $("#daily-difficulty");
  const solveButton = $("#solve-daily-challenge");
  const feedback = $("#daily-feedback");

  if (!title || !solveButton) return;

  try {
    title.textContent = "Loading today's challenge...";
    solveButton.disabled = true;

    const challenge = await apiRequest(
      "/api/problems/daily"
    );

    if (!challenge || !challenge.id) {
      throw new Error("No daily challenge was returned.");
    }

    state.dailyChallenge = challenge;

    title.textContent = challenge.title || "Daily Challenge";

    meta.textContent =
      `${challenge.topic || "DSA"} · ` +
      `${challenge.difficulty || "Easy"} · ` +
      `+${Number(challenge.xp_reward || 0)} XP` +
      (
        challenge.challenge_date
          ? ` · ${challenge.challenge_date}`
          : ""
      );

    description.textContent =
      challenge.description ||
      "Solve today's DSA coding challenge.";

    difficulty.textContent =
      challenge.difficulty || "Easy";

    difficulty.className =
      `difficulty ${(challenge.difficulty || "easy").toLowerCase()}`;

    solveButton.disabled = false;
    solveButton.textContent = "Solve Daily Challenge";

    if (feedback) {
      feedback.textContent = "";
      feedback.className = "challenge-feedback";
    }

  } catch (error) {
    title.textContent = "Challenge unavailable";

    meta.textContent = "Daily challenge could not be loaded.";

    description.textContent = error.message;

    solveButton.disabled = true;
    solveButton.textContent = "Try again later";
  }
}

// Open today's question in the existing coding dialog.
$("#solve-daily-challenge").addEventListener("click", () => {
  if (!state.dailyChallenge) return;

  openProblem(Number(state.dailyChallenge.id));
});
 
// --------------------------------------------------
// DAILY CHALLENGE CALENDAR AND STREAK TRACKER
// --------------------------------------------------

function getLocalDateKey(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");

  return `${year}-${month}-${day}`;
}

// Create the calendar UI below the Daily Challenge card.
function createDailyProgressUI() {
  const dailyCard = $(".daily-card");

  if (!dailyCard || $("#daily-progress-card")) return;

  const section = document.createElement("section");

  section.className = "daily-progress-card";
  section.id = "daily-progress-card";

  section.innerHTML = `
    <div class="daily-progress-heading">
      <div>
        <p class="eyebrow">YOUR CONSISTENCY</p>
        <h2>Daily Progress</h2>
      </div>

      <span class="calendar-flame">♨</span>
    </div>

    <div class="streak-summary">
      <div class="streak-stat">
        <span class="streak-stat-icon">🔥</span>
        <strong id="calendar-current-streak">0</strong>
        <small>Current streak</small>
      </div>

      <div class="streak-stat">
        <span class="streak-stat-icon">🏆</span>
        <strong id="calendar-longest-streak">0</strong>
        <small>Longest streak</small>
      </div>

      <div class="streak-stat">
        <span class="streak-stat-icon">✓</span>
        <strong id="calendar-total-days">0</strong>
        <small>Days completed</small>
      </div>
    </div>

    <div class="calendar-container">

      <div class="calendar-header">
        <button
          type="button"
          id="calendar-previous"
          aria-label="Previous month">
          ‹
        </button>

        <strong id="calendar-month-label"></strong>

        <button
          type="button"
          id="calendar-next"
          aria-label="Next month">
          ›
        </button>
      </div>

      <div class="calendar-weekdays">
        <span>Sun</span>
        <span>Mon</span>
        <span>Tue</span>
        <span>Wed</span>
        <span>Thu</span>
        <span>Fri</span>
        <span>Sat</span>
      </div>

      <div
        class="calendar-days"
        id="calendar-days">
      </div>
    </div>

    <div class="calendar-legend">
      <span>
        <i class="legend-completed"></i>
        Completed
      </span>

      <span>
        <i class="legend-today"></i>
        Today
      </span>
    </div>

    <p
      class="calendar-message"
      id="calendar-message"
      aria-live="polite">
      Log in to track your daily challenge progress.
    </p>
  `;

  dailyCard.insertAdjacentElement("afterend", section);

  $("#calendar-previous").addEventListener("click", () => {
    state.calendarMonth--;

    if (state.calendarMonth < 0) {
      state.calendarMonth = 11;
      state.calendarYear--;
    }

    renderDailyCalendar();
  });

  $("#calendar-next").addEventListener("click", () => {
    const today = new Date();

    const nextDate = new Date(
      state.calendarYear,
      state.calendarMonth + 1,
      1
    );

    // Do not allow navigating into future months.
    if (
      nextDate.getFullYear() > today.getFullYear() ||
      (
        nextDate.getFullYear() === today.getFullYear() &&
        nextDate.getMonth() > today.getMonth()
      )
    ) {
      return;
    }

    state.calendarMonth++;
    
    if (state.calendarMonth > 11) {
      state.calendarMonth = 0;
      state.calendarYear++;
    }

    renderDailyCalendar();
  });
}

// Render the calendar for the selected month.
function renderDailyCalendar() {
  createDailyProgressUI();

  const calendarDays = $("#calendar-days");
  const monthLabel = $("#calendar-month-label");

  if (!calendarDays || !monthLabel) return;

  const year = state.calendarYear;
  const month = state.calendarMonth;

  const today = state.dailyProgress?.today ||
    getLocalDateKey(new Date());

  const completedDates = new Set(
    state.dailyProgress?.completed_dates || []
  );

  const monthName = new Date(year, month, 1)
    .toLocaleDateString("en-US", {
      month: "long",
      year: "numeric"
    });

  monthLabel.textContent = monthName;

  const firstDay = new Date(year, month, 1).getDay();

  const totalDays = new Date(year, month + 1, 0).getDate();

  const cells = [];

  // Empty cells before the first day of the month.
  for (let i = 0; i < firstDay; i++) {
    cells.push('<span class="calendar-day empty"></span>');
  }

  for (let day = 1; day <= totalDays; day++) {
    const date = getLocalDateKey(
      new Date(year, month, day)
    );

    const isCompleted = completedDates.has(date);
    const isToday = date === today;

    const classes = [
      "calendar-day",
      isCompleted ? "completed" : "",
      isToday ? "today" : ""
    ].filter(Boolean).join(" ");

    cells.push(`
      <span
        class="${classes}"
        aria-label="${date}${isCompleted ? ", completed" : ""}${isToday ? ", today" : ""}"
        title="${date}${isCompleted ? " - Challenge completed" : ""}">
        ${isCompleted ? "✓" : day}
      </span>
    `);
  }

  calendarDays.innerHTML = cells.join("");

  const currentMonth = new Date(
    today + "T00:00:00"
  );

  const selectedMonth = new Date(year, month, 1);

  const nextButton = $("#calendar-next");

  if (nextButton) {
    nextButton.disabled =
      selectedMonth.getFullYear() > currentMonth.getFullYear() ||
      (
        selectedMonth.getFullYear() === currentMonth.getFullYear() &&
        selectedMonth.getMonth() >= currentMonth.getMonth()
      );
  }

  const previousButton = $("#calendar-previous");

  if (previousButton) {
    previousButton.disabled = false;
  }
}

// Update streak information and calendar.
function renderDailyProgress() {
  createDailyProgressUI();

  const progress = state.dailyProgress;

  if ($("#calendar-current-streak")) {
    $("#calendar-current-streak").textContent =
      Number(progress?.current_streak || 0);
  }

  if ($("#calendar-longest-streak")) {
    $("#calendar-longest-streak").textContent =
      Number(progress?.longest_streak || 0);
  }

  if ($("#calendar-total-days")) {
    $("#calendar-total-days").textContent =
      Number(progress?.total_completed_days || 0);
  }

  const message = $("#calendar-message");

  if (message) {
    if (!getToken()) {
      message.textContent =
        "Log in to track your daily challenge progress.";

    } else if (!progress) {
      message.textContent =
        "Unable to load your progress. Please try again.";

    } else if (progress.completed_today) {
      message.textContent =
        "✓ Today's challenge completed! Come back tomorrow to continue your streak.";

    } else {
      message.textContent =
        "Complete today's Daily Challenge to keep your streak alive!";
    }
  }

  renderDailyCalendar();
}

// Fetch daily challenge progress from FastAPI.
async function loadDailyProgress() {
  createDailyProgressUI();

  if (!getToken()) {
    state.dailyProgress = null;
    state.streak = 0;

    updateStats();
    renderDailyProgress();

    return;
  }

  try {
    const progress = await apiRequest(
      "/api/problems/daily/progress"
    );

    state.dailyProgress = progress;

    // Use the daily challenge streak in the dashboard.
    state.streak = Number(progress.current_streak || 0);

    updateStats();
    renderDailyProgress();

  } catch (error) {
    console.error("Daily progress error:", error);

    state.dailyProgress = null;
    state.streak = 0;

    updateStats();
    renderDailyProgress();
  }
}

// --------------------------------------------------
// SIDEBAR NAVIGATION
// --------------------------------------------------

$$("[data-view]").forEach((button) => {
  button.addEventListener("click", () => {
    $$("[data-view]").forEach((item) => {
      item.classList.toggle("active", item === button);
    });

    const view = button.dataset.view;

    if ($("#breadcrumb-current")) {
      $("#breadcrumb-current").textContent =
        button.querySelector("span")?.textContent ||
        button.textContent.trim();
    }

    if (view === "challenges") {
      $("#problem-list")?.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });

    } else if (view === "learning") {
  openLearningPaths();

    } else if (view === "leaderboard") {
      $(".leaderboard-card")?.scrollIntoView({
        behavior: "smooth",
        block: "center"
      });

    } else {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    }
  });
});

// --------------------------------------------------
// INITIALIZATION
// --------------------------------------------------

$("#account-button").addEventListener("click", () => {
  openAccount("login");
});

if ($("#today-label")) {
  $("#today-label").textContent =
    new Date().toLocaleDateString(undefined, {
      weekday: "long",
      month: "long",
      day: "numeric",
      year: "numeric"
    }).toUpperCase();
}

updateStats();

createDailyProgressUI();
createAchievementsUI();

loadProblems();

loadDailyChallenge();

loadProfile().then(async () => {
  await loadDailyProgress();
  await loadLeaderboard();
  await loadBadges();
});


// --------------------------------------------------
// LEARNING PATHS
// --------------------------------------------------

let learningPaths = [];
let activeLearningPath = null;

// Create the Learning Paths dialog dynamically.
// This avoids changing your existing index.html.
function createLearningDialog() {
  let dialog = document.getElementById("learning-dialog");

  if (dialog) return dialog;

  const style = document.createElement("style");

  style.textContent = `
    #learning-dialog {
      width: min(900px, 94vw);
      max-height: 88vh;
      padding: 0;
      border: 1px solid #343746;
      border-radius: 18px;
      background: #171923;
      color: #f4f4f7;
      overflow: auto;
    }

    #learning-dialog::backdrop {
      background: rgba(0, 0, 0, .75);
      backdrop-filter: blur(4px);
    }

    .learning-modal-header {
      position: sticky;
      top: 0;
      z-index: 2;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      padding: 20px 24px;
      background: #171923;
      border-bottom: 1px solid #343746;
    }

    .learning-modal-header h2 {
      margin: 0;
      font-size: 21px;
    }

    .learning-modal-close {
      border: 0;
      border-radius: 8px;
      padding: 8px 12px;
      background: #292d3b;
      color: white;
      cursor: pointer;
    }

    .learning-modal-body {
      padding: 24px;
    }

    .learning-intro {
      color: #aeb3c4;
      line-height: 1.6;
      margin: 0 0 20px;
    }

    .learning-path-card {
      padding: 20px;
      margin-bottom: 16px;
      border: 1px solid #343746;
      border-radius: 14px;
      background: #202331;
    }

    .learning-path-card h3 {
      margin: 0 0 8px;
    }

    .learning-path-card p {
      color: #aeb3c4;
      line-height: 1.5;
    }

    .learning-progress-track {
      height: 8px;
      border-radius: 20px;
      overflow: hidden;
      background: #363a49;
      margin: 14px 0 8px;
    }

    .learning-progress-fill {
      height: 100%;
      background: #8b75ff;
      border-radius: 20px;
      transition: width .2s ease;
    }

    .learning-muted {
      color: #aeb3c4;
      font-size: 13px;
    }

    .learning-primary-button,
    .learning-secondary-button {
      border: 0;
      border-radius: 9px;
      padding: 11px 16px;
      cursor: pointer;
      font-weight: 600;
      margin-top: 10px;
    }

    .learning-primary-button {
      color: white;
      background: #7659ed;
    }

    .learning-primary-button:disabled {
      opacity: .55;
      cursor: not-allowed;
    }

    .learning-secondary-button {
      color: #eee;
      background: #343849;
    }

    .learning-module {
      margin: 14px 0;
      border: 1px solid #343746;
      border-radius: 12px;
      overflow: hidden;
    }

    .learning-module-title {
      padding: 14px 16px;
      background: #242838;
      font-weight: 700;
    }

    .learning-lesson-row {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      padding: 13px 16px;
      border: 0;
      border-top: 1px solid #343746;
      text-align: left;
      color: #f4f4f7;
      background: #1c202d;
      cursor: pointer;
    }

    .learning-lesson-row:hover {
      background: #292e40;
    }

    .learning-lesson-row small {
      color: #aeb3c4;
    }

    .learning-completed {
      color: #65d6a1;
      font-weight: 700;
    }

    .learning-lesson-content {
      line-height: 1.75;
      color: #e1e3eb;
      white-space: pre-wrap;
    }

    /* Readable lesson explanation formatting */
    .learning-explanation {
      color: #e1e3eb;
      line-height: 1.65;
      white-space: normal;
    }

    .learning-explanation p {
      margin: 8px 0 12px;
    }

    .learning-explanation h4 {
      margin: 16px 0 6px;
      color: #f4f4f7;
      font-size: 15px;
    }

    .learning-explanation-list {
      margin: 6px 0 12px;
      padding-left: 22px;
    }

    .learning-explanation-list li {
      margin: 0 0 6px;
      line-height: 1.5;
    }

    /* Compact spacing for Key Concepts */
    .learning-concepts-list {
      margin: 10px 0 14px;
      padding-left: 22px;
    }

    .learning-concepts-list li {
      margin: 0 0 8px;
      padding: 0;
      line-height: 1.5;
    }

    .learning-concepts-list li:last-child {
      margin-bottom: 0;
    }

    /* Compact, readable MCQ choices */
    .learning-mcq-options {
      display: flex;
      flex-direction: column;
      gap: 7px;
      margin: 12px 0 14px;
    }

    .learning-mcq-options p {
      margin: 0;
      line-height: 1.5;
      color: #e1e3eb;
    }

    .learning-practice-approach {
      margin: 10px 0;
      line-height: 1.55;
      color: #d5d8e2;
    }

    .learning-example {
      padding: 16px;
      border-radius: 10px;
      background: #10131c;
      border: 1px solid #343746;
      overflow-x: auto;
      white-space: pre-wrap;
      color: #a9e5c3;
    }

    .learning-section-title {
      margin: 22px 0 8px;
      font-size: 16px;
    }

    .learning-error {
      color: #ff9292;
      padding: 12px;
    }

    @media (max-width: 600px) {
      .learning-modal-body {
        padding: 16px;
      }

      .learning-modal-header {
        padding: 16px;
      }
    }
  `;

  document.head.appendChild(style);

  dialog = document.createElement("dialog");
  dialog.id = "learning-dialog";

  dialog.innerHTML = `
    <div class="learning-modal-header">
      <h2 id="learning-dialog-title">Learning Paths</h2>
      <button class="learning-modal-close"
        id="learning-dialog-close">✕ Close</button>
    </div>

    <div class="learning-modal-body" id="learning-dialog-body">
      Loading learning paths...
    </div>
  `;

  document.body.appendChild(dialog);

  dialog.querySelector("#learning-dialog-close")
    .addEventListener("click", () => dialog.close());

  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close();
  });

  return dialog;
}

function getLearningPathsArray(data) {
  if (Array.isArray(data)) return data;
  if (Array.isArray(data.paths)) return data.paths;
  if (Array.isArray(data.learning_paths)) return data.learning_paths;
  return [];
}


function getPathId(path) {
  return path.id || path.path_id || path.slug;
}

function getProgressPercentage(path) {
  return Number(
    path.progress?.percentage ??
    path.progress_percentage ??
    0
  );
}

function getLessonId(lesson) {
  return lesson.id || lesson.lesson_id;
}
async function openLearningPaths() {
    const dialog = createLearningDialog();
    const body = document.querySelector("#learning-dialog-body");

    if (!dialog || !body) {
        console.error("Learning Paths dialog elements not found.");
        return;
    }

    body.innerHTML = "<p>Loading learning paths...</p>";

    if (!dialog.open) {
        dialog.showModal();
    }

    try {
        const data = await apiRequest("/api/learning/paths");

        learningPaths = getLearningPathsArray(data);

        renderLearningPaths();

    } catch (error) {
        console.error("Learning Paths Error:", error);

        body.innerHTML = `
            <p>Unable to load learning paths.</p>
            <p>${escapeHTML(error.message)}</p>
        `;
    }
}
function renderLearningPaths() {
  const body = $("#learning-dialog-body");

  if (!learningPaths.length) {
    body.innerHTML = `
      <p>No learning paths are available yet.</p>
    `;
    return;
  }

  body.innerHTML = `
    <p class="learning-intro">
      Choose a structured learning path, complete lessons,
      and earn XP as you improve your coding skills.
    </p>

    ${learningPaths.map((path, index) => {
      const progress = Math.max(
        0,
        Math.min(100, getProgressPercentage(path))
      );

      const modules = Array.isArray(path.modules)
        ? path.modules
        : [];

      const totalLessons = Number(
        path.total_lessons ??
        modules.reduce(
          (total, module) =>
            total + (module.lessons || []).length,
          0
        )
      );

      const completedCount = Number(
        path.progress?.completed_lessons ?? 0
      );

      const pathId = getPathId(path);

      return `
        <div class="learning-path-card">
          <h3>
            ${escapeHTML(path.title || `Learning Path ${index + 1}`)}
          </h3>

          <p>
            ${escapeHTML(
              path.description ||
              "Follow this learning path step by step."
            )}
          </p>

          <div class="learning-progress-track">
            <div
              class="learning-progress-fill"
              style="width: ${progress}%">
            </div>
          </div>

          <div class="learning-muted">
            ${completedCount} of ${totalLessons} lessons completed
            · ${progress}% complete
          </div>

          <button
            class="learning-primary-button"
            data-open-learning-path="${escapeHTML(pathId)}">
            ${progress > 0 ? "Continue Learning" : "Start Learning"} →
          </button>
        </div>
      `;
    }).join("")}
  `;

  $$("[data-open-learning-path]").forEach((button) => {
    button.addEventListener("click", () => {
      openLearningPath(button.dataset.openLearningPath);
    });
  });
}
function openLearningPath(pathId) {
  activeLearningPath = learningPaths.find(
    (path) => String(getPathId(path)) === String(pathId)
  );

  if (!activeLearningPath) {
    showToast("Learning path not found.");
    return;
  }

  renderLearningModules();
}

function renderLearningModules() {
  const path = activeLearningPath;
  const body = $("#learning-dialog-body");

  $("#learning-dialog-title").textContent =
    path.title || "Learning Path";

  const modules = path.modules || [];

  body.innerHTML = `
    <button class="learning-secondary-button"
      id="learning-back-paths">← All learning paths</button>

    <p class="learning-intro">
      ${escapeHTML(path.description || "Complete the lessons in each module.")}
    </p>

    ${modules.map((module, index) => {
      const lessons = module.lessons || [];

      return `
        <section class="learning-module">
          <div class="learning-module-title">
            Module ${index + 1}: ${escapeHTML(module.title || "Module")}
          </div>

          ${lessons.map((lesson) => {
            const lessonId = getLessonId(lesson);
            const completed = Boolean(
              lesson.completed || lesson.is_completed
            );

            return `
              <button class="learning-lesson-row"
                data-open-lesson="${escapeHTML(lessonId)}">

                <span>
                  <strong>${escapeHTML(lesson.title || "Lesson")}</strong>
                  <br>
                  <small>${escapeHTML(lesson.duration || "Lesson")}</small>
                </span>

                <span class="${completed ? "learning-completed" : ""}">
                  ${completed ? "✓ Completed" : "Start →"}
                </span>
              </button>
            `;
          }).join("")}
        </section>
      `;
    }).join("")}
  `;

  $("#learning-back-paths").addEventListener("click", () => {
    renderLearningPaths();
    $("#learning-dialog-title").textContent = "Your Learning Paths";
  });

  $$("[data-open-lesson]").forEach((button) => {
    button.addEventListener("click", () => {
      openLearningLesson(button.dataset.openLesson);
    });
  });
}

async function openLearningLesson(lessonId) {
  const body = $("#learning-dialog-body");

  body.textContent = "Loading lesson...";

  try {
    const result = await apiRequest(
      `/api/learning/lessons/${encodeURIComponent(lessonId)}`
    );

    const lesson = result.lesson || result;
    const completed = Boolean(
      result.completed || lesson.completed || lesson.is_completed
    );

    renderLearningLesson(lesson, completed);

  } catch (error) {
    body.innerHTML = `
      <div class="learning-error">
        Unable to load this lesson: ${escapeHTML(error.message)}
      </div>
      <button class="learning-secondary-button"
        id="learning-back-modules">← Back to modules</button>
    `;

    $("#learning-back-modules").addEventListener(
      "click",
      renderLearningModules
    );
  }
}


function formatLearningValue(value) {
  if (value === null || value === undefined) {
    return "";
  }

  if (typeof value === "string") {
    return value;
  }

  return JSON.stringify(value, null, 2);
}

// Format lesson explanation text without interpreting it as raw HTML.
// Supports numbered headings, bullet points, and ordinary paragraphs.



function formatLearningContent(value) {
    if (!value) {
        return "<p>No content available.</p>";
    }

    const lines = String(value)
        .replace(/\r\n?/g, "\n")
        .split("\n")
        .map(line => line.trim());

    let html = "";
    let paragraph = [];
    let inList = false;

    function closeParagraph() {
        if (paragraph.length) {
            html += `<p>${escapeHTML(paragraph.join(" "))}</p>`;
            paragraph = [];
        }
    }

    function closeList() {
        if (inList) {
            html += "</ul>";
            inList = false;
        }
    }

    function getCells(line) {
        return line
            .trim()
            .replace(/^\|/, "")
            .replace(/\|$/, "")
            .split("|")
            .map(cell => cell.trim());
    }

    function isTableSeparator(line) {
        return /^\|?[\s:|-]+\|?$/.test(line) &&
            line.includes("-") &&
            line.includes("|");
    }

    function renderTable() {
        const header = getCells(lines[i]);
        i += 2; // Skip header and separator.

        let rows = "";

        while (
            i < lines.length &&
            lines[i].includes("|") &&
            lines[i].trim() !== ""
        ) {
            const cells = getCells(lines[i]);

            rows += `<tr>${header.map((_, index) =>
                `<td>${escapeHTML(cells[index] || "")}</td>`
            ).join("")}</tr>`;

            i++;
        }

        html += `
            <div class="learning-table-wrapper">
                <table class="learning-content-table">
                    <thead>
                        <tr>
                            ${header.map(cell =>
                                `<th>${escapeHTML(cell)}</th>`
                            ).join("")}
                        </tr>
                    </thead>
                    <tbody>${rows}</tbody>
                </table>
            </div>
        `;
    }

    for (var i = 0; i < lines.length;) {
        const line = lines[i];

        if (!line) {
            closeParagraph();
            closeList();
            i++;
            continue;
        }

        // Markdown tables
        if (
            line.includes("|") &&
            i + 1 < lines.length &&
            isTableSeparator(lines[i + 1])
        ) {
            closeParagraph();
            closeList();
            renderTable();
            continue;
        }

        // Markdown headings
        if (/^#{1,6}\s+/.test(line)) {
            closeParagraph();
            closeList();

            const level = Math.min(
                line.match(/^#+/)[0].length + 2,
                6
            );

            const heading = line.replace(/^#{1,6}\s+/, "");

            html += `<h${level}>${escapeHTML(heading)}</h${level}>`;
            i++;
            continue;
        }

        // Numbered headings
        if (/^\d+\.\s+/.test(line)) {
            closeParagraph();
            closeList();

            html += `<h4>${escapeHTML(line)}</h4>`;
            i++;
            continue;
        }

        // Bullet points
        if (/^[-•]\s+/.test(line)) {
            closeParagraph();

            if (!inList) {
                html += '<ul class="learning-explanation-list">';
                inList = true;
            }

            html += `<li>${escapeHTML(line.replace(/^[-•]\s+/, ""))}</li>`;
            i++;
            continue;
        }

        closeList();
        paragraph.push(line);
        i++;
    }

    closeParagraph();
    closeList();

    return html;
}




function renderCodeExample(examples) {
  if (!examples || typeof examples !== "object") {
    return `<p class="learning-muted">No examples available.</p>`;
  }

  const languages = ["python", "java", "cpp"];

  return languages.map((language) => {
    const example = examples[language];

    if (!example) return "";

    return `
      <h4 class="learning-section-title">
        ${language.toUpperCase()} Example
      </h4>

      <pre class="learning-example">${escapeHTML(
        formatLearningValue(example.code)
      )}</pre>

      ${example.output ? `
        <p class="learning-muted">Expected Output</p>
        <pre class="learning-example">${escapeHTML(
          formatLearningValue(example.output)
        )}</pre>
      ` : ""}
    `;
  }).join("");
}

function renderLearningLesson(lesson, completed) {
  const body = $("#learning-dialog-body");

  $("#learning-dialog-title").textContent =
    lesson.title || "Lesson";

  const concepts = Array.isArray(lesson.key_concepts)
    ? lesson.key_concepts
    : [];

  const practiceQuestions = Array.isArray(lesson.practice_questions)
    ? lesson.practice_questions.map((question) => ({
        ...question,
        question:
          question.question ||
          question.problem ||
          question.title ||
          "Practice Question",
        level: question.level || question.difficulty || "Practice",
        solutions: question.solutions || question.solution || {},
        sample_output:
          question.sample_output ?? question.expected_output ?? ""
      }))
    : [];

  const interviewQuestions = Array.isArray(lesson.interview_questions)
    ? lesson.interview_questions
    : [];

  const mcqs = Array.isArray(lesson.mcqs)
    ? lesson.mcqs
    : [];

  const examples = renderCodeExample(lesson.examples);

  const dryRun = formatLearningValue(lesson.dry_run);

  body.innerHTML = `
    <button class="learning-secondary-button"
      id="learning-back-modules">
      ← Back to modules
    </button>

    <h3>${escapeHTML(lesson.title || "Lesson")}</h3>

    <p class="learning-muted">
      ${escapeHTML(lesson.duration || "15 min")}
    </p>

    ${lesson.subtitle ? `
      <p class="learning-intro">
        ${escapeHTML(lesson.subtitle)}
      </p>
    ` : ""}

    <h3 class="learning-section-title">
      Lesson Explanation
    </h3>

    <div class="learning-explanation">
      ${formatLearningContent(lesson.content || lesson.description || "No content available.")}
    </div>

    ${concepts.length ? `
      <h3 class="learning-section-title">Key Concepts</h3>

      <ul class="learning-concepts-list">
        
${concepts.map((concept) => {
    if (typeof concept === "string") {
        return `<li>${escapeHTML(concept)}</li>`;
    }

    const title =
        concept.title ||
        concept.name ||
        concept.concept ||
        concept.term ||
        concept.heading ||
        concept.text ||
        "";

    const description =
    concept.description ||
    concept.definition ||
    concept.explanation ||
    concept.details ||
    concept.meaning ||
    "";

    return `
        <li>
            ${title ? `<strong>${escapeHTML(String(title))}</strong>` : ""}
            ${description ? `: ${escapeHTML(String(description))}` : ""}
            ${!title && !description
                ? escapeHTML(JSON.stringify(concept))
                : ""}
        </li>
    `;
}).join("")}

      </ul>
    ` : ""}

    <h3 class="learning-section-title">
      Code Examples
    </h3>

    ${examples}

    ${dryRun ? `
      <h3 class="learning-section-title">
        Dry Run / Step-by-Step Walkthrough
      </h3>

      <pre class="learning-example">${escapeHTML(dryRun)}</pre>
    ` : ""}

    ${practiceQuestions.length ? `
      <h3 class="learning-section-title">
        Practice Questions and Solutions
      </h3>

      ${practiceQuestions.map((question, index) => {
        const solutions = question.solutions || {};

        return `
          <div class="learning-path-card">
            <h4>
              ${index + 1}. ${escapeHTML(question.question || "Practice Question")}
            </h4>

            <p class="learning-muted">
              Difficulty: ${escapeHTML(question.level || "Practice")}
            </p>

            ${question.approach ? `
              <p class="learning-practice-approach">
                <strong>Approach:</strong> ${escapeHTML(question.approach)}
              </p>
            ` : ""}

            ${question.sample_input !== undefined ? `
              <p><strong>Sample Input</strong></p>
              <pre class="learning-example">${escapeHTML(
                formatLearningValue(question.sample_input)
              )}</pre>
            ` : ""}

            ${question.sample_output !== undefined ? `
              <p><strong>Sample Output</strong></p>
              <pre class="learning-example">${escapeHTML(
                formatLearningValue(question.sample_output)
              )}</pre>
            ` : ""}

            ${["python", "java", "cpp"].map((language) => {
              if (!solutions[language]) return "";

              return `
                <details>
                  <summary>
                    View ${language.toUpperCase()} Solution
                  </summary>

                  <pre class="learning-example">${escapeHTML(
                    formatLearningValue(solutions[language])
                  )}</pre>
                </details>
              `;
            }).join("")}

            ${question.explanation ? `
              <p class="learning-lesson-content">
                <strong>Explanation:</strong>
                ${escapeHTML(question.explanation)}
              </p>
            ` : ""}
          </div>
        `;
      }).join("")}
    ` : ""}

    ${interviewQuestions.length ? `
      <h3 class="learning-section-title">
        Interview Questions
      </h3>

      ${interviewQuestions.map((item, index) => `
        <details class="learning-path-card">
          <summary>
            ${index + 1}. ${escapeHTML(item.question || "")}
          </summary>

          <p class="learning-lesson-content">
            ${escapeHTML(item.answer || "Answer not available.")}
          </p>
        </details>
      `).join("")}
    ` : ""}

    ${mcqs.length ? `
      <h3 class="learning-section-title">
        Multiple Choice Questions (MCQs)
      </h3>

      ${mcqs.map((mcq, index) => `
        <div class="learning-path-card">
          <strong>
            ${index + 1}. ${escapeHTML(mcq.question || "")}
          </strong>

          <div class="learning-mcq-options">
            ${(mcq.options || []).map((option, optionIndex) => `
              <p>
                <strong>${String.fromCharCode(65 + optionIndex)}.</strong>
                ${escapeHTML(option)}
              </p>
            `).join("")}
          </div>

          <details>
            <summary>Show Answer</summary>

            <p>
              <strong>Answer:</strong>
              ${escapeHTML(mcq.answer ?? "Not available")}
            </p>

            ${mcq.explanation ? `
              <p>${escapeHTML(mcq.explanation)}</p>
            ` : ""}
          </details>
        </div>
      `).join("")}
    ` : ""}

    <button class="learning-primary-button"
      id="complete-learning-lesson"
      ${completed ? "disabled" : ""}>
      ${completed ? "✓ Lesson Completed" : "Mark Lesson Complete (+10 XP)"}
    </button>

    <p class="learning-muted" id="learning-completion-message">
      ${completed
        ? "You have already completed this lesson."
        : "Complete this lesson to earn 10 XP."}
    </p>
  `;

  $("#learning-back-modules").addEventListener(
    "click",
    renderLearningModules
  );

  if (!completed) {
    $("#complete-learning-lesson").addEventListener(
      "click",
      () => completeLearningLesson(getLessonId(lesson))
    );
  }
}
async function completeLearningLesson(lessonId) {
  const button = $("#complete-learning-lesson");
  const message = $("#learning-completion-message");

  if (!getToken()) {
    showToast("Please log in first.");
    return;
  }

  button.disabled = true;
  button.textContent = "Saving progress...";

  try {
    const result = await apiRequest(
      `/api/learning/lessons/${encodeURIComponent(lessonId)}/complete`,
      {
        method: "POST"
      }
    );

    const awardedXP = Number(
      result.xp_earned ??
      result.awarded_xp ??
      result.xp_awarded ??
      0
    );

    button.textContent = "✓ Lesson Completed";

    message.textContent = result.message ||
      `Lesson completed! You earned ${awardedXP} XP.`;

    if (result.already_completed) {
      showToast("You already completed this lesson.");
    } else {
      showToast(`Lesson completed! +${awardedXP} XP`);
    }

    // Refresh user XP and profile.
    await loadProfile();
    await loadBadges();

    // Refresh learning path progress from backend.
    const data = await apiRequest("/api/learning/paths");

    learningPaths = getLearningPathsArray(data);

    // Update the active learning path.
    if (activeLearningPath) {
      const activePathId = getPathId(activeLearningPath);

      activeLearningPath = learningPaths.find(
        path =>
          String(getPathId(path)) === String(activePathId)
      ) || activeLearningPath;
    }

    // Mark the lesson as completed in the refreshed path.
    learningPaths.forEach((path) => {
      (path.modules || []).forEach((module) => {
        (module.lessons || []).forEach((lesson) => {
          if (
            String(getLessonId(lesson)) === String(lessonId)
          ) {
            lesson.completed = true;
          }
        });
      });
    });

  } catch (error) {
    button.disabled = false;
    button.textContent = "Mark Lesson Complete (+10 XP)";

    message.textContent = error.message;

    showToast(error.message);
  }
}
// Make existing learning cards clickable.
$$(".learning-card").forEach((card) => {
  card.style.cursor = "pointer";

  card.addEventListener("click", () => {
    openLearningPaths();
  });
});
