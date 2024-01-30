from datetime import datetime


def find_current_date():
    print('Start data finder func')
    print(f'Current date: {datetime.now().strftime("%d:%m:%Y")}')
    print('Finish data finder func')
