# Web UI Test Automation Framework

Автоматизированный фреймворк для тестирования графического интерфейса веб-приложений на основе Playwright и PyTest.

- **Playwright** — современная библиотека автоматизации браузера.
- **PyTest** — фреймворк для написания и выполнения тестов.
- **Page Object Model** — архитектурный паттерн для поддержки читаемости и переиспользования кода.
- **Python 3.9+**
- **Allure** - отчёты с шагами, скриншотами, графиками

## Установка

1. Клонировать репозиторий.
2. Создать виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   playwright install chromium firefox webkit

4. Настроить `.env` по образцу `.env.example`.

## Структура

├── .venv/                  ← виртуальное окружение
├── allure-reports/         ← готовые Allure отчёты
├── allure-results/         ← сырые данные Allure
├── reports/                ← скриншоты падений
├── tests/
│   ├── configs/            ← locators.conf
│   ├── pages/              ← Page Objects (Header и др.)
│   ├── utils/              ← Config, date, helpers
│   ├── conftest.py         ← фикстуры
│   ├── test_header.py      ← тесты
|── .env                
├── .gitignore
├── docker-compose.yaml
├── example.env
├── pytest.ini
├── README.md
├── requirements.txt
└── Taskfile.yaml

## Запуск тестов

1. Все тесты:
pytest

2. Запуск тестов с allure
pytest -v -s --alluredir allure-results/

3. Для генерации отчета:
task gen-report

## Отчёты

После выполнения генерируется HTML-отчёт в `allure-reports/index.html`.
открыть можно через http://localhost:5252