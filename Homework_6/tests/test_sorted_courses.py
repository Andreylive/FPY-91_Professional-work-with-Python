
import sys
sys.path.append('/Users/andrei/Desktop/Андрей/1. Образование/7. Fullstack разработчик (Нетология)/6. Профессиональна работа с Python/Домашняя работа для Git/Homework_6')

from main import sorted_corses

class TestSortedCorses:
    def test_unique_names_1(self):
        courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]

        mentors = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек"]
        ]

        durations = [14, 20, 12, 5]

        expected = ['Frontend-разработчик с нуля - 5 месяцев',
                    'Python-разработчик с нуля - 12 месяцев',
                    'Java-разработчик с нуля - 14 месяцев',
                    'Fullstack-разработчик на Python - 20 месяцев'
                    ]
        
        actual = sorted_corses(courses, mentors, durations)
        
        assert expected == actual


    def test_unique_names_2(self):
        courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]

        mentors = [
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек"]
        ]

        durations = [14, 20, 12, 20]

        expected = ['Python-разработчик с нуля - 12 месяцев',
                    'Java-разработчик с нуля - 14 месяцев',
                    'Fullstack-разработчик на Python - 20 месяцев',
                    'Frontend-разработчик с нуля - 20 месяцев'
                    ]
        
        actual = sorted_corses(courses, mentors, durations)
        
        assert expected == actual