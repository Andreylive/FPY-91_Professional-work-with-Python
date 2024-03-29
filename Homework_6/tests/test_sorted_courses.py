from main import sorted_corses


def test_sorted_courses_1(data_prep_1):
    """Test to check courses with the different durations"""
    courses, mentors, durations, expected = data_prep_1
    actual = sorted_corses(courses, mentors, durations)
    assert expected == actual


def test_sorted_courses_2(data_prep_2):
    """Test to check courses with the same durations"""
    courses, mentors, durations, expected = data_prep_2
    actual = sorted_corses(courses, mentors, durations)
    assert expected == actual
