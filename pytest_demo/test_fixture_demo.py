import pytest


@pytest.mark.usefixtures("setup_fixture")
class TestExamples:
    def test_fixture_demo_1(self):
        print("Steps of the test_fixture_demo_1 test that will be executed after the fixture setup")

    def test_fixture_demo_2(self):
        print("Steps of the test_fixture_demo_2 test that will be executed after the fixture setup")

    def test_fixture_demo_3(self):
        print("Steps of the test_fixture_demo_3 test that will be executed after the fixture setup")

    def test_fixture_demo_4(self):
        print("Steps of the test_fixture_demo_4 test that will be executed after the fixture setup")