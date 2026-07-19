
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def create_image(prices):

    width = 1080
    height = 1080

    img = Image.new("RGB", (width, height), "#111111")
    draw = ImageDraw.Draw(img)

    try:
        font_big = ImageFont.truetype("DejaVuSans.ttf", 70)
        font = ImageFont.truetype("DejaVuSans.ttf", 45)
    except:
        font_big = None
        font = None

    draw.text(
        (260, 80),
        "ROYAL GOLD",
        fill="#D4AF37",
        font=font_big
    )

    lines = [
        f"🥇 طلای ۱۸ عیار: {prices['gold18']}",
        f"🥇 طلای ۲۴ عیار: {prices['gold24']}",
        f"🪙 سکه: {prices['coin']}",
        f"💵 دلار: {prices['dollar']}",
        f"🌍 اونس جهانی: {prices['ounce']}",
    ]

    y = 250

    for line in lines:
        draw.text(
            (80, y),
            line,
            fill="#FFFFFF",
            font=font
        )
        y += 120

    draw.text(
        (80, 950),
        f"@RoyalGold_Shop | پشتیبانی: @saeedbikhasteh",
        fill="#D4AF37",
        font=font
    )

    filename = "royal_gold.png"
    img.save(filename)

    return filename
