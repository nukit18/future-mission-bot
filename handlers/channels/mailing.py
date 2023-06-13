import asyncio
import aioschedule as aioschedule
from data import config
from loader import bot


async def mailing(text):
    await bot.send_message(config.CHANNEL_ID, text)


async def open_text():
    file = open("data/mailing.txt", "r", encoding='utf-8')
    text = file.read()
    file.close()
    counter = int(text.split("/")[0])
    if counter >= len(text.split("/")) - 1:
        counter = 1
    mail = text.split("/")[counter]
    new_text = str(counter+1) + text[1:]
    file = open("data/mailing.txt", "w", encoding='utf-8')
    file.write(new_text)
    file.close()
    await mailing(mail)


async def mailing_schedule():
    await asyncio.sleep(10)
    print("Запускаем скрипт рассылки")
    aioschedule.every().monday.at("10:00").do(open_text)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(60)