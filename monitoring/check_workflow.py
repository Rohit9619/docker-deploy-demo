import requests
import os

GITHUB_TOKEN = os.getenv("GH_PAT")
REPO_OWNER = "your-username"
REPO_NAME = "your-repo"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

def check_workflow_status():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs"
    response = requests.get(url, headers=headers)
    runs = response.json().get("workflow_runs", [])

    if runs:
        latest_run = runs[0]
        status = latest_run["conclusion"]
        if status not in ["success", None]:
            print(f"⚠️ Workflow failed: {latest_run['html_url']}")
            return False
    return True

if not check_workflow_status():
    os.system("python3 monitoring/alert.py")  # Trigger alert if failed
