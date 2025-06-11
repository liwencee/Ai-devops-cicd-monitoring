import requests
import os

slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")

if slack_webhook:
    test_message = {
        "text": "✅ Slack alert test successful from CI pipeline."
    }
    response = requests.post(slack_webhook, json=test_message)
    print(f"Slack test alert status: {response.status_code}")
else:
    print("SLACK_WEBHOOK_URL not set.")
