##Notice the output F means test is failed and green dot means that test cases is pass

##f you give command py.test then also it will execute the command


import pytest

def test_m1():
    a=3
    b=4
    assert a+1 ==b,'Test failed '
    assert a==b,'test failed if a ia not equal to b'

def test_m2():
    name='selenium'
    assert name.upper()=='SELENIUM'


def test_m3():
    assert True

def test_m4():
    assert False

def test_m4():
    assert 100==100

def test_m5():
    assert 'naveen'=='NAVEEN'