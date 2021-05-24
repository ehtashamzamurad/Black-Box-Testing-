import sys
import pytest
import loyalty

def test_invalid():
    points = -1
    result = loyalty.decideReward(points)
    assert result == 'invalid'

def test_norewardsmin():
    points = 0
    result = loyalty.decideReward(points)
    assert result == 'no rewards'

def test_norewardsmax():
    points = 349
    result = loyalty.decideReward(points)
    assert result == 'no rewards'

def test_coffeemin():
    points = 350
    result = loyalty.decideReward(points)
    assert result == 'coffee'

def test_coffeemax():
    points = 949
    result = loyalty.decideReward(points)
    assert result == 'coffee'

def test_cakemin():
    points = 950
    result = loyalty.decideReward(points)
    assert result == 'coffee and cake'

def test_cakemax():
    points = 2999
    result = loyalty.decideReward(points)
    assert result == 'coffee and cake'

def test_sandwichmin():
    points = 3000
    result = loyalty.decideReward(points)
    assert result == 'coffee, cake and sandwich'

def test_sandwichmax():
    points = 5000
    result = loyalty.decideReward(points)
    assert result == 'coffee, cake and sandwich'

def test_exceeds():
    points = 5001
    result = loyalty.decideReward(points)
    assert result == 'unable to earn > 5000'