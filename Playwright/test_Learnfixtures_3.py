import pytest



@pytest.fixture(scope="module")
def fix_test(fix_mainSessionfixure):
    print("This is a fixture")



def test_modulefirsttest(fix_test):
    print("This is the module first test case")

def test_modulesecondtest(fix_test):
    print("This is the module second test case")

def test_modulethirdtest(fix_test):
    print("This is the module third test case")