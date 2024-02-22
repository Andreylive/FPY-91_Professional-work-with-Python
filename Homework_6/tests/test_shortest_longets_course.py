from main import shortest_longest_courses


def test_shortest_longest_courses_1():
    """Test to check courses with the same durations"""
    courses = ["Java-разработчик с нуля",
               "Fullstack-разработчик на Python",
               "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]

    durations = [14, 20, 12, 20]

    expected = (['Python-разработчик с нуля'],
                ['Fullstack-разработчик на Python',
                 'Frontend-разработчик с нуля'])

    actual = shortest_longest_courses(courses, durations)
    assert expected == actual


def test_shortest_longest_courses_2():
    """Test to check courses with the different durations"""
    courses = ["Java-разработчик с нуля",
               "Fullstack-разработчик на Python",
               "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"
               ]

    durations = [14, 120, 12, 20]

    expected = (['Python-разработчик с нуля'],
                ['Fullstack-разработчик на Python']
                )

    actual = shortest_longest_courses(courses, durations)
    assert expected == actual
