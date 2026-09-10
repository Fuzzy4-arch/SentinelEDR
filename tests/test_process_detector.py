from app.detectors.process_detector import analyze_process


def test_detects_suspicious_process():
    process = {
        "pid": 1234,
        "name": "mimikatz.exe",
        "exe": r"C:\Windows\mimikatz.exe",
        "cmdline": [],
    }

    alerts = analyze_process(process)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "SUSPICIOUS_PROCESS"
    assert alerts[0]["severity"] == "HIGH"
    assert alerts[0]["risk"] == 80


def test_normal_process_has_no_alert():
    process = {
        "pid": 5678,
        "name": "notepad.exe",
        "exe": r"C:\Windows\notepad.exe",
        "cmdline": [],
    }

    alerts = analyze_process(process)

    assert alerts == []


def test_detects_suspicious_command():
    process = {
        "pid": 9999,
        "name": "powershell.exe",
        "exe": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
        "cmdline": ["powershell", "-EncodedCommand", "test"],
    }

    alerts = analyze_process(process)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "SUSPICIOUS_COMMAND"
    assert alerts[0]["severity"] == "HIGH"