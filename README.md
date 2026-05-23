# AutoOps - DevOps Monitoring Project

A complete DevOps monitoring project built using:

- Docker
- Kubernetes
- Prometheus
- Grafana
- FastAPI

## Features

- Containerized Python application
- Kubernetes deployment and scaling
- Prometheus metrics monitoring
- Grafana dashboards visualization
- CPU load simulation
- Pod failure and auto-restart testing
- Real-time monitoring dashboards

## Tech Stack

- Python FastAPI
- Docker
- Kubernetes
- Prometheus
- Grafana

## Architecture Flow

User Request → FastAPI App → Prometheus Metrics → Grafana Dashboard

- FastAPI application exposes metrics
- Prometheus scrapes metrics
- Grafana visualizes monitoring dashboards
- Kubernetes manages pods and auto-restarts

## Monitoring Dashboards

- Node Exporter Full Dashboard
- Kubernetes Compute Resources Dashboard
- CPU / Memory / Disk Monitoring

## Project Screenshots

(Add your screenshots here later)

---

## 🏗️ Architecture Flow

```text
User Request
     ↓
FastAPI Application
     ↓
Prometheus Metrics Endpoint
     ↓
Prometheus Scraping
     ↓
Grafana Dashboard Visualization
     ↓
Kubernetes Pod Monitoring
```

---

## ⚙️ API Endpoints

| Endpoint | Purpose |
|----------|----------|
| `/` | Home endpoint |
| `/metrics` | Prometheus metrics |
| `/health` | Health check |
| `/cpu` | CPU load simulation |
| `/simulate-failure` | Simulate pod failure |

---

## 📁 Project Structure

```text
AutoOps/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── deployment.yaml
│
├── Dockerfile
├── metrics-patch.yaml
├── metrics-server-full.yaml
└── README.md
```

---

## 🚀 Future Improvements

- Add CI/CD pipeline using GitHub Actions
- Add alerting with Alertmanager
- Add Slack/Email notifications
- Add Helm charts
- Deploy on cloud Kubernetes cluster

---

---

## ▶️ How To Run The Project

### Clone Repository

```bash
git clone https://github.com/24adarshs/AutoOps.git
cd AutoOps
```

### Build Docker Image

```bash
docker build -t autoops:v3 .
```

### Apply Kubernetes Deployment

```bash
kubectl apply -f app/deployment.yaml
```

### Start Monitoring Stack

```bash
kubectl apply -f metrics-server-full.yaml
kubectl apply -f metrics-patch.yaml
```

### Check Running Pods

```bash
kubectl get pods
```

### Access Grafana

```text
http://localhost:3001
```

### Access FastAPI App

```text
http://localhost:8001
```

## Author

Adarsh Sharma
