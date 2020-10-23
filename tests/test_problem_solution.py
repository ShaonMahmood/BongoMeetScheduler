import pytest
from problem_solution import suggested_meeting_time


def example_allocated_meeting_data1():
    p1 = [
        ('08:00', '12:30'),
        ('14:00', '15:00'),
    ]

    p2 = [
        ('09:00', '12:00'),
        ('14:00', '15:30'),
    ]

    return ([p1, p2], "08:00", "17:00", 60)


def example_allocated_meeting_data2():
    p1 = [
        ('10:00', '12:30'),
        ('14:00', '15:00'),
    ]

    p2 = [
        ('09:00', '12:00'),
        ('14:00', '15:00'),
    ]

    p3 = [
        ('07:30', '09:50'),
        ('11:40', '12:40'),
        ('16:00', '17:00'),
    ]

    return ([p1, p2, p3], "08:00", "17:00", 60)


@pytest.mark.parametrize("unwanted_input", [(1,)])
def test_raises_exception_on_invalid_arguments(unwanted_input):
    with pytest.raises(TypeError):
        suggested_meeting_time(*unwanted_input)


@pytest.mark.parametrize("input_args, expected_result", [
    ( example_allocated_meeting_data1(), [('12:30', '14:00'), ('15:30', '17:00')] ),
    ( example_allocated_meeting_data2(), [('12:40', '14:00'), ('15:00', '16:00')] ),
])
def test_suggested_meeting_time(input_args, expected_result):
    assert suggested_meeting_time(*input_args) == expected_result