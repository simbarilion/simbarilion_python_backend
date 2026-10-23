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
            {"label": "Образование", "value": "Высшее + SkyPro + ModulDev"},
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
                "Python Backend-разработчик (Django / FastAPI): REST API, бизнес-логика, "
                "интеграции с внешними сервисами и фоновые процессы."
            ),
            (
                "Работаю с PostgreSQL, SQLAlchemy, Celery, Redis, Kafka (aiokafka), Docker, Git. "
                "Есть опыт разработки fullstack-приложений и ETL-пайплайнов."
            ),
            (
                "Прошла backend-стажировку ModulDev в Модульбанке: спроектировала и собрала единый банковский контур: "
                "API, транзакции, идемпотентность, внешние интеграции, обработка сбоев и наблюдаемость."
            ),
            (
                "Сейчас — коммерческий проект в ООО «Экосистема Альфа»: backend PWA-сервиса для владельцев питомцев. "
                "Ранее в той же компании — платформа автоматизации курьерской доставки."
            ),
            (
                "Параллельно веду собственные и клиентские проекты полного цикла — от проектирования API до production."
            ),
            (
                "Использую AI-инструменты (Cursor, GitHub Copilot и ChatGPT) как часть рабочего процесса: "
                "для ускорения разработки и исследования, с обязательной верификацией результата и доработкой решений."
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
                "SQLAlchemy",
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
                "Kafka / aiokafka",
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
                "Uvicorn",
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
            "note": "Исследование требований, проверка решений, разбор ошибок",
            "skills": [
                "Cursor",
                "GitHub Copilot",
                "ChatGPT",
            ],
        },
    ],
    "education": [
        {
            "degree": "Разработка машинного обучения",
            "period": "Август 2026 — настоящее время",
            "institution": "Учебный центр «ШИФТ» (АНО ДПО) — проект ШИФТ",
            "description": (
                "Участие в проекте ШИФТ по направлению «Разработка машинного обучения»."
            ),
        },
        {
            "degree": (
                "Диплом об успешном окончании адаптационного курса "
                "«Backend разработка банковских систем»"
            ),
            "period": "05.10.2026, Москва",
            "institution": "ModulDev · Модульбанк",
            "description": (
                "Backend-стажировка (17.08–05.10.2026): проектирование и сборка единого банковского контура — "
                "API, транзакционная логика, идемпотентность, внешние интеграции, обработка сбоев и наблюдаемость. "
                "Итоговый проект: ReliaPay."
            ),
        },
        {
            "degree": "Backend-разработчик (Python)",
            "period": "2026",
            "institution": "SkyPro — профессиональная переподготовка",
            "description": (
                "Профессиональная переподготовка по дополнительной профессиональной программе «Python-разработчик»."
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
            "projects": [
                {
                    "label": "PWA для владельцев питомцев",
                    "stack": (
                        "Python, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, "
                        "Redis, Celery, S3, Uvicorn, JWT, Docker, Nginx, Git"
                    ),
                    "bullets": [
                        (
                            "Развиваю backend PWA-сервиса для владельцев питомцев: "
                            "несколько питомцев, паспорт и прививки, календарь и напоминания, "
                            "медицинские записи, загрузка документов, уведомления, экспорт и удаление данных"
                        ),
                        (
                            "Вынесла доставку уведомлений (email, Web Push) и фоновую обработку в Celery/Redis"
                        ),
                        (
                            "Реализовала загрузку и выдачу файлов через закрытое S3-совместимое хранилище"
                        ),
                        (
                            "Участвую в разработке API синхронизации для офлайн-режима PWA"
                        ),
                        (
                            "Согласовываю API с frontend, участвую в code review и командной разработке в Git"
                        ),
                    ],
                },
                {
                    "label": "Платформа курьерской доставки",
                    "stack": (
                        "Python, Django, DRF, PostgreSQL, JWT, Redis, Celery, "
                        "Telegram API, Nginx, Git, Docker"
                    ),
                    "bullets": [
                        (
                            "Развивала backend платформы автоматизации курьерской доставки: "
                            "REST API, бизнес-логика заказов, сопровождение production"
                        ),
                        (
                            "Переработала геолокацию курьеров: модели координат, API и обновление местоположения"
                        ),
                        (
                            "Доработала жизненный цикл заказа: старт доставки и причины отмены — "
                            "прозрачные статусы для клиентов и операций"
                        ),
                        (
                            "Улучшила регистрацию/email-активацию; стабилизировала Celery на production"
                        ),
                    ],
                },
            ],
        },
        {
            "title": "Backend-стажёр (ModulDev)",
            "period": "17 августа — 5 октября 2026",
            "company": "ModulDev · Модульбанк, Москва",
            "stack": (
                "Python, C#, PostgreSQL, Docker, JWT; "
                "AI-инструменты — исследование требований, проверка решений, расследование ошибок"
            ),
            "bullets": [
                (
                    "Спроектировала и собрала единый банковский контур ReliaPay — систему, "
                    "через которую безопасно принимаются запросы, выполняются операции и запускаются сценарии оплаты"
                ),
                (
                    "Проектировала API: вход по токену, проверка данных запроса, каталог операций, "
                    "единый понятный формат ответов об успехе и ошибках"
                ),
                (
                    "Реализовывала надёжную обработку операций в базе: повтор того же запроса не создаёт дубликат, "
                    "а при другом содержимом система возвращает конфликт"
                ),
                (
                    "Настраивала обмен с внешними сервисами: очередь исходящих и входящих сообщений, "
                    "доставку платежа провайдеру, восстановление после сбоев и мониторинг состояния системы"
                ),
            ],
        },
        {
            "title": "Backend-разработчик (Python)",
            "period": "Март 2025 — настоящее время",
            "company": "Freelance & собственные проекты",
            "stack": (
                "Django/DRF, FastAPI, SQLAlchemy, Uvicorn, PostgreSQL, SQLite, Redis, "
                "Kafka/aiokafka, Celery, aiogram, requests, httpx, Apache Airflow, pytest, Sentry, "
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
            "title": "ReliaPay",
            "description": (
                "Итоговый проект стажировки ModulDev (Модульбанк): единый банковский контур. "
                "Единая точка входа для API-запросов и среда выполнения банковских операций и сценариев оплаты в PostgreSQL. "
                "Спроектированы API и контракты, надёжная обработка операций без дублей, "
                "доставка платежей во внешний сервис, обработка сбоев и мониторинг."
            ),
            "tags": [
                "Python",
                "C#",
                "PostgreSQL",
                "Docker",
                "JWT",
                "REST API",
            ],
            "categories": ["fullstack"],
            "github": "https://github.com/simbarilion/ReliaPay",
            "demo": None,
            "featured": False,
            "readme_url": "/static/projects/reliapay-overview.html?v=3",
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
