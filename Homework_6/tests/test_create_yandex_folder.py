from main import create_yandex_dick_folder


def test_shortest_longest_courses_1():
    """Test to check if a yandex_disk folder was created"""

    token = 'put you token to test'
    folder_name = 'Image'

    expected = 201

    actual = create_yandex_dick_folder(token, folder_name)
    assert expected == actual
