import asyncio
import pyrogram
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

# Создаем клиента API
app = Client("my_bot")

# Обработчик команды "/farmdick"
@app.on_message(filters.command("farmdick"))
async def send_dick(client, message):
    # Получаем chat_id из объекта message
    chat_id = message.chat.id
    # Отправляем сообщение в группу
    await client.send_message(chat_id=chat_id, text="/dick@dickupbot")

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
                    # Получаем chat_id из объекта message
                    chat_id = (await app.get_chat("my_group_name")).id
                    await app.send_message(chat_id=chat_id, text="/dick@dickupbot")
                await asyncio.sleep(3600) # ожидаем 1 час
            except Exception as e:
                print(e)

    # Регистрируем фильтр
    app.add_handler(
        pyrogram.filters.create(
            lambda _, __, message: message.chat.type in ["group", "supergroup"]
        ),
        send_message,
    )

    asyncio.get_event_loop().run_forever()
