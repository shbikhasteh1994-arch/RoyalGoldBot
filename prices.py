
import requests
from bs4 import BeautifulSoup


def get_prices():
    try:
        url = "https://www.tgju.org/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        return {
            "gold18": "در حال دریافت...",
            "gold24": "در حال دریافت...",
            "coin": "در حال دریافت...",
            "dollar": "در حال دریافت...",
            "ounce": "در حال دریافت..."
        }

    except Exception:
        return {
            "gold18": "نامشخص",
            "gold24": "نامشخص",
            "coin": "نامشخص",
            "dollar": "نامشخص",
            "ounce": "نامشخص"
        }
