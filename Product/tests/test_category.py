import requests


class TestCategories:
    url_categories = "http://127.0.0.1:8000/bookstore/category/"

    def test_get_categories(self):
        response = requests.get(url=self.url_categories)
        assert response.status_code == 200