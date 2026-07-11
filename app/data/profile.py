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
        {"value": "Flask", "label": "Микрофреймворк"},
    ],
    "about": {
        "role": "Python Backend Developer",
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
                "Python Backend-разработчик с опытом коммерческой разработки и создания "
                "собственных проектов на Django и FastAPI."
            ),
            (
                "Разрабатываю REST API, бизнес-логику, "
                "проектирую модели данных, реализую интеграции с внешними сервисами и фоновые процессы."
            ),
            (
                "Есть опыт разработки fullstack-приложений, ETL-пайплайнов, Telegram-интеграций "
                "и рекомендательных систем. Уверенно работаю с PostgreSQL, Docker, Celery, Redis, "
                "Git и Linux."
            ),
            (
                "Сейчас развиваю коммерческий проект в ООО «Экосистема Альфа» — платформу "
                "автоматизации курьерской доставки. Параллельно веду собственные проекты с полным циклом: "
                "от проектирования API до деплоя на VPS."
            ),
            (
                "При написании кода руководствуюсь принципами SOLID, DRY и KISS: проектирую "
                "масштабируемую архитектуру с разделением ответственности между слоями представлений, "
                "сервисов и репозиториев, применяю архитектурные паттерны Repository, Service Layer "
                "и Strategy. Разрабатываю код с учётом тестируемости, сопровождаемости, расширяемости "
                "и долгосрочной поддержки."
            ),
        ],
    },
    "skills": [
        {"name": "Python", "level": 90},
        {"name": "Django", "level": 82},
        {"name": "Django REST Framework", "level": 78},
        {"name": "REST API", "level": 85},
        {"name": "PostgreSQL", "level": 78},
        {"name": "SQLite", "level": 65},
        {"name": "Redis", "level": 72},
        {"name": "Celery", "level": 70},
        {"name": "Docker", "level": 78},
        {"name": "Git / GitHub Actions", "level": 85},
        {"name": "Pytest", "level": 72},
        {"name": "FastAPI", "level": 68},
        {"name": "Flask", "level": 55},
        {"name": "httpx", "level": 68},
        {"name": "requests", "level": 72},
        {"name": "HTML / CSS", "level": 62},
        {"name": "JavaScript / AJAX", "level": 58},
        {"name": "Nginx", "level": 62},
        {"name": "Beautiful Soup", "level": 48},
        {"name": "Telegram Bot API / aiogram", "level": 70},
        {"name": "Apache Airflow", "level": 52},
        {"name": "Linux / Bash", "level": 72},
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
            "description": "Участие в в конференции по PostgreSQL (г. Москва).",
        },
    ],
    "experience": [
        {
            "title": "Python Backend Developer",
            "period": "Апрель 2026 — настоящее время",
            "company": 'ООО «Экосистема Альфа», Москва (удалённо)',
            "bullets": [
                (
                    "Коммерческий проект: веб-приложение для автоматизации курьерской доставки"
                ),
                (
                    "Стек: Python, Django, Django REST Framework, PostgreSQL, JWT, Redis, Celery, "
                    "Telegram API, Nginx, Gunicorn, Swagger, Git, Docker"
                ),
                (
                    "Разрабатывала и сопровождала REST API"
                ),
                (
                    "Провела рефакторинг подсистемы геолокации: спроектировала новые модели хранения "
                    "координат, реализовала API и бизнес-логику обновления местоположения курьеров"
                ),
                (
                    "Доработала бизнес-логику обработки заказов: реализовала механизм начала доставки "
                    "и разделение причин отмены"
                ),
                (
                    "Улучшила регистрацию и email-активацию пользователей, оптимизировала выполнение "
                    "Celery-задач на production"
                ),
                (
                    "Проанализировала причины нестабильной работы Celery и участвовала в повышении стабильности фоновых задач"
                ),
                (
                    "Выполняла рефакторинг, исправляла production-баги и участвовала в проектировании новых решений"
                ),
                (
                    "Взаимодействовала с frontend-разработчиками при проектировании и интеграции API, "
                    "участвовала в code review и командной разработке с Git"
                )
            ],
        },
        {
            "title": "Backend-разработчик (Python)",
            "period": "Март 2025 — настоящее время",
            "company": "Freelance & собственные проекты",
            "bullets": [
                (
                    "Backend- и fullstack-приложения, REST API, автоматизация "
                    "и интеграции с внешними сервисами."
                ),
                (
                    "Проектирование БД, фоновые задачи, деплой на VPS, "
                    "CI/CD через GitHub Actions."
                ),
                (
                    "Стек: Django, DRF, FastAPI, Flask, PostgreSQL, SQLite, Redis, Celery, "
                    "APScheduler, Telegram Bot API, aiogram, requests, httpx, Apache Airflow, "
                    "pytest, Sentry, Docker, Docker Compose, Nginx, Git, GitHub Actions, "
                    "HTML, CSS, JavaScript, AJAX."
                ),
            ],
        },
    ],
    "projects": [
        {
            "title": "WB Limits Tracker",
            "description": (
                "Telegram-бот для мониторинга лимитов приёмки Wildberries. "
                "Интеграция с API Wildberries, периодический опрос через APScheduler, уведомления пользователей "
                "и шифрование API-ключей."
            ),
            "tags": ["Python", "aiogram", "Flask", "httpx", "Pydantic", "SQLite", "pytest"],
            "categories": ["commercial", "integrations"],
            "github": "https://github.com/simbarilion/WBLimitsTracker",
            "demo": None,
            "video_url": None,
            "readme_url": "/static/projects/wb-limits-tracker-readme.html",
        },
        {
            "title": "Oh! my tea — YML Feed",
            "description": (
                "Сервис генерации YML-фида для магазина чая. "
                "Валидация каталога по бизнес-правилам, отчёт об отсеянных позициях, сборка XML "
                "для Яндекс.Маркета и Яндекс.Директа, интерактивное демо."
            ),
            "tags": ["Python", "XML", "pytest", "JavaScript"],
            "categories": ["commercial", "integrations"],
            "github": "https://github.com/simbarilion/Oh-my-tea-demo",
            "demo": "https://simbarilion.github.io/Oh-my-tea-demo/",
            "readme_url": "/static/projects/oh-my-tea-overview.html",
        },
        {
            "title": "FilmDiary",
            "description": (
                "Fullstack-платформа персональных рекомендаций фильмов. REST API (20+ эндпоинтов), "
                "система ролей, рекомендательная система, Telegram-интеграция, фоновые Celery-задачи, frontend на JS."
            ),
            "tags": ["Django", "DRF", "PostgreSQL", "Celery", "Redis", "JavaScript", "pytest", "Docker", "CI/CD"],
            "categories": ["fullstack"],
            "github": "https://github.com/simbarilion/FilmDiary",
            "demo": None,
            "video_url": None,
            "readme_url": "/static/projects/film-diary-overview.html",
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
        "phone": "+7 (923) 643-03-97",
        "github": "https://github.com/simbarilion",
        "telegram": "https://t.me/simbarilion",
        "linkedin": None,
        "intro": (
            "Открыта к новым знакомствам и интересным задачам — "
            "напишите, если ищете backend-разработчика или хотите обсудить идею."
        ),
    },
}
