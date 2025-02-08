import app

def test_home():
    response = app.home()
    assert response == "Hello, DevOps!"
