# Application Health Checker (Python)

import requests

# Application URL to monitor
APP_URL = "https://example.com"  # Replace with your application URL

def check_application_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if 200 <= response.status_code < 400:
            print(f"The application is UP. Status Code: {response.status_code}")
        else:
            print(f"The application is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application is DOWN. Error: {e}")

if __name__ == "__main__":
    check_application_health()

# ✅ This script checks if the application is up based on HTTP status code (should be 200 OK).

