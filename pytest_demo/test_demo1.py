import pytest


@pytest.mark.Smoke
def test_first_program(setup_fixture):
    a = 1
    print(f"a is {a}")
    assert a == 1


# This test will run 3 times, and each time it will print the browser wrapped in the setup_fixture format
def test_cross_browser(setup_fixture, cross_browser):
    # Printing only the first value of the tuple from the params from the fixture
    print(cross_browser[0])