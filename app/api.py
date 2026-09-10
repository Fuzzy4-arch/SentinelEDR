from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.core.scanner import scan_endpoint
from app.core.process_monitor import get_running_processes
from app.core.network_monitor import get_network_connections
from app.storage.database import get_alerts, initialize_database


app = FastAPI(
    title="SentinelEDR API",
    description="Endpoint Detection and Response API",
    version="1.0.0",
)

initialize_database()

DASHBOARD = Path(__file__).parent / "templates" / "dashboard.html"


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return DASHBOARD.read_text(encoding="utf-8")


@app.get("/scan")
def run_scan():
    return scan_endpoint()


@app.get("/processes")
def processes():
    return get_running_processes()


@app.get("/network")
def network():
    return get_network_connections()


@app.get("/alerts")
def alerts():
    return get_alerts()