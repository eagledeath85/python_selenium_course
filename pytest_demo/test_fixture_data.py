import pytest
from pytest_demo.log_class import LogClass



@pytest.mark.usefixtures("data_load")
class TestExample2(LogClass):

    # Passing the fixture name to the test is mandatory because we want to return the fixture data to the test
    def test_edit_profile(self, data_load):
        # Print whatever the data_load fixture returns to test_edit_profile
        log = self.get_logger()
        log.info(data_load[0])
        log.info(data_load[2])
        print(data_load[1])
