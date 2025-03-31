
# Python Basic Diploma — Telegram Bot

## 📜 Описание

**Python Basic Diploma** — это Telegram-бот, который помогает пользователям искать фильмы по различным критериям, таким как жанр, рейтинг и бюджет. Бот использует **Kinopoisk API** для поиска фильмов и предоставляет возможность фильтровать результаты.

## 🔧 Функциональность

- **Поиск фильмов**: Бот позволяет искать фильмы по ключевым словам.
- **Фильтры**: Пользователи могут фильтровать фильмы по жанру, рейтингу и бюджету.
- **Пагинация**: Результаты поиска выводятся с пагинацией для удобства пользователя.
- **Избранное**: Пользователи могут добавлять фильмы в избранное и удалять их оттуда.

## 🛠 Технологии

- **Python**: Основной язык программирования.
- **pyTelegramBotAPI**: Библиотека для создания Telegram-бота.
- **Kinopoisk API**: API для получения информации о фильмах.
- **SQLite**: База данных для хранения информации о пользователях и их избранных фильмах.

## 📦 Установка и запуск

### 1. Клонируйте репозиторий:

```bash
git clone https://gitlab.skillbox.ru/sergei_rusakovich/python_basic_diploma.git
```

### 2. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. Настройте переменные окружения:

Создайте файл `.env` и добавьте токен бота и ключ API Kinopoisk:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
KINOPOISK_API_KEY=YOUR_KINOPOISK_API_KEY
```

### 4. Запустите бота:

```bash
python main.py
```

## 🧑‍💻 Примеры использования

- **Поиск фильмов**: Напишите `/search` и введите название фильма.
- **Фильтры**: Используйте кнопки для выбора жанра, рейтинга или бюджета.
- **Избранное**: Добавьте фильм в избранное, нажав на соответствующую кнопку.

## ⚠️ Примечания

- **Безопасность**: Токен бота и ключ API Kinopoisk должны храниться в секрете.
- **API-ключи**: Обновляйте ключи API регулярно для безопасности.

## 📫 Контакты

Если у вас есть вопросы или предложения, вы можете связаться со мной через **Telegram**: [ваш Telegram-никнейм].
