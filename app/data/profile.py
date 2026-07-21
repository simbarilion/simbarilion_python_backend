"""Данные профиля — редактируйте этот файл для обновления контента сайта."""

PROFILE = {
    "name": "Надежда",
    "full_name": "Попова Надежда",
    "title": "Python Backend Developer",
    "tagline": "REST API, бизнес-логика и надёжные backend-системы",
    "hero_description": (
        "Разрабатываю REST API и бизнес-логику на Django и FastAPI, проектирую модели данных, "
        "интеграции с внешними сервисами и фоновые процессы. "
        "Имею опыт коммерческой разработки и собственных проектов."
    ),
    "hero_stats": [
        {"value": "Python", "label": "основной язык"},
        {"value": "Django / DRF", "label": "веб-стек"},
        {"value": "FastAPI", "label": "API-фреймворк"},
        {"value": "PostgreSQL", "label": "СУБД"},
    ],
    "about": {
        "role": "Python Backend Developer",
        "avatar": "/static/images/avatar.png",
        "facts": [
            {"label": "Город", "value": "Барнаул"},
            {"label": "Формат", "value": "Удалённо"},
            {"label": "Образование", "value": "Высшее + SkyPro"},
            {
                "label": "Почта",
                "value": "nadezhdapopova13@yandex.ru",
                "link": "mailto:nadezhdapopova13@yandex.ru",
            },
            {
                "label": "Telegram",
                "value": "@simbarilion",
                "link": "https://t.me/simbarilion",
            },
            {
                "label": "GitHub",
                "value": "@simbarilion",
                "link": "https://github.com/simbarilion",
            },
        ],
        "bio": [
            (
                "Python Backend-разработчик (Django / FastAPI): REST API, бизнес-логика, интеграции с внешними сервисами и фоновые процессы."
            ),
            (
                "Работаю с PostgreSQL, Celery, Redis, Docker, Git. Есть опыт разработки fullstack-приложений и ETL-пайплайнов."
            ),
            (
                "Использую AI-инструменты (Cursor, GitHub Copilot и ChatGPT) как часть рабочего процесса: "
                "для ускорения разработки и исследования, с обязательной проверкой и доработкой решений."
            ),
            (
                "Сейчас — коммерческий проект в ООО «Экосистема Альфа»: платформа автоматизации курьерской доставки. "
            ),
            (
                "Параллельно веду собственные и клиентские проекты полного цикла — от проектирования API до production."
            ),
        ],
    },
    "skill_groups": [
        {
            "title": "Backend & API",
            "note": "Основной стек коммерческих и собственных проектов",
            "skills": [
                "Python",
                "Django",
                "Django REST Framework",
                "FastAPI",
                "Flask",
                "REST API",
                "Pydantic",
            ],
        },
        {
            "title": "Данные и фоновые процессы",
            "note": "Хранение, кэш, очереди и отложенные задачи",
            "skills": [
                "PostgreSQL",
                "SQLite",
                "Redis",
                "Celery",
                "APScheduler",
                "Apache Airflow",
            ],
        },
        {
            "title": "Интеграции",
            "note": "Внешние API, боты и HTTP-клиенты",
            "skills": [
                "Telegram Bot API",
                "aiogram",
                "httpx",
                "requests",
                "Wildberries API",
                "Beautiful Soup",
            ],
        },
        {
            "title": "Инфраструктура и качество",
            "note": "Деплой, CI/CD, тесты, сопровождение",
            "skills": [
                "Docker",
                "Docker Compose",
                "Nginx",
                "Gunicorn",
                "Git",
                "GitHub Actions",
                "Pytest",
                "Linux / Bash",
            ],
        },
        {
            "title": "Frontend (supporting)",
            "note": "Для fullstack и демо-интерфейсов",
            "skills": [
                "HTML / CSS",
                "JavaScript / AJAX",
                "Jinja2",
            ],
        },
        {
            "title": "AI-инструменты",
            "note": "Ускорение разработки, рефакторинга и разбора сложных задач",
            "skills": [
                "Cursor",
                "GitHub Copilot",
                "ChatGPT",
            ],
        },
    ],
    "education": [
        {
            "degree": "Backend-разработчик (Python)",
            "period": "2026",
            "institution": "SkyPro — профессиональная переподготовка",
            "description": (
                "Профессиональная переподготовка по дополнительной профессиональной программе 'Python-разработчик'."
            ),
        },
        {
            "degree": "Разработка на FastAPI",
            "period": "2026",
            "institution": "SkyPro",
            "description": "Углублённый курс по разработке API на FastAPI.",
        },
        {
            "degree": "Основы генеративного ИИ",
            "period": "2026",
            "institution": "SkyPro",
            "description": "Образовательный модуль по применению генеративного ИИ в разработке.",
        },
        {
            "degree": "PG BootCamp Russia 2026",
            "period": "2026",
            "institution": "Сертификат участника",
            "description": "Участие в конференции по PostgreSQL (г. Москва).",
        },
    ],
    "experience": [
        {
            "title": "Python Backend Developer",
            "period": "Апрель 2026 — настоящее время",
            "company": 'ООО «Экосистема Альфа», Москва (удалённо)',
            "stack": (
                "Python, Django, DRF, PostgreSQL, JWT, Redis, Celery, "
                "Telegram API, Nginx, Git, Docker"
            ),
            "bullets": [
                (
                    "Развиваю backend платформы автоматизации курьерской доставки: REST API, бизнес-логика заказов, сопровождение production"
                ),
                (
                    "Переработала подсистему геолокации курьеров: модели координат, API и обновление местоположения"
                ),
                (
                    "Доработала жизненный цикл заказа: старт доставки и причины отмены — прозрачные статусы для клиентов и операций"
                ),
                (
                    "Улучшила регистрацию/email-активацию; стабилизировала Celery на production"
                ),
                (
                    "Согласовываю API с frontend, участвую в code review и командной разработке в Git"
                ),
            ],
        },
        {
            "title": "Backend-разработчик (Python)",
            "period": "Март 2025 — настоящее время",
            "company": "Freelance & собственные проекты",
            "stack": (
                "Django/DRF, FastAPI, PostgreSQL, SQLite, Redis, Celery, "
                "aiogram, requests, httpx, Apache Airflow, pytest, Sentry, "
                "Docker, Nginx, GitHub Actions, HTML, CSS, JavaScript"
            ),
            "bullets": [
                (
                    "Коммерческие задачи: боты (бот лимитов Wildberries), фиды (YML-фид для магазина чая), API, автоматизация рутины селлеров и магазинов"
                ),
                (
                    "Собственные проекты полного цикла — от API и БД до CI/CD и VPS"
                ),
                (
                    "Интеграции: маркетплейсы, Telegram, рекламные фиды; фоновые задачи и планировщики"
                )
            ],
        },
    ],
    "projects": [
        {
            "title": "FilmDiary",
            "description": (
                "Fullstack-платформа персональных рекомендаций фильмов. REST API (20+ эндпоинтов), "
                "RBAC, рекомендательная система, Telegram-интеграция, фоновые Celery-задачи, frontend на JS. "
                "Адрес сервера с развернутым приложением: "
                '<a href="https://filmdiary.creepysnakes.su/" target="_blank" rel="noopener">'
                "https://filmdiary.creepysnakes.su/</a>"
            ),
            "tags": ["Django", "DRF", "PostgreSQL", "Celery", "Redis", "JavaScript", "pytest", "Docker", "CI/CD"],
            "categories": ["fullstack"],
            "github": "https://github.com/simbarilion/FilmDiary",
            "demo": None,
            "featured": True,
            "video_url": "https://rutube.ru/video/private/a11f5ac10ad0f569cdc9c8180dff018a/?p=1Li0EXLN8iab7NYugpTieQ",
            "readme_url": "/static/projects/film-diary-overview.html",
        },
        {
            "title": "WB Limits Tracker",
            "description": (
                "Проблема. Селлеру нужно вовремя занимать слоты приёмки Wildberries — ручной мониторинг отнимает время и легко пропустить окно. "
                "Решение. Telegram-бот с интеграцией WB API: уведомляет о доступных лимитах и хранит API-ключи в зашифрованном виде. "
                "Результат. Автоматический контроль складов. Demo-режим и видеообзор без открытого кода."
            ),
            "tags": ["Python", "aiogram", "Flask", "httpx", "Pydantic", "SQLite", "pytest", "Telegram Bot API", "Wildberries API"],
            "categories": ["commercial", "integrations"],
            "github": None,
            "demo": None,
            "video_url": "https://rutube.ru/video/private/776c4e67778a2873b56f7195b9a60e10/?p=GLPCzLMA0pX8zV9LRdHeKg",
            "readme_url": "/static/projects/wb-limits-tracker-readme.html",
        },
        {
            "title": "Oh! my tea — YML Feed",
            "description": (
                "Проблема. Для рекламы нужен валидный YML. В CMS содержатся скрытые и неполные позиции без единого формата; ручная проверка перед выгрузкой даёт ошибки модерации. "
                "Решение. Сервис валидирует товары по бизнес-правилам, отсеивает ошибки и собирает XML с отчётом об отсеянных позициях. "
                "Результат. Фид без ручной проверки перед каждой выгрузкой. Интерактивное демо показывает работу конвейера на тестовых данных."
            ),
            "tags": ["Python", "XML", "pytest", "JavaScript"],
            "categories": ["commercial", "integrations"],
            "github": "https://github.com/simbarilion/Oh-my-tea-demo",
            "demo": "https://simbarilion.github.io/Oh-my-tea-demo/",
            "readme_url": "/static/projects/oh-my-tea-overview.html",
        },
        {
            "title": "Habr Career Vacancy ETL",
            "description": (
                "ETL-пайплайн на Apache Airflow для автоматического сбора вакансий Habr Career, "
                "обработки данных, загрузки в PostgreSQL и уведомлений в Telegram."
            ),
            "tags": ["Python", "Apache Airflow", "PostgreSQL", "BeautifulSoup", "httpx", "Telegram Bot API", "Docker"],
            "categories": ["etl"],
            "github": "https://github.com/simbarilion/HH_Vacancy_etl_airflow",
            "demo": None,
            "readme_url": "/static/projects/habr-career-etl-overview.html",
        },
        {
            "title": "GitHub Analytics",
            "description": (
                "FastAPI-сервис поиска популярных GitHub-репозиториев с аналитикой: "
                "асинхронный сбор данных, агрегация метрик, экспорт JSON/CSV и интеграция с Google Sheets Dashboard"
            ),
            "tags": ["FastAPI", "httpx", "Docker", "Google Sheets", "Pydantic"],
            "categories": ["etl"],
            "github": "https://github.com/simbarilion/PythonIdeasFromGitHub",
            "demo": None,
            "readme_url": "/static/projects/github-analytics-overview.html",
        },
        {
            "title": "HabitLadder",
            "description": (
                "Backend-сервис для управления привычками с системой ролей, Telegram-уведомлениями через Celery/Redis, "
                "и покрытием тестами ~90%."
            ),
            "tags": ["Django", "DRF", "Celery", "Redis", "Telegram", "pytest"],
            "categories": ["fullstack"],
            "github": "https://github.com/simbarilion/HabitLadder",
            "demo": None,
            "readme_url": "/static/projects/habit-ladder-overview.html",
        },
        {
            "title": "ElectroNet",
            "description": (
                "REST API для управления иерархической сетью продаж электроники. Self-referencing модели, "
                "кастомные permissions DRF и контроль задолженности между звеньями сети."
            ),
            "tags": ["Django", "DRF", "PostgreSQL", "pytest", "Docker"],
            "categories": ["fullstack"],
            "github": "https://github.com/simbarilion/ElectroNet",
            "demo": None,
            "readme_url": "/static/projects/electronet-overview.html",
        },
    ],
    "project_categories": [
        {"id": "all", "label": "Все"},
        {"id": "commercial", "label": "Коммерческие"},
        {"id": "fullstack", "label": "Fullstack / Backend API"},
        {"id": "etl", "label": "Data & ETL"},
        {"id": "integrations", "label": "Integrations & Bots"},
    ],
    "contacts": {
        "location": "Барнаул, Россия (удалённо)",
        "email": "nadezhdapopova13@yandex.ru",
        "github": "https://github.com/simbarilion",
        "telegram": "https://t.me/simbarilion",
        "linkedin": None,
        "intro": (
            "Открыта к новым знакомствам и интересным задачам — "
            "напишите, если ищете backend-разработчика или хотите обсудить идею."
        ),
    },
}
