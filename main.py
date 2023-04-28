import time
import pyrogram
from pyrogram import Client

# Создаем клиента API
app = Client("my_bot")

# Обработчик команды "/farmdick"
@app.on_message(pyrogram.filters.command("farmdick"))
def send_dick(client, message):
    # Отправляем сообщение в группу
    client.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")

# Запускаем бота
app.run()

# Отправляем сообщение каждый час
while True:
    with app:
        app.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")
    time.sleep(3600) # ожидаем 1 час
