import pytest
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("dataload")
class Testdata(BaseClass):

    def test_dataload(self, dataload):
        log=self.getlogger()
        print(dataload[1])
        log.info(dataload[1])