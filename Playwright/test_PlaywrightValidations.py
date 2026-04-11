
import pytest


@pytest.fixture
def prework():
    print("pre setup from the fixture")
    yield
    print("post setup from the fixture")


def test_initialcheck(prework):
    print("This is a test case from pytest")