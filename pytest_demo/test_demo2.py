import pytest


# Add a mark Smoke to the test to be ran only in Smoke suite
# @pytest.mark.Smoke
def test_first_program(setup_fixture):
    a = 4
    b = 6
    assert a + 2 == b, f"Addition doesn't match"


# Run a test that we know in advance will fail, without reporting it as failed
# @pytest.mark.xfail
def test_second_program(setup_fixture):
    msg = "Hello"
    assert not msg.casefold() == "Hi", f"Test failed because {msg} doesn't match to 'Hi'"


# @pytest.mark.skip
def test_third_program(setup_fixture):
    pass


def test_fixture_demo_0(setup_fixture):
    print("Steps of the test itself that will be executed after the fixture setup")
