from app.main import app, create_app


def test_app_exists():
    assert app is not None
    assert app.title == "GrantMatch API"


def test_create_app():
    instance = create_app()
    assert instance.title == "GrantMatch API"
