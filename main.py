import asyncio
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

if __name__ == '__main__':
    # Запускаем бота
    asyncio.get_event_loop().run_until_complete(start_bot())

    # Отправляем сообщение каждый час
    async def send_message():
        while True:
            try:
                async with app:
                    await app.send_message(chat_id="GROUP_CHAT_ID", text="/dick@dickupbot")
                await asyncio.sleep(3600) # ожидаем 1 час
            except Exception as e:
                print(e)

    asyncio.get_event_loop().create_task(send_message())
    asyncio.get_event_loop().run_forever()
