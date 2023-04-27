import pytest
from conftest import client

# TODO: check the order of tests execusion, because download_file should be called after sendbook
@pytest.mark.run(after='test_sendbook')
def test_vocabulary_download():
    print("TODO:")
    assert True == True
