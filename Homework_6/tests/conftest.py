import pytest

@pytest.fixture
def data_prep_1():
    from data_for_tests import courses_1, mentors_1, durations_1, expected_1
    return courses_1, mentors_1, durations_1, expected_1


@pytest.fixture
def data_prep_2():
    from data_for_tests import courses_2, mentors_2, durations_2, expected_2
    return courses_2, mentors_2, durations_2, expected_2
