import pytest
import day_01


@pytest.mark.parametrize("test_input, expected_result", [(12,2), (14,2), (1969, 654), (100756, 33583)])
def test_fuel_calculation(test_input, expected_result):
    assert day_01.fuel_calculator(test_input) == expected_result
    
@pytest.mark.parametrize("test_input, expected_result", [(14, 2), (1969, 966), (100756, 50346)])
def test_fuel_calculator_inc_fuel(test_input, expected_result):
    assert day_01.fuel_calculator_inc_fuel(test_input) == expected_result


if __name__ == '__main__':
    pytest.main()
    



# Run tests from terminal:
#  python -m pytest test_day_01_pytest.py 