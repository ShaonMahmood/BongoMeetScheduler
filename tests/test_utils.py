import pytest
from utils import stringToMinute, minuteToString


@pytest.mark.parametrize("unwanted_builtin_input", [3, []])
def test_raises_exception_on_builtin_arguments(unwanted_builtin_input):
    with pytest.raises(TypeError):
        stringToMinute(unwanted_builtin_input)



@pytest.mark.parametrize("input_string, expected_result", [
    (
        "13:00",
        780
    ),
    (
        "00:00",
        0
    ),
])
def test_time_string_to_minute_function(input_string, expected_result):
    actual_result = stringToMinute(input_string)
    assert actual_result == expected_result


@pytest.mark.parametrize("input_minute, expected_result", [
    (
        780,
        "13:00"
    ),
    (
        0,
        "00:00"
    ),
])
def test_minute_to_time_slot_function(input_minute, expected_result):
    actual_result = minuteToString(input_minute)
    assert actual_result == expected_result
