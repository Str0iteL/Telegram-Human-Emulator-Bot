# 🤖 Telegram Human Emulator Bot

```markdown

Скрипт для **эмуляции активности живого пользователя** в Telegram. Имитирует чтение сообщений, набор текста, отправку сообщений и проставление реакций. Отлично подходит для разогрева аккаунтов, создания активности в группах и автоматизированного участия в чатах.

---

⚙️ Возможности

- Автоматическое подключение к Telegram через `Telethon`
- Получение списка всех групповых чатов
- Имитирование "набора текста" перед отправкой
- Отправка случайного сообщения из `words.txt`
- Случайная реакция на последнее сообщение в чате
- Умные задержки между действиями для маскировки
- Поддержка конфигурации через `config.txt`

---

📁 Структура проекта

```
TelegramHumanBot/
├── main.py             # Основной скрипт
├── AKKAYNT.txt         # Содержит api_id, api_hash и phone_number
├── config.txt          # Конфигурация задержек
├── words.txt           # Список слов/фраз для отправки
├── session_name.session  # Автоматически создаётся после входа
```

---

## 🧠 Что нужно изменить под себя

### 1. `AKKAYNT.txt`

Создай файл `AKKAYNT.txt` и добавь туда свои данные:

```txt
api_id = 123456
api_hash = 'abcdef1234567890abcdef1234567890'
phone_number = '+1234567890'
```

2. Инициализация клиента

В `main.py` находится блок:

```python
# Инициализация клиента
client = TelegramClient(
    'session_name',
    api_id,
    api_hash,
    device_model='X570 MB',
    system_version='Windows 10 x64',
    lang_code='ru',
    system_lang_code='ru'
)
```

Этот блок нужно **изменить под свой Telegram-клиент**.

Для имитации мобильного устройства можно использовать, например:

```python
client = TelegramClient(
    'session_name',
    api_id,
    api_hash,
    device_model='Xiaomi Redmi Note 8',
    system_version='Android 11',
    lang_code='ru',
    system_lang_code='ru'
)
```

---

🧾 Формат `config.txt` (опционально)

```ini
min_delay=200
max_delay=400
start_delay_min=3600
start_delay_max=7200
typing_min=3
typing_max=7
max_chats=0
```

| Параметр           | Описание                                         |
|--------------------|--------------------------------------------------|
| `min_delay`        | Минимальная задержка между чатами (в секундах)  |
| `max_delay`        | Максимальная задержка между чатами              |
| `start_delay_min`  | Минимальная задержка перед началом активности   |
| `start_delay_max`  | Максимальная задержка перед началом активности  |
| `typing_min`       | Минимальное время "набора текста"               |
| `typing_max`       | Максимальное время "набора текста"              |
| `max_chats`        | Сколько чатов использовать (0 = все)            |

---

📄 Пример `words.txt`

```txt
Привет!
Как дела?
Что нового?)
👋
Доброе утро!
```

---

🚀 Запуск

```bash
python main.py
```

При первом запуске потребуется ввести код из Telegram. Сессия будет сохранена.

---

🔐 Безопасность

- Используется **официальная библиотека Telethon**
- Скрипт **не сохраняет пароли**
- Все действия выполняются только от **твоего имени**

---

📌 Требования

- Python 3.8+
- Установленные библиотеки: `telethon`, `colorama`

```bash
pip install telethon colorama
```

---

🧪 Советы

- Используй прокси/VPN для дополнительной анонимности
- Не спамь — это эмулятор, а не спамер
- Добавь больше фраз в `words.txt` для реалистичности

---

👤 Автор

**Пикарина / Дэн**  
Telegram: [@твой_ник](https://t.me/Falruper)

---

## ⭐ Если скрипт полезен — поставь звёздочку на GitHub!
```
