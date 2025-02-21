from app import hello



def test_hello():
    assert hello() == 'Hello World!'
    assert hello("Rafał") == "Hello Rafał!"