
import pytest

@pytest.fixture(scope="session")
def fix_mainSessionfixure():
    print("this is fixture only to run once for a session")