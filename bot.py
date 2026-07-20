
import asyncio
from telegram import Bot

from config import BOT_TOKEN, CHANNEL_ID
from prices import get_prices
from image_generator import create_image


async def send_post():

    bot = Bot(token="8893002935:AAFS...")

    prices = get_prices()

    image = create_image(prices)

    caption = """
💎 ROYAL GOLD

قیمت لحظه‌ای طلا و ارز

@RoyalGold_Shop
پشتیبانی: @saeedbikhasteh
"""

    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=open(image, "rb"),
        caption=caption
    )


async def main():

    while True:
        try:
            await send_post()

        except Exception as e:
            print(e)

        await asyncio.sleep(1800)


if __name__ == "__main__":
    asyncio.run(main())
