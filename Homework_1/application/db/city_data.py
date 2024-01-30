import pandas as pd


def create_city_data():
    print('Start create city_data')
    print('Информация о городах', end='\n\n')
    city = {'Город': ['Москва', 'Санкт-Петербург',
                      'Новосибирск', 'Екатеринбург'],
            'Год основания': [1147, 1703, 1893, 1723],
            'Население': [11.9, 4.9, 1.5, 1.4]}
    df = pd.DataFrame(city)
    print(df, end='\n\n')
    print('Finish create city_data')
