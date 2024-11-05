import pytest





class TestProject:

    def test_001(self):
        print("test1")


    def test_002(self):
        print("test2")

    def test_003(self):
        print("test3")



if __name__ == '__main__':
    pytest.main(['test1'])