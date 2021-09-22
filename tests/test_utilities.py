from utilities import CpiData
import pytest

cpi_data = CpiData()

# Ensures that attributes of CpiData class exists
@pytest.mark.parametrize("cpi_data_attributes, unexpected_result", [
    (cpi_data.cpi, None),
    (cpi_data.countries, None)
])
def test_dow_dog_attributes(cpi_data_attributes, unexpected_result):
    assert cpi_data_attributes != unexpected_result

# Ensures that get_cpi_all method works correctly
def test_cpi_all():
    data = cpi_data.get_cpi_all('ticker=CPICN')
    result = 'BELOW ITS 12-MONTH AVERAGE INDICATING DEFLATION'
    assert result in data

# Ensures that get_cpi method works correctly
def test_cpi():
    cpi_data.get_cpi('ticker=CPICN')
    result = ['DEFLATION', 'CHINA']
    assert result in cpi_data.cpi

# Ensures that get_cpi_g5 method works correctly
def test_cpi_g5():
    cpi_data.get_cpi_g5()
    result = [['DEFLATION', 'CHINA'], ['INFLATION', 'GERMANY'], ['INFLATION', 'INDIA'], ['INFLATION', 'JAPAN'], ['INFLATION', 'UNITED STATES']]
    assert result == cpi_data.cpi