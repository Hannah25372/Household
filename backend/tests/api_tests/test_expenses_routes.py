def test_get_expenses_returns_list(client):
    response = client.get("/api/expenses")
    assert response.status_code == 200