import asyncio
import schedule
from telethon import events

@borg.on(events.NewMessage(pattern="/farmdick"))
async def farm_dick(event):
    await event.reply("Starting to farm dicks!")
    schedule_pick()

def job():
    borg.send_message("dickupbot", "/dick@dickupbot")

def schedule_pick():
    # Запустить задание каждый час
    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
