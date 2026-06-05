import asyncio
import base64
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, BufferedInputFile

# Railway сам подставит эти значения из панели управления
TOKEN = os.getenv("8742890963:AAHkF3akMyOGCQMheJ6RbhMXSmNiQSpPri0")
AUTHOR_USERNAME = os.getenv("AUTHOR_USERNAME", "@b4s1st") 

if not TOKEN:
    raise ValueError("Ошибка: Переменная окружения BOT_TOKEN не задана!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список твоих VPN-ссылок
VPN_LINKS = [
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@de1.darknet.lol:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=chrome&sni=de1.darknet.lol&alpn=h2#Германия 1",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@nl1.crystalia.world:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=chrome&sni=nl1.crystalia.world&alpn=h2#Нидерланды 1",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@nl2.crystalia.world:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=chrome&sni=nl2.crystalia.world&alpn=h2#Нидерланды 2",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@nl3.crystalia.world:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=chrome&sni=nl3.crystalia.world&alpn=h2#Нидерланды 3",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@nl4.crystalia.world:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=chrome&sni=nl4.crystalia.world&alpn=h2#Нидерланды 4",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@lv2.darknet.cv:443?encryption=none&security=tls&type=grpc&serviceName=grpc&fp=firefox&sni=lv2.darknet.cv&alpn=h2#Латвия 1",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@gg4.darknet.cv:8443?encryption=none&security=reality&type=grpc&serviceName=/api/v1/sync&fp=qq&sni=ads.x5.ru&pbk=zB8I5jz39SXbIroaVYX5jOWqpkg63oh-DUA1OQzX6m4&sid=a2b223d4#Германия Игровой",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@gg6.darknet.cv:8443?encryption=none&security=reality&type=grpc&serviceName=/api/v1/sync&fp=qq&sni=ads.x5.ru&pbk=38UuuYefN13ZjNWs23anya6AjHDYnsEjJrYpGf9p7Q0&sid=a2b223d4#Нидерланды Игровой",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@5.188.115.153:11443?encryption=none&security=reality&type=grpc&fp=firefox&sni=sun6-21.userapi.com&pbk=FDrNbkUYPJS7uzUhgVsNuT8-TqXNeDm7bc24NgTM5GY&sid=846229eb47b3a5c9#Россия Банки ВК",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@5.188.115.153:12443?encryption=none&security=reality&type=grpc&fp=firefox&sni=www.wildberries.ru&pbk=FDrNbkUYPJS7uzUhgVsNuT8-TqXNeDm7bc24NgTM5GY&sid=846229eb47b3a5c9#Россия Банки ВК 2",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@46.243.234.197:9443?encryption=none&security=reality&type=grpc&fp=firefox&sni=ir-2.ozone.ru&pbk=xaCeAr_3ySiXpOLoC2TWPJdkL00Mq_Hbj08ebKZOnW4&sid=846229eb47b3a5c9#Чехия Все Операторы",
    "vless://f5747be5-cd72-4092-93ed-6ab712727e46@81.94.148.189:9443?encryption=none&security=reality&type=grpc&fp=firefox&sni=st.ozone.ru&pbk=eyjAKd47tjI-uh1blnQj69tkctoOuEurbPkxfqq1vB4&sid=846229eb47b3a5c9#Латвия Все Операторы"
]

def generate_subscription():
    raw_text = "\n".join(VPN_LINKS)
    b64_bytes = base64.b64encode(raw_text.encode('utf-8'))
    return b64_bytes.decode('utf-8')

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    sub_config = generate_subscription()
    
    welcome_text = (
        f"👋 <b>Привет! Рад видеть тебя в боте.</b>\n"
        f"👑 <b>Автор бота:</b> {AUTHOR_USERNAME}\n\n"
        f"───────────────────────\n"
        f"🔑 <b>ТВОЙ КОНФИГ ПОДПИСКИ (Base64):</b>\n"
        f"<i>Нажми на код ниже, он автоматически скопируется в буфер обмена:</i>\n\n"
        f"<code>{sub_config}</code>\n"
        f"───────────────────────\n\n"
        f"📖 <b>ИНСТРУКЦИЯ ПО ПОДКЛЮЧЕНИЮ В hApp:</b>\n\n"
        f"1️⃣ <b>Скопируй код</b> подписки выше (просто тапни по нему).\n"
        f"2️⃣ Открой приложение <b>hApp</b>.\n"
        f"3️⃣ Перейди во вкладку <b>«Настройки»</b> или в раздел <b>«Прокси» / «Группы»</b>.\n"
        f"4️⃣ Найди пункт <b>«Добав
