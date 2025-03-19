import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

message = {
    "text": "🚨 GitHub Workflow Failed! AI is working on a fix."
}
requests.post(SLACK_WEBHOOK, json=message)
