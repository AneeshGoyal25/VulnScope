import requests
import time


def get_website_info(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=10)

        end_time = time.time()

        return {
            "status": "success",
            "status_code": response.status_code,
            "response_time": round(end_time - start_time, 3)
        }

    except requests.exceptions.RequestException:

        return {
            "status": "error",
            "message": "Website could not be reached."
        }