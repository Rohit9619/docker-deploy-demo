import openai
import requests
import os

GITHUB_TOKEN = os.getenv("GH_PAT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_OWNER = "Rohit9619"
REPO_NAME = "docker-deploy-demo"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_latest_logs():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs"
    response = requests.get(url, headers=headers)
    runs = response.json().get("workflow_runs", [])
    
    if runs:
        logs_url = runs[0]["logs_url"]
        logs_response = requests.get(logs_url, headers=headers)
        return logs_response.text[:2000]  # Limit to 2000 chars for GPT-4

def analyze_logs():
    logs = get_latest_logs()
    if not logs:
        return "No logs available."

    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze GitHub Actions logs and suggest fixes."},
                  {"role": "user", "content": logs}]
    )
    return response["choices"][0]["message"]["content"]

fix = analyze_logs()
print(f"🛠 Suggested Fix: {fix}")
