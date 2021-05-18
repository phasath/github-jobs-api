from app.core.extensions import CONFIG


def test_liveness(client, parser):
    res = client.get("/api/health/liveness")
    st_code, response = parser(res)

    assert st_code == 200
    assert response["name"] == "Jobs4You"
    assert response["version"] == str(CONFIG.VERSION)
