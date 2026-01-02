from hello import hello

def test_hello():
    assert hello("Pragyan")=="Hello, Pragyan"  #== needs some return value in hello.py
    

def test_argument():
    assert hello() =="Hello, World"