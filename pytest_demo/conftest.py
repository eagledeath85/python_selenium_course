import pytest


@pytest.fixture(scope="class")
def setup_fixture():
    print("Code to run as a pre-requisite")
    print("----------------------------------------")
    yield
    print("----------------------------------------")
    print("Code to run after the test")


@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["John", "Doe", "rahulshettyacademy.com"]


# The values in the params argument are sent to the request instance
@pytest.fixture(params=[("Chrome", "John"), "Firefox", "IE"])
def cross_browser(request):
    # Return the value of each from params
    return request.param