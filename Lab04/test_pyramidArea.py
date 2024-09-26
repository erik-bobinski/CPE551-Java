# Author: Erik Bobinski
# Date: 9/24/2024
# Description: Test program that asserts the validity of 
# several imported functions form a separate file

import pytest
import pyramidArea as pa

@pytest.mark.xfail(reason="input should not be text")
def test_calcBaseArea():
    assert pa.calcBaseArea(15) == 225
    assert pa.calcBaseArea("15") # unceratain about this and the decorator

def test_calcSideArea():
    assert 270.41 <= pa.calcSideArea(15, 5) <= 270.42

    # round result to 2 decimal point precision
    assert round(pa.calcSideArea(10, 3), 2) == 270.42 

@pytest.mark.skip(reason="function only prints text")
def prntSurfArea():
    assert pa.prntSurfArea(15, 10)
