import pytest

@pytest.mark.SmokeTesting
def test_SmokeTesting():
    print("This is SmokeTesting ")

@pytest.mark.profile
def test_SalinityTesting():
    print("This is SalinityTesting")

def test_EndtoEndTesting():
    print("This is EndtoEndTesting")

def test_RegressionTesting():
    print("This is RegressionTesting")