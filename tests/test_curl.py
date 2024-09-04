from src.fishmlserv.curl import get

def test_get():
    fish = get(20, 150)
    assert fish=="빙어"
