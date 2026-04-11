import pytest



@pytest.fixture(scope="class")
def fix_test(fix_mainSessionfixure):
    print("This is a fixture")



class Test_learnfixtures:

    def test_classfirsttest(self,fix_test):
        print("This is the class first test case")

    def test_classsecondtest(self,fix_test):
        print("This is the class second test case")

    def test_classthirdtest(self,fix_test):
        print("This is the class third test case")