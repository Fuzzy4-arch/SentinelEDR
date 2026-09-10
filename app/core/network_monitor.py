import psutil


def get_network_connections():
    connections = []

    for connection in psutil.net_connections(kind="inet"):
        try:
            process_name = None

            if connection.pid:
                try:
                    process_name = psutil.Process(connection.pid).name()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    process_name = "Unknown"

            local_address = (
                f"{connection.laddr.ip}:{connection.laddr.port}"
                if connection.laddr
                else None
            )

            remote_address = (
                f"{connection.raddr.ip}:{connection.raddr.port}"
                if connection.raddr
                else None
            )

            connections.append({
                "pid": connection.pid,
                "process": process_name,
                "local": local_address,
                "remote": remote_address,
                "status": connection.status,
            })

        except Exception:
            continue

    return connections


if __name__ == "__main__":
    connections = get_network_connections()

    print("=" * 60)
    print("        SENTINELEDR NETWORK MONITOR")
    print("=" * 60)

    print(f"Connections detected: {len(connections)}")

    for connection in connections[:20]:
        print(
            f'PID={connection["pid"]} '
            f'PROCESS={connection["process"]} '
            f'LOCAL={connection["local"]} '
            f'REMOTE={connection["remote"]} '
            f'STATUS={connection["status"]}'
        )