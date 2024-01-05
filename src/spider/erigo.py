from typing import Any
from httpx import Client

class ErigoScrap(object):
    def __init__(self, search_query) -> None:
        self.search_query = search_query
        self.eri_url: str = "https://erigostore.co.id/"
        self.client = Client()  # Corrected the case
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    def get_pages(self):
        params: dict[str, Any] = {
            "q": self.search_query,
        }

        headers: dict[str, Any] = self.user_agent.copy()  # Correct way to copy headers

        # Request to website
        response = self.client.get(self.eri_url, params=params, headers=headers)  # Corrected the URL variable

        # Handle response (Example)
        if response.status_code == 200:
            return response.text
        else:
            return None


        
