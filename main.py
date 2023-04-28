import time
import pyrogram
from pyrogram import Client

# Создаем клиента API
app = Client("my_bot")

# Обработчик команды "/farmdick"
@app.on_message(pyrogram.filters.command("farmdick"))
async def send_dick(client, message):
    # Отправляем сообщение в группу
    await client.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")

# Запускаем бота
async def main():
    async with app:
        await app.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")

app.run(main())

# Отправляем сообщение каждый час
while True:
    time.sleep(3600) # ожидаем 1 час
    main()
