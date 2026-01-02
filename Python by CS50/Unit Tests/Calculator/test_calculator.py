from calculator import square
import random
 
# def test():
#     a= random.randint(1,100)
#     assert square(a)==a*a
       

def test_positive():
    assert square (2)==4
    assert square (3)==9

def test_negative():
    assert square (-2)==4
    assert square (-3)==9

def test_zero():
    assert square (0)==0
