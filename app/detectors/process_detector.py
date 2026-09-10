SUSPICIOUS_NAMES = {
    "mimikatz.exe",
    "procdump.exe",
    "psexec.exe",
    "nc.exe",
    "netcat.exe",
}


def analyze_process(process):
    alerts = []

    name = (process.get("name") or "").lower()
    exe = process.get("exe") or ""
    cmdline = " ".join(process.get("cmdline") or []).lower()

    if name in SUSPICIOUS_NAMES:
        alerts.append({
            "type": "SUSPICIOUS_PROCESS",
            "severity": "HIGH",
            "risk": 80,
            "pid": process.get("pid"),
            "process": process.get("name"),
            "reason": "Known suspicious process name",
        })

    suspicious_commands = [
        "encodedcommand",
        "bypass",
        "downloadstring",
        "invoke-expression",
        "powershell -enc",
    ]

    for keyword in suspicious_commands:
        if keyword in cmdline:
            alerts.append({
                "type": "SUSPICIOUS_COMMAND",
                "severity": "HIGH",
                "risk": 85,
                "pid": process.get("pid"),
                "process": process.get("name"),
                "reason": f"Suspicious command-line argument: {keyword}",
            })
            break

    if exe and (
        "\\temp\\" in exe.lower()
        or "\\appdata\\local\\temp\\" in exe.lower()
    ):
        alerts.append({
            "type": "SUSPICIOUS_LOCATION",
            "severity": "MEDIUM",
            "risk": 60,
            "pid": process.get("pid"),
            "process": process.get("name"),
            "reason": "Executable running from a temporary directory",
        })

    return alerts