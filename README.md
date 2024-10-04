# Bank Operations Widget

## Описание проекта

Этот проект представляет собой виджет банковских операций клиента. В рамках проекта реализованы функции для обработки данных банковских операций, такие как фильтрация по состоянию и сортировка по дате.

## Установка

1. Склонируйте репозиторий: https://github.com/andranikavdzhiyan/Course_work_3.git
   


 ##  Структура проекта

Вот обзор структуры проекта:

```plaintext
Course_work/
│
├── .env_template           # Шаблон файла переменных окружения
├── .flake8                 # Конфигурация для проверки стиля кода
├── .gitignore              # Правила игнорирования файлов Git
├── READMY.md               # Документация проекта (этот файл)
├── poetry.lock             # Файл блокировки зависимостей Poetry
├── pyproject.toml          # Конфигурационный файл проекта для Poetry
├── requirments.txt         # Зависимости для установки через pip
├── user_settings.json      # Пользовательские настройки и конфигурации
│
├── data/                   # Данные проекта
│   └── operations.xlsx     # Excel-файл с данными транзакций
│    
│
├── src/                    # Исходный код приложения
│   ├── __init__.py         # Помечает src как пакет
│   ├── logger.py           # Логирование файлов
│   ├── reports.py          # Логика генерации отчетов
│   ├── services.py         # Основная бизнес-логика
│   ├── utils.py            # Вспомогательные функции
│   ├── views.py            # Логика взаимодействия с пользователем
│   └── main.py             # Точка входа в приложение
│
└── tests/                  # Модульные тесты
    ├── __init__.py         # Помечает tests как пакет
    ├── test_logger.py      # Тесты для генерации отчетов
    ├── test_reports.py     # Тесты для основной логики
    ├── test_services.py    # Тесты для основной логики
    ├── test_utils.py       # Тесты для основной логики
    └── test_views.py       # Тесты для вспомогательных функций
    
```
## Покрытие тестами

```
============================ test session starts ============================
platform win32 -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Andrey\PycharmProjects\my_prj\Course_work_3
configfile: pyproject.toml
plugins: cov-5.0.0
collected 14 items                                                                                                                                                                         

tests\test_logger.py .                                         [  7%]
tests\test_reports.py .                                        [ 14%]
tests\test_services.py ...                                     [ 35%]
tests\test_utils.py .                                          [ 42%]
tests\test_views.py ........                                   [100%]

---------- coverage: platform win32, python 3.12.4-final-0 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
src\__init__.py              0      0   100%
src\logger.py               17      0   100%
src\reports.py              28      0   100%
src\services.py             15      0   100%
src\utils.py                16      3    81%
src\views.py                50     13    74%
tests\__init__.py            0      0   100%
tests\test_logger.py        18      0   100%
tests\test_reports.py       27      0   100%
tests\test_services.py      18      0   100%
tests\test_utils.py         12      0   100%
tests\test_views.py         24      0   100%
--------------------------------------------
TOTAL                      225     16    93%


============================ 14 passed in 6.69s ============================
```

 
###  Запуск тестов

#### Для запуска тестов и проверки работоспособности:
Копировать код ```pytest tests/```

#### Этот проект лицензирован по лицензии MIT. ☺