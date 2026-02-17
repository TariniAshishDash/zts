# ZTS Project

Welcome to the ZTS project. This repository contains the core functionality and infrastructure for the ZTS application.

## Project Structure

```plaintext
zts/
├── README.md
├── requirements.txt
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── setup.py
├── config/
│   ├── __init__.py
│   └── config.py
├── core/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── authenticator.py
│   │   ├── mfa_handler.py
│   │   └── password_manager.py
│   ├── access_control/
│   │   ├── __init__.py
│   │   ├── rbac.py
│   │   ├── abac.py
│   │   └── policy_engine.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── db_manager.py
│   └── monitoring/
│       ├── __init__.py
│       ├── logger.py
│       └── audit.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   ├── access_routes.py
│   │   └── health_routes.py
│   └── middleware/
│       ├── __init__.py
│       ├── auth_middleware.py
│       └── rate_limit.py
├── web/
│   ├── __init__.py
│   ├── dashboard.py
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       └── users.html
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_access_control.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_DOCUMENTATION.md
│   ├── SETUP_GUIDE.md
│   └── COMPONENTS.md
└── scripts/
    ├── init_db.py
    └── create_admin.py
```

## Getting Started

To get started with the ZTS project, please follow the steps in the `SETUP_GUIDE.md` file located in the `docs` directory.