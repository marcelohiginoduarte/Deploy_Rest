import requests


class TestProducts:
    url_products = "http://127.0.0.1:8000/bookstore/product/"

    def test_get_products(self):
        response = requests.get(url=self.url_products)
        assert response.status_code == 200


    def test_post_product(self):
        novo = {
            "title": "O Senhor dos Aneis",
            "description": "Um hobbit que tem a missao de destruir o Anel do Poder, para salvar seu mundo da destruicao",
            "price": 45,
            "active": True,
            "categories_id": [],
        }

        response = requests.post(url=self.url_products, data=novo)
        assert response.status_code == 201
        assert response.json()["title"] == novo["title"]


    def test_get_product(self):
        response = requests.get(url=f"{self.url_products}1")
        assert response.status_code == 200
