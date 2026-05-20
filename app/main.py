from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response
import os

app = FastAPI()

# Custom Prometheus metric
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total App HTTP Request Count"
)

healthy = True


@app.get("/")
def home():
    REQUEST_COUNT.inc()

    x = 0
    for i in range(10**7):   # 🔥 heavy CPU work
        x += i * i

    return {
        "message": "CPU load generated",
        "value": x
    }


@app.get("/health")
def health():
    if healthy:
        return {"status": "healthy"}
    else:
        return {"status": "unhealthy"}


@app.get("/simulate-failure")
def simulate_failure():
    global healthy
    healthy = False
    return {"message": "Failure simulated"}


@app.get("/crash")
def crash():
    os._exit(1)


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )