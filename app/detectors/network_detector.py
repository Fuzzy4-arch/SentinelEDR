SUSPICIOUS_PORTS = {
    4444,
    5555,
    1337,
    31337,
    6667,
}


def analyze_connection(connection):
    alerts = []

    remote = connection.get("remote")
    process = connection.get("process")
    pid = connection.get("pid")

    if not remote:
        return alerts

    try:
        remote_port = int(remote.rsplit(":", 1)[1])
    except (ValueError, IndexError):
        return alerts

    if remote_port in SUSPICIOUS_PORTS:
        alerts.append({
            "type": "SUSPICIOUS_NETWORK_CONNECTION",
            "severity": "HIGH",
            "risk": 85,
            "pid": pid,
            "process": process,
            "reason": f"Connection to suspicious port {remote_port}",
            "remote": remote,
        })

    return alerts