import re
import requests
import os
import openai

with open('ai/logs/sample_logs.txt') as f:
    logs = f.readlines()

openai.api_key = os.environ.get("OPENAI_API_KEY")

summary_context = "Summarize these critical logs for alerting:\n" + "\n".join(logs)
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": summary_context}]
    )
    log_summary = response.choices[0].message['content'].strip()
except Exception:
    log_summary = "Critical log events detected. (Summary generation failed)"

for line in logs:
    if re.search("ERROR|FAIL|EXCEPTION", line):
        print("[ALERT]", line.strip())
        slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
        if slack_webhook:
            requests.post(slack_webhook, json={"text": f"⚠️ Log Alert: {line.strip()}\n📘 Summary: {log_summary}"})
        else:
            print("Slack webhook URL not found in environment variables.")