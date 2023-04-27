from hikka import Hikka
from dick_schedule import *

bot = Hikka()

# Зарегистрировать модуль
bot.register_module(dick_schedule)

bot.run()