
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

JUDGE0_URL = os.getenv(
    "JUDGE0_API_URL",
    "https://ce.judge0.com"
).rstrip("/")

# Judge0 language IDs
LANGUAGE_IDS = {
    "python": 100,
    "java": 91,
    "cpp": 105
}


def execute_code(source_code: str, language: str, stdin: str = ""):
    """
    Submit code to Judge0 and return its execution result.
    """

    language = language.lower().strip()

    if language not in LANGUAGE_IDS:
        raise ValueError(
            "Unsupported language. Use Python, Java or C++."
        )

    language_id = LANGUAGE_IDS[language]

    # Step 1: Submit code
    submission_url = f"{JUDGE0_URL}/submissions"

    payload = {
        "source_code": source_code,
        "language_id": language_id,
        "stdin": stdin
    }

    response = requests.post(
        submission_url,
        params={"base64_encoded": "false", "wait": "false"},
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    token = response.json().get("token")

    if not token:
        raise RuntimeError("Judge0 did not return a submission token.")

    # Step 2: Poll for execution result
    result_url = f"{JUDGE0_URL}/submissions/{token}"

    for _ in range(30):
        result_response = requests.get(
            result_url,
            params={
                "base64_encoded": "false",
                "fields": "stdout,stderr,compile_output,message,status"
            },
            timeout=30
        )

        result_response.raise_for_status()
        result = result_response.json()

        status_id = result.get("status", {}).get("id")

        # 1 = In Queue, 2 = Processing
        if status_id not in (1, 2):
            return {
                "status": result.get("status", {}).get("description"),
                "status_id": status_id,
                "output": result.get("stdout"),
                "error": (
                    result.get("stderr")
                    or result.get("compile_output")
                    or result.get("message")
                ),
                "time": result.get("time"),
                "memory": result.get("memory")
            }

        time.sleep(1)

    raise TimeoutError("Code execution timed out while waiting for Judge0.")
