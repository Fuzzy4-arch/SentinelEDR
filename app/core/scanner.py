from app.core.process_monitor import get_running_processes
from app.core.network_monitor import get_network_connections

from app.detectors.process_detector import analyze_process
from app.detectors.network_detector import analyze_connection

from app.storage.database import initialize_database, save_alert


def scan_endpoint():
    processes = get_running_processes()
    connections = get_network_connections()

    alerts = []

    # Process detection
    for process in processes:
        alerts.extend(analyze_process(process))

    # Network detection
    for connection in connections:
        alerts.extend(analyze_connection(connection))

    # Store alerts
    for alert in alerts:
        save_alert(alert)

    return {
        "processes_scanned": len(processes),
        "connections_scanned": len(connections),
        "alerts_detected": len(alerts),
    }


if __name__ == "__main__":
    initialize_database()

    result = scan_endpoint()

    print("=" * 55)
    print("        SENTINELEDR ENDPOINT SCAN")
    print("=" * 55)

    print(f"Processes scanned: {result['processes_scanned']}")
    print(f"Network connections: {result['connections_scanned']}")
    print(f"Alerts detected: {result['alerts_detected']}")

    if result["alerts_detected"] == 0:
        print("No suspicious activity detected.")