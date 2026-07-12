# 📱 Telegram Broadcast Panel

Полнофункциональная веб-панель для управления Telegram рассылками, работы с чатами, папками и прокси.

## 🎯 Возможности

- ✅ Аутентификация по номеру телефона с поддержкой прокси
- ✅ Управление чатами и папками
- ✅ Два типа рассылки: из избранного и пересылка
- ✅ Работа с прокси серверами
- ✅ Веб-интерфейс для управления
- ✅ API для интеграции
- ✅ История рассылок и статистика

## 🛠️ Технологический стек

**Backend:**
- FastAPI (Python)
- Telethon (библиотека Telegram)
- SQLAlchemy + SQLite
- Pydantic для валидации

**Frontend:**
- Vue.js 3
- Vite
- Axios
- TailwindCSS

**DevOps:**
- Docker & Docker Compose
- Nginx (для production)

## 📦 Установка

### Требования
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose (опционально)

### Локальная установка

```bash
# Клонируем репозиторий
git clone https://github.com/qwix123/telegram-broadcast-panel.git
cd telegram-broadcast-panel

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
```

## 🚀 Запуск

### Backend
```bash
cd backend
python main.py
# API будет доступен на http://localhost:8000
```

### Frontend
```bash
cd frontend
npm run dev
# Панель будет доступна на http://localhost:5173
```

### Docker
```bash
docker-compose up -d
```

## 📖 Документация API

После запуска backend посетите:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔑 Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# Telegram
API_ID=123456
API_HASH=your_api_hash

# Прокси
PROXY_ENABLED=false
PROXY_SERVER=
PROXY_PORT=

# База данных
DATABASE_URL=sqlite:///./app.db

# Backend
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend
VITE_API_URL=http://localhost:8000
```

## 📝 Структура проекта

```
telegram-broadcast-panel/
├── backend/
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── core/          # Основной функционал
│   │   ├── services/      # Бизнес-логика
│   │   ├── models/        # Модели БД
│   │   ├── schemas/       # Pydantic схемы
│   │   └── main.py        # FastAPI приложение
│   ├── requirements.txt
│   ├── .env.example
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/    # Компоненты Vue
│   │   ├── views/         # Страницы
│   │   ├── store/         # Vuex store
│   │   ├── services/      # API сервисы
│   │   └── App.vue
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🔐 Безопасность

- Все данные аутентификации хранятся в зашифрованном виде
- Поддержка HTTPS
- Rate limiting на API endpoints
- CORS конфигурация

## 🤝 Вклад

Приветствуются pull requests с новыми функциями!

## 📄 Лицензия

MIT License

## 📞 Поддержка

Если у вас есть вопросы или проблемы, откройте Issue на GitHub.

---

**Статус**: 🚧 В разработке