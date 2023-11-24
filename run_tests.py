import pytest
import main

if __name__ == '__main__':
     pytest.main(['-x', 'tests', '--capture', 'sys', '--verbose'])