import sys
sys.path.append('/Users/andrei/Desktop/Андрей/1. Образование/7. Fullstack разработчик (Нетология)/6. Профессиональна работа с Python/Домашняя работа для Git/Homework_6')

from main import unique_names

def test_unique_names():
    mentors = [
	["Евгений Шмаргунов", "Олег Булыгин"],
	["Филипп Воронов", "Анна Юшина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин"]
    ]

    expected = 'Александр, Анна, Евгений, Олег, Филипп'
    actual = unique_names(mentors)
    
    assert expected == actual