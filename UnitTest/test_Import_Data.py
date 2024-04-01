import pytest
from Scripts import Import_Data

def test_clean_data():
    assert Import_Data.clean_data(Import_Data.import_data('UnitTest\\data_test.csv')) == [{'Date': 20231028230000, 'kWh': 0.15}, {'Date': 20231028233000, 'kWh': 0.159}, {'Date': 20231029000000, 'kWh': 1.177}, {'Date': 20231029003000, 'kWh': 0.151}, {'Date': 20231029010000, 'kWh': 3.139}, {'Date': 20231029013000, 'kWh': 0.151}]


