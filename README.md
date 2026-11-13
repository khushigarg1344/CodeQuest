# CodeQuest

CodeQuest is a gamified coding and DSA practice web app built with vanilla HTML/CSS/JavaScript, Vite, FastAPI, SQLAlchemy, and SQLite for local development.

## Current features

- Seeded DSA problems loaded from FastAPI
- Registration and login with hashed passwords and JWT authentication
- Per-user XP, level, practice history, streak, and milestone badges stored in SQLite
- Leaderboard backed by registered users' XP
- Interactive responsive dashboard

## Run locally on Windows

### 1. Backend setup

Open a terminal in the project folder, then:

```powershell
cd backend
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `backend/.env`. For local development, keep SQLite configured as:

```env
DATABASE_URL=sqlite:///./codequest.db
SECRET_KEY=replace_this_with_a_long_random_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
FRONTEND_ORIGINS=http://127.0.0.1:5173,http://localhost:5173,http://127.0.0.1:5174,http://localhost:5174
```

Replace `SECRET_KEY` with a long random value. You can generate one using:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Then start the backend **from inside the `backend` folder**:

```powershell
python -m uvicorn main:app --reload
```

Check `http://127.0.0.1:8000/health` and open `http://127.0.0.1:8000/docs` for API testing.

### 2. Frontend setup

Open a second terminal in the project root (the folder containing `package.json`):

```powershell
npm install
npm run dev
```

Open the local URL Vite prints in the terminal. Keep both terminals running.

## Test registration and login

1. Open the frontend and select **Log in / Register** in the sidebar.
2. Create an account with a name, valid email, and password of at least 8 characters.
3. Open a challenge and choose **Mark as practiced**. Your XP and progress are saved to SQLite.
4. Refresh the page; your account's saved progress should load again.
5. Try marking the same problem as practiced a second time; XP should not be awarded again for that problem.
6. Log out, then log back in with the same credentials.

You can also test the `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/users/me`, `POST /api/users/me/practice/{problem_id}`, and `GET /api/users/leaderboard` endpoints in Swagger. For protected endpoints, click **Authorize** and enter `Bearer YOUR_ACCESS_TOKEN` if Swagger prompts for a bearer token.

## Important notes

- `backend/.env` contains secrets and should never be committed or shared.
- SQLite is used for the current local build; `codequest.db` is created/updated when the backend starts.
- The current practice button records a practice event; it does not yet compile or verify submitted source code. Judge0 execution and the AI tutor/RAG workflow are subsequent implementation phases.
