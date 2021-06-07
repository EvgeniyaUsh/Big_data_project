# Big Data

Необходимо написать консольную утилиту для многопоточной обработки данных, аккумулирования результатов через API из Интернета и их дальнейшего представления на графиках.

## Входные данные
Входные данные находятся в каталоге **/data** в данном репозитории в упакованном виде в файле **hotels.zip**.

Внутри данного архива расположено несколько файлов в формате _.CSV_, содержащих множество строк с информацией по отелям. В том числе, среди информации вы найдете:

- название отеля;
- широту и долготу отеля;
- страну и город, где расположен объект.

## Выходные данные
Все полученные результаты должны быть расположены в выходном каталоге со следующей структурой:

`{output_folder}\{country}\{city}\`

## Задание

Задание состоит из нескольких блоков и требований, которые перечислены ниже:

1. Приложение должно представлять собой консольную утилиту, которая принимает на вход следующие параметры:

    - путь к каталогу с входными данными;
    - путь к каталогу для выходных данных;
    - количество потоков для параллельной обработки данных;
    - возможно другие параметры, необходимые для функционирования приложения.
    
2. Первичная подготовка входных данных для использования:

    - распаковать архив с данными;
    - очистить данные от невалидных записей (содержащих заведомо ложные значения или отсутствующие необходимые элементы);
    - произвести группировку: для каждой страны выбрать город, содержащий максимальное количество отелей.
    
3. Обработка данных:
    
    - Обогатить данные по каждому из отелей в выбранных городах в **многопоточном режиме** его географическим адресом, полученным при помощи пакета **geopy**;
    - Вычислить географический центр области города, равноудаленный от крайних отелей. 
    - Для центра области при помощи стороннего сервиса (например, _openweathermap.org_) получить погодные данные:
    
        - исторические: за предыдущие 5 дней;
        - прогноз: на последующие 5 дней;
        - текущие значения.
    - Построить графики (например, при помощи пакета **matplotlib**), содержащие зависимости от дня:
    
        - минимальной температуры;
        - максимальной температуры.
    
4. Пост-процессинг:

    - Среди всех центров (городов) найти:
        
        - город и день наблюдения с максимальной температурой за рассматриваемый период;
        - город с максимальным изменением максимальной температуры;  
        - город и день наблюдения с минимальной температурой за рассматриваемый период;
        - город и день с максимальной разницей между максимальной и минимальной температурой.
    
5. Сохранение результатов:

    - В каталоге с указанной структурой для каждого города сохранить:
        
        - все полученные графики;
        - список отелей (название, адрес, широта, долгота) в формате CSV в файлах, содержащих не более 100 записей в каждом;
        - полученную информацию по центру в произвольном формате, удобном для последующего использования.
    
# Требования к проекту

Требования достаточно либеральные:
- Версия интерпретатора не ниже 3.7;
- Заполненные _requirements.txt_ или _poetry.toml_;
- Заполненный _.gitignore_;
- Выбор конечного инструментария для выполнения задания во многом остается за исполнителем, например:
  
   - argparser - для обработки параметров командной строки;
   - geopy - для получения адреса по координатам;
   - matplotlib - для построения графиков;
   - zipfile - для работы с архивам;
   - requests, urllib, aiohttp-клиент, etc - для осуществления запросов к внешнему API;
   - threading, multiprocessing, asyncio, etc - для "распараллеливания" задач;
   - pytest, unittest - для создания тестов;
   - pandas - для представления данных в виде дата-фреймов;
   - csv - для работы с CSV-файлами;
   - и многие другие - как из комплекта поставки python, так и сторонние пакеты.
- Ключевые фрагменты кода должны быть покрыты unit-тестами;
- Код должен быть оформлен в соответствии с рекомендациями PEP;
- Должна присутствовать документация, позволяющая незнакомому человеку начать использование приложения.
