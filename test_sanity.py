import pytest

#Customised markers
def test_regression():
    print("Happy to run for you")
    assert 4==4

def test_regression1():
    print("Not regression Happy to run for you1")
    assert 6==6

def test_regression123():
    print("Not regression Happy to run for you1")
    assert 6==6

## Inbuild markers
@pytest.mark.xfail
def test_regression12():
    print("Not regression Happy to run for you1")
    assert 4==6


# Registered markers (pytest.ini)
