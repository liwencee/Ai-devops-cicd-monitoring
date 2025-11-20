# Ai-devops-cicd-monitoring
AI and ML Authomation of a CI
# 🤖 AI-Powered CI/CD and Monitoring Stack

This project demonstrates a full-stack DevOps pipeline enhanced with AI for intelligent monitoring and alerting. It uses **GitHub Actions**, **Docker**, **Prometheus**, **Grafana**, and **OpenAI's GPT** to build, monitor, and auto-notify on incidents through Slack.

---

## 🚀 Features

- ✅ **CI/CD pipeline** via GitHub Actions
- 🧠 **AI-based log and anomaly summarization** using GPT-4
- 📊 Real-time monitoring with **Prometheus + Grafana**
- 🔔 Slack alerts with GPT-powered summaries
- 🐳 Dockerized frontend and backend apps
- 🔍 Automatic Slack alert testing

---

## 📁 Project Structure

i-devops-cicd-monitoring/
├── .github/workflows/ci.yml # GitHub Actions pipeline
├── backend/ # Flask API (Python)
│ ├── app.py
│ └── Dockerfile
├── frontend/ # Frontend stub (Node.js)
│ ├── app.js
│ └── Dockerfile
├── ai/ # AI log classification
│ ├── log_classifier.py
│ └── logs/sample_logs.txt
├── monitoring/ # Anomaly detection with ML
│ ├── ml_anomaly_detection.py
│ └── prometheus.yml
├── tests/ # Slack alert test
│ └── test_slack_alert.py
├── docker-compose.yml # Local dev + monitoring stack

markdown
Copy
Edit

---

## 🔧 Technologies Used

- **CI/CD**: GitHub Actions
- **Containers**: Docker, Docker Compose
- **Monitoring**: Prometheus + Grafana
- **AI/NLP**: OpenAI GPT-4
- **Anomaly Detection**: Isolation Forest (Scikit-learn)
- **Alerts**: Slack (via Webhooks)

---

## 🛠 How It Works

### 1. CI Pipeline
- Triggered on push or pull request
- Builds Docker images for frontend and backend
- Runs:
  - AI log classifier (GPT summarization)
  - Slack test alert

### 2. Monitoring with AI
- `ml_anomaly_detection.py`:
  - Detects outliers in CPU/memory usage
  - GPT-4 writes a human-readable incident summary
  - Sends alert to Slack

- `log_classifier.py`:
  - Scans logs for critical errors
  - Summarizes logs with GPT
  - Sends alert to Slack

### 3. Observability Stack
- Prometheus scrapes metrics
- Grafana visualizes them
- Docker Compose runs services locally

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/Ai-devops-cicd-monitoring.git
   cd Ai-devops-cicd-monitoring
Set environment variables

bash
Copy
Edit
export SLACK_WEBHOOK_URL="your-slack-webhook-url"
export OPENAI_API_KEY="your-openai-api-key"
Run locally with Docker Compose

bash
Copy
Edit
docker-compose up --build
Test Slack alerts

bash
Copy
Edit
python tests/test_slack_alert.py
📈 Dashboards
Prometheus: http://localhost:9090

Grafana: http://localhost:3001 (login: admin / admin)

🧪 Sample Log Alerts
Logs in ai/logs/sample_logs.txt are used to simulate real system logs. Any lines containing ERROR, FAIL, or EXCEPTION trigger Slack alerts.

📬 Slack Alert Preview
Example alert from log classifier:

pgsql
Copy
Edit
⚠️ Log Alert: ERROR: Out of memory
📘 Summary: The application ran out of memory due to excessive resource usage. Please check for memory leaks.
📌 Future Improvements
✅ ECS or Kubernetes deployment automation

🔐 Slack signature verification

🧪 GPT-based test case generator

📡 Real-time metrics ingestion from containers

🧠 Credits
Built using OpenAI GPT-4

Monitoring with Prometheus + Grafana

CI/CD with GitHub Actions

Containerization by Docker

📄 License
MIT License

yaml
Copy
Edit

