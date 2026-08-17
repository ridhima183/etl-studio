def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"

def test_get_customers(client):
    response = client.get("/customers")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_customer(client):
    response = client.get("/customers/101")
    assert response.status_code == 200

def test_customer_not_found(client):
    assert client.get("/customers/99999").status_code == 404

def test_city_filter(client):
    response = client.get("/customers?city=Hyderabad")
    assert response.status_code == 200
    assert all(c["city"] == "Hyderabad" for c in response.get_json())
