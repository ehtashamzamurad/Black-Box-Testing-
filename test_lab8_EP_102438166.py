import sys
import pytest
import loyalty

def test_char():
    points = 'abc'
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_alphanum():
    points = 'ab12'
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_zero():
    points = 0
    result = loyalty.decideReward(points)
    assert result == 'no rewards'

def test_float():
    points = 349.5
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_special():
    points = '#$'
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_negative():
    points = -350
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_noReward():
    points = 300
    result = loyalty.decideReward(points)
    assert result == 'no rewards'


def test_coffee():
    points = 351
    result = loyalty.decideReward(points)
    assert result == 'coffee'

def test_reward2():
    points = 1000
    result = loyalty.decideReward(points)
    assert result == 'coffee and cake'

def test_reward3():
    points = 3512
    result = loyalty.decideReward(points)
    assert result == 'coffee, cake and sandwich'

def test_reward4():
    points = 5512
    result = loyalty.decideReward(points)
    assert result == 'unable to earn > 5000'
