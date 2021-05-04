
##if you use pytest.mark keyword then it will execute only that methods.
## command py.test Pytestsession /test_demo_3.py -m login
import pytest

@pytest.mark.login
def test_m1():
    a=3
    b=4
    assert a+1 ==b,'Test failed '
    assert a==b,'test failed if a ia not equal to b'

def test_m2():
    name='selenium'
    assert name.upper()=='SELENIUM'

@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert False

def test_m4():
    assert 100==100

@pytest.mark.login
def test_m5():
    assert 'naveen'=='NAVEEN'