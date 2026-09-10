\# SentinelEDR



SentinelEDR is a Python-based Endpoint Detection and Response (EDR) platform designed to monitor Windows endpoints, analyze running processes and network connections, detect suspicious activity, store security alerts, and expose security telemetry through a FastAPI dashboard.



\## Features



\* Live Windows process monitoring

\* Network connection monitoring

\* Suspicious process detection

\* Suspicious PowerShell command detection

\* Suspicious executable location detection

\* Suspicious network-port detection

\* Risk-based alert classification

\* SQLite alert storage

\* FastAPI REST API

\* Interactive security dashboard

\* Automated tests with pytest

\* GitHub Actions CI



\## Architecture



```text

Windows Endpoint

&#x20;      |

&#x20;      v

Process Monitor -----> Process Detector

&#x20;      |

&#x20;      +--------------> Network Monitor

&#x20;                             |

&#x20;                             v

&#x20;                      Network Detector

&#x20;                             |

&#x20;                             v

&#x20;                        Alert Engine

&#x20;                             |

&#x20;                             v

&#x20;                        SQLite DB

&#x20;                             |

&#x20;                             v

&#x20;                      FastAPI Dashboard

```



\## API



| Endpoint     | Purpose                   |

| ------------ | ------------------------- |

| `/`          | EDR dashboard             |

| `/processes` | Running processes         |

| `/network`   | Network connections       |

| `/alerts`    | Stored security alerts    |

| `/scan`      | Run endpoint scan         |

| `/docs`      | FastAPI API documentation |



\## Detection Examples



SentinelEDR can identify:



\* Known suspicious process names

\* Suspicious PowerShell command-line arguments

\* Executables running from temporary directories

\* Connections to suspicious ports such as `4444`, `5555`, and `1337`



\## Testing



Run:



```bash

py -m pytest -v

```



\## Technology Stack



\* Python

\* FastAPI

\* Uvicorn

\* psutil

\* SQLite

\* pytest

\* GitHub Actions



\## Disclaimer



This project is intended for cybersecurity learning, defensive security research, and portfolio demonstration.



