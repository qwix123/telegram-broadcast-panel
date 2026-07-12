# Telegram Broadcast Panel - Инструкция по запуску

## 🚀 Быстрый старт (Docker)

### Требования
- Docker & Docker Compose
- Telegram API ID и API Hash (https://my.telegram.org/)

### Шаг 1: Скачайте репо
```bash
git clone https://github.com/qwix123/telegram-broadcast-panel.git
cd telegram-broadcast-panel
```

### Шаг 2: Настройте .env
```bash
cp .env.example .env
```

Отредактируйте `.env` и добавьте:
```env
API_ID=123456          # Ваш Telegram API ID
API_HASH=abc123def...  # Ваш Telegram API Hash
PROXY_ENABLED=false    # Включить прокси (true/false)
PROXY_SERVER=          # IP прокси сервера
PROXY_PORT=            # Порт прокси
```

### Шаг 3: Запустите Docker Compose
```bash
docker-compose up -d
```

### Шаг 4: Откройте панель
- **Фронтенд**: http://localhost
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🛠️ Локальный запуск

### Backend
```bash
cd backend
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

Бакенд запустится на `http://localhost:8000`

### Frontend (новый терминал)
```bash
cd frontend
npm install
npm run dev
```

Фронтенд откроется на `http://localhost:5173`

---

## 📱 Получение Telegram API

1. Перейдите на https://my.telegram.org/
2. Введите номер телефона
3. Подтвердите вход
4. Перейдите в "API development tools"
5. Создайте приложение (App title = любое имя)
6. Скопируйте **API ID** и **API Hash**
7. Вставьте в `.env`

---

## 🔐 Первый вход

1. Откройте http://localhost
2. Введите номер телефона в формате: `+7 (999) 123-45-67`
3. Нажмите "Получить код"
4. Вас попросят подтвердить вход в Telegram
5. После подтверждения вернитесь на панель и введите код
6. Готово! ✅

---

## 🌐 Структура API

### Аутентификация
- `POST /api/auth/request-code` - Запрос кода
- `POST /api/auth/login` - Вход
- `POST /api/auth/logout` - Выход

### Рассылка
- `POST /api/broadcast/send` - Отправить рассылку
- `GET /api/broadcast/history` - История
- `GET /api/broadcast/stats` - Статистика

### Чаты
- `GET /api/chats/list` - Список чатов
- `GET /api/chats/{chat_id}` - Детали чата
- `POST /api/chats/add-favorite/{chat_id}` - В избранное

### Папки
- `GET /api/folders/list` - Список папок
- `POST /api/folders/create` - Создать папку
- `POST /api/folders/{folder_id}/add-chat/{chat_id}` - Добавить в папку

### Прокси
- `GET /api/proxy/config` - Текущая конфигурация
- `POST /api/proxy/config` - Установить прокси
- `POST /api/proxy/test` - Тестировать прокси

---

## 🎨 Особенности дизайна

✨ **Темный режим с градиентом** - красивый и удобный интерфейс
🎯 **Адаптивный дизайн** - работает на мобильных и десктопных устройствах
⚡ **Быстрая загрузка** - Vite для фронтенда, FastAPI для бэкенда
🔐 **Безопасность** - JWT токены, CORS, HTTPS поддержка
📱 **Интуитивный интерфейс** - легко использовать

---

## 📊 Функции

✅ Аутентификация по номеру телефона
✅ Поддержка прокси серверов
✅ Управление чатами
✅ Работа с папками
✅ Два типа рассылки (избранное + пересылка)
✅ История рассылок
✅ Статистика
✅ REST API

---

## 🔧 Переменные окружения

| Переменная | Описание | По умолчанию |
|---|---|---|
| `API_ID` | Telegram API ID | - |
| `API_HASH` | Telegram API Hash | - |
| `PROXY_ENABLED` | Включить прокси | false |
| `PROXY_TYPE` | Тип прокси (http/socks5) | http |
| `PROXY_SERVER` | IP прокси | - |
| `PROXY_PORT` | Порт прокси | - |
| `DATABASE_URL` | URL БД | sqlite:///./app.db |
| `BACKEND_HOST` | Host бэкенда | 0.0.0.0 |
| `BACKEND_PORT` | Порт бэкенда | 8000 |
| `VITE_API_URL` | URL API для фронтенда | http://localhost:8000 |
| `SECRET_KEY` | Секретный ключ | your-secret-key-... |

---

## 📝 Логи

Логи сохраняются в `logs/app.log`

---

## 🐛 Решение проблем

### "Connection refused"
- Убедитесь, что бэкенд запущен на порту 8000
- Проверьте `.env` файл

### "Invalid API ID"
- Проверьте, что API ID и Hash верны
- Перейдите на https://my.telegram.org/ и проверьте

### "Proxy error"
- Проверьте, что прокси сервер доступен
- Попробуйте отключить прокси (`PROXY_ENABLED=false`)

### "Database locked"
- Закройте все подключения к БД
- Удалите `app.db` и перезапустите

---

## 📞 Поддержка

Если у вас есть вопросы, откройте Issue на GitHub.

---

**Версия**: 1.0.0
**Лицензия**: MIT
**Автор**: @qwix123