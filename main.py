import schedule
import time

from hikka import Hikka
from hikka.decorators import register

bot = Hikka()

@register(events.NewMessage(pattern='/farmdick'))
async def start_schedule(event):
    # Запустить расписание, когда получена команда /farmdick
    schedule_pick()
    await event.reply('Scheduled /dick@dickupbot every hour!')

def job():
    # Функция для выполнения задания
    bot.send_message('dickupbot', '/dick')

def schedule_pick():
    # Запустить задание каждый час
    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

bot.run()
