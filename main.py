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

# Асинхронно запускаем бота
async def start_bot():
    async with app:
        await app.start()

# Запускаем бота
if __name__ == '__main__':
    app.loop.create_task(start_bot())

# Отправляем сообщение каждый час
while True:
    with app:
        app.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")
    time.sleep(3600) # ожидаем 1 час
