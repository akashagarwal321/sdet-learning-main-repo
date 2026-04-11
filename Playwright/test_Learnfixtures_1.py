import pytest


@pytest.fixture
#@pytest.fixture(scope="module")


def fix_test(fix_mainSessionfixure):
    print("This is a fixture")


def test_firsttest(fix_test):
    print("This is the first test case")

def test_secondtest(fix_test):
    print("This is the second test case")

def test_thirdtest(fix_test):
    print("This is the third test case")