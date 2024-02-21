import sys
sys.path.append('/Users/andrei/Desktop/Андрей/1. Образование/7. Fullstack разработчик (Нетология)/6. Профессиональна работа с Python/Домашняя работа для Git/Homework_6')
from main import sorted_corses

def test_sorted_courses_1(data_prep_1):
    courses, mentors, durations, expected = data_prep_1
    actual = sorted_corses(courses, mentors, durations) 
    assert expected == actual


def test_sorted_courses_2(data_prep_2):
    courses, mentors, durations, expected = data_prep_2
    actual = sorted_corses(courses, mentors, durations) 
    assert expected == actual
