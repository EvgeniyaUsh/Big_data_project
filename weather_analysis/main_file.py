import click as click
from app.temperatures import get_temperature
from app.geo_py import get_geo
from app.plotting import build_a_graph_with_max_temperature, build_a_graph_with_min_temperature
from app.post_processing import get_day_and_city_with_max_temperature, get_day_and_city_with_min_temperature, \
    get_city_with_max_change_in_max_temperature, get_day_and_city_with_max_difference_between_max_min_temp
from app.saving_to_csv_format import get_dataframe_with_address_and_write_csv
from app.data_preparation import unpack_zip, create_dataframe_from_csv_files, clearing_data
from app.data_processing import get_centre_coordinates, get_list_with_coordinates, get_cities_with_max_numbers_of_hotel


@click.command()
@click.argument('input_path')  # data/hotels.zip
@click.argument('output_path')  # путь для сохранения полученных результатов
@click.argument('max_workers')
@click.argument('api_key_weather')  # API ключ с сайта  https://openweathermap.org/appid
@click.argument('api_key_geo')  # API ключ с сайта https://developer.mapquest.com/
def main(input_path, output_path, max_workers, api_key_weather, api_key_geo):
    """
    Утилита предназначена для многопоточной обработки данных,
    аккумулирования результатов через API из Интернета и их дальнейшего представления на графиках.
    Утилита принимает на вход входные и выходные каталоги, число потоков для многопоточной обработки
    и 2 API-ключа.
    Все полученные результаты будут располагаться в выходном каталоге со следующей структурой
    output_folder/country/city/
    Пример использования:
    C:/data/input_folder C:/data/output_folder Кол-во_потоков Ваш_API-OpenWeatherMap Ваш_API-OpenMapQuest
    Для использования приложения Вам необходимы 2 API-ключа.
    1й-для работы с OpenWeatherMap. Вы можете зарегистрировать бесплатный
    аккаунт на https://openweathermap.org/appid.
    2й-для работы с OpenMapQuest. Вы можете зарегистрировать бесплатный
    аккаунт на https://developer.mapquest.com/
    """
    unpack_zip(input_path)
    df = create_dataframe_from_csv_files('csv_files_for_work')
    print('Файлы распакованы')
    df = clearing_data(df)
    df = get_cities_with_max_numbers_of_hotel(df)
    list_with_coordinates = get_list_with_coordinates(df)

    df_with_lon_lat_address = get_geo(list_with_coordinates, api_key_geo, int(max_workers))
    get_dataframe_with_address_and_write_csv(df, df_with_lon_lat_address, output_path)
    print('Адреса получены')

    dict_with_centre_of_coordinates = get_centre_coordinates(df)
    min_temperature, max_temperature = get_temperature(dict_with_centre_of_coordinates, api_key_weather)
    print('Температуры для каждого дня получены')

    build_a_graph_with_min_temperature(min_temperature, output_path)
    build_a_graph_with_max_temperature(max_temperature, output_path)
    print('Графики построены и сохранены')

    get_day_and_city_with_max_temperature(max_temperature, output_path)
    get_city_with_max_change_in_max_temperature(max_temperature, output_path)
    get_day_and_city_with_min_temperature(min_temperature, output_path)
    get_day_and_city_with_max_difference_between_max_min_temp(max_temperature, min_temperature, output_path)

    print(f"Утилита отработала успешно. Данные сохранены в {output_path}/")


if __name__ == '__main__':
    main()
