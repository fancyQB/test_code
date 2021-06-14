import pytest

class Test_Case:
    def setup_class(self):
        print('---------------------> setup method')

    def teardown_class(self):
        print('----------------------> teardown method')

    def test_1(self):
        print('----------------------> test_1 method')
        assert 1

    def test_2(self):
        print('----------------------> test_2 method')
        assert 0

if __name__ == '__main__':
    # pytest.main(["-s", 'test-py.py'])
    pytest.main('-s test-py.py')