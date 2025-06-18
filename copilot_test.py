import platform
from datetime import datetime

def get_windows_uptime():
    """
    Returns system uptime in seconds on Windows using WMIC.
    """
    try:
        import subprocess
        result = subprocess.run(
            ['wmic', 'os', 'get', 'lastbootuptime'], 
            capture_output=True, text=True, check=True
        )
        lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        if len(lines) >= 2:
            boot_time_str = lines[1][:14]  # Format: YYYYMMDDhhmmss
            boot_time = datetime.strptime(boot_time_str, "%Y%m%d%H%M%S")
            now = datetime.now()
            return (now - boot_time).total_seconds()
    except Exception as e:
        return None

def get_unix_uptime():
    """
    Returns system uptime in seconds on Unix-like systems.
    """
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    except Exception:
        # Fallback to 'uptime' command
        try:
            import subprocess
            result = subprocess.run(['uptime', '-s'], capture_output=True, text=True, check=True)
            boot_time_str = result.stdout.strip()
            boot_time = datetime.strptime(boot_time_str, "%Y-%m-%d %H:%M:%S")
            now = datetime.now()
            return (now - boot_time).total_seconds()
        except Exception:
            return None

def format_uptime(seconds):
    """
    Formats uptime in seconds to a human-readable string.
    """
    if not seconds:
        return "Could not determine uptime."
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

def main():
    system = platform
    uptime = None
    if system.system() == "Windows":
        uptime = get_windows_uptime()
    else:
        uptime = get_unix_uptime()
    
    if isinstance(uptime, (float, int)):
        print("System uptime:", format_uptime(uptime))
    else:
        print("Could not determine uptime.")

if __name__ == "__main__":
    main()

