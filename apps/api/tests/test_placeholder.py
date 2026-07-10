from fastapi.testclient import TestClient

from app.main import CORS_ALLOW_HEADERS, CORS_ALLOW_METHODS, app, create_app


def test_app_exists():
    assert app is not None
    assert app.title == "GrantMatch API"


def test_create_app():
    instance = create_app()
    assert instance.title == "GrantMatch API"


def test_cors_preflight_uses_explicit_methods_and_headers():
    client = TestClient(app)
    response = client.options(
        "/docs",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type,authorization",
        },
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"
    allowed_methods = response.headers.get("access-control-allow-methods", "")
    for method in ("GET", "POST", "OPTIONS"):
        assert method in allowed_methods
    assert "*" not in allowed_methods
    allowed_headers = response.headers.get("access-control-allow-headers", "").lower()
    assert "content-type" in allowed_headers
    assert "authorization" in allowed_headers
    assert "*" not in allowed_headers


def test_cors_constants_are_explicit_lists():
    assert "*" not in CORS_ALLOW_METHODS
    assert "*" not in CORS_ALLOW_HEADERS
    assert "POST" in CORS_ALLOW_METHODS
    assert "Content-Type" in CORS_ALLOW_HEADERS
