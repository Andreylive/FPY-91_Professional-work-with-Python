def unique_names(mentors: list) -> str:
    all_names = []

    [all_names.extend(m) for m in mentors]
    only_names = set()

    for name in all_names:
        only_names.add(name.split(' ')[0])

    only_names = sorted(list(only_names))
    only_names = ', '.join(only_names)

    return only_names


def sorted_corses(courses: list, mentors: list, durations: list) -> list:
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course,
                       "mentors": mentor,
                       "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    sorted_courses = []

    for duration, id in durations_dict.items():
        for element in id:
            sorted_courses.append(
                f'{courses_list[element]["title"]} - {duration} месяцев'
                )

    return sorted_courses


def shortest_longest_courses(courses: list, durations: list) -> list:
    courses_list = []

    for title, duration in zip(courses, durations):
        course_dict = {
            "title": title,
            "duration": duration
            }
        courses_list.append(course_dict)

    min_number = min(durations)
    max_number = max(durations)

    maxes = []
    minis = []

    for i, duration in enumerate(durations):
        if duration == min_number:
            minis.append(i)
        elif duration == max_number:
            maxes.append(i)

    courses_min = []
    courses_max = []

    for id in minis:
        courses_min.append(courses_list[id].get('title'))

    for id in maxes:
        courses_max.append(courses_list[id].get('title'))

    return courses_min, courses_max
