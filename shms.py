import psutil
import shutil
import logging

# Set threshold values
CPU_THRESHOLD = 80  # in %
MEMORY_THRESHOLD = 80  # in %
DISK_THRESHOLD = 80  # in %

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = shutil.disk_usage('/').used / shutil.disk_usage('/').total * 100

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")

    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")

    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage:.2f}%")

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage:.2f}%")

if __name__ == "__main__":
    check_system_health()
# //✅ It will log warnings into a file if CPU, Memory, or Disk usage crosses the threshold.
