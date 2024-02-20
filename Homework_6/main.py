def unique_names(mentors: list) -> str:

    all_names = []

    [all_names.extend(m) for m in mentors]
    only_names = set()

    for name in all_names:
        only_names.add(name.split(' ')[0])

    only_names = sorted(list(only_names))
    only_names = ', '.join(only_names)

    return only_names
