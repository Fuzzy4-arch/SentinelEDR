import psutil


def get_running_processes():
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username", "exe", "cmdline"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "username": info["username"],
                "exe": info["exe"],
                "cmdline": info["cmdline"],
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes


if __name__ == "__main__":
    processes = get_running_processes()

    print(f"Processes detected: {len(processes)}")

    for process in processes[:10]:
        print(
            f'PID={process["pid"]} '
            f'NAME={process["name"]} '
            f'USER={process["username"]}'
        )