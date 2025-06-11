import pandas as pd
from sklearn.ensemble import IsolationForest
import requests
import os
import openai

# Load dummy metric data
metrics = pd.read_csv('monitoring/sample_metrics.csv')

model = IsolationForest(contamination=0.05)
metrics['anomaly'] = model.fit_predict(metrics[['cpu_usage', 'memory_usage']])

# Alert logic
if (metrics['anomaly'] == -1).any():
    print("Anomaly detected! Notifying Slack...")
    slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if slack_webhook:
        summary_prompt = f"Summarize this incident report in one sentence: Anomaly detected in metrics:\n{metrics.to_string()}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": summary_prompt}]
            )
            summary = response.choices[0].message['content'].strip()
        except Exception as e:
            summary = "Anomaly detected in metrics. (Summary failed to generate)"

        requests.post(slack_webhook, json={"text": f"🚨 AI Monitoring Alert: {summary}"})
    else:
        print("Slack webhook URL not found in environment variables.")