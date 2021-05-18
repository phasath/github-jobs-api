from base64 import b64encode


def test_get_admin_unauthorized(client, parser):
    res = client.get("/api/admin", follow_redirects=True)

    assert res.status_code == 401


def test_get_admin_with_credentials(client, parser):
    valid_credentials = b64encode(b"test:test").decode("utf-8")

    res = client.get(
        "/api/admin",
        headers={"Authorization": f"Basic {valid_credentials}"},
        follow_redirects=True,
    )

    assert res.status_code == 200
