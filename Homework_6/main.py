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
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
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
            sorted_courses.append(f'{courses_list[element]["title"]} - {duration} месяцев')

    return sorted_courses
