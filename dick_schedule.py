import schedule
import time
from telethon import events

@events.register(events.NewMessage(pattern='/farmdick'))
async def start_schedule(event):
    # Запустить расписание, когда получена команда /farmdick
    schedule_pick()
    await event.reply('Scheduled /dick@dickupbot every hour!')

def job():
    # Функция для выполнения задания
    client.send_message('dickupbot', '/dick')

def schedule_pick():
    # Запустить задание каждый час
    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Зарегистрировать модуль
bot.register_module(dick_schedule)

bot.run()
