import asyncio
import os
from telethon.tl.functions.messages import SetTypingRequest, SendReactionRequest
from telethon.tl.types import SendMessageTypingAction, ReactionEmoji
from telethon import TelegramClient
from telethon.errors import ChannelPrivateError, ChatAdminRequiredError, UserPrivacyRestrictedError
from colorama import Fore, init
import random

# Инициализация colorama
init(autoreset=True)

# Чтение данных из файла AKKAYNT.txt
with open('AKKAYNT.txt', 'r', encoding='utf-8') as file:
    data = file.read()
exec(data)

# Чтение конфигурации из config.txt
def read_config():
    config = {
        "min_delay": 200,
        "max_delay": 400,
        "start_delay_min": 3600,
        "start_delay_max": 7200,
        "typing_min": 3,
        "typing_max": 7,
        "max_chats": 0
    }
    if os.path.exists("config.txt"):
        with open("config.txt", "r", encoding="utf-8") as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    key = key.strip().lower()
                    try:
                        config[key] = int(value.strip())
                    except ValueError:
                        pass
    return config

config = read_config()

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

# Список emoji для реакции
EMOJI_LIST = ["❤️", "🔥", "😂", "👍", "🥰", "😎", "😱", "💯", "🤖", "👀"]

async def save_all_chats():
    try:
        dialogs = await client.get_dialogs()
        chats = []
        for dialog in dialogs:
            if dialog.is_group:
                chats.append(dialog.id)
        print(f"{Fore.GREEN}Найдено {len(chats)} бесед.")
        return chats
    except Exception as e:
        print(f"{Fore.RED}Ошибка при получении чатов: {str(e)}")
        return []

async def send_message_to_chat(chat_id, words):
    try:
        print(f"{Fore.YELLOW}Подключение к чату {chat_id}...")
        entity = await client.get_entity(chat_id)
        messages = await client.get_messages(entity, limit=1)
        print(f"{Fore.LIGHTBLUE_EX}Последние сообщения прочитаны.")

        if messages:
            last_msg = messages[0]
            random_emoji = random.choice(EMOJI_LIST)
            await client(SendReactionRequest(
                peer=entity,
                msg_id=last_msg.id,
                reaction=[ReactionEmoji(emoticon=random_emoji)]
            ))
            print(f"{Fore.YELLOW}Поставлена реакция: {random_emoji} на сообщение ID {last_msg.id}")

        print(f"{Fore.LIGHTMAGENTA_EX}Имитируем набор текста...")
        await client(SetTypingRequest(peer=entity, action=SendMessageTypingAction()))
        await asyncio.sleep(random.uniform(config["typing_min"], config["typing_max"]))

        random_word = random.choice(words)
        await client.send_message(entity, random_word)
        print(f"{Fore.GREEN}Сообщение успешно отправлено в чат {entity.title} (ID: {chat_id})!")

        random_delay = random.randint(config["min_delay"], config["max_delay"])
        print(f"{Fore.CYAN}Задержка перед следующим: {random_delay} секунд.")
        await asyncio.sleep(random_delay)

    except (ChannelPrivateError, ChatAdminRequiredError, UserPrivacyRestrictedError) as e:
        print(f"{Fore.RED}Ошибка при отправке в {chat_id}: {str(e)}")
    except Exception as e:
        print(f"{Fore.RED}Ошибка при отправке в {chat_id}: {str(e)}")

async def main():
    await client.start(phone=phone_number)

    delay = random.randint(config["start_delay_min"], config["start_delay_max"])
    print(f"{Fore.CYAN}Ждём {delay // 60} минут перед активностью для маскировки...")
    await asyncio.sleep(delay)

    valid_chat_ids = await save_all_chats()

    if config["max_chats"] > 0:
        valid_chat_ids = valid_chat_ids[:config["max_chats"]]

    with open('words.txt', 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]

    if not valid_chat_ids:
        print(f"{Fore.RED}Нет валидных ID чатов для отправки.")
        return

    while True:
        for chat_id in valid_chat_ids:
            await send_message_to_chat(chat_id, words)
            print(f"{Fore.CYAN}Ждем перед отправкой в следующий чат...")
            await asyncio.sleep(10)

if __name__ == "__main__":
    session_file = 'session_name.session'
    print(f"{Fore.CYAN}У вас есть сессия аккаунта? (Да/Нет): ", end="")
    answer = input().strip().lower()

    if answer in ["да", "y", "yes"]:
        if os.path.exists(session_file):
            print(f"{Fore.GREEN}Сессия найдена. Запуск клиента...")
            with client:
                print(f"{Fore.MAGENTA}Запуск скрипта...")
                client.loop.run_until_complete(main())
        else:
            print(f"{Fore.RED}Сессия не найдена. Убедитесь, что файл {session_file} существует.")
    else:
        print(f"{Fore.YELLOW}Запуск нового входа в аккаунт...")
        with client:
            client.loop.run_until_complete(main())
