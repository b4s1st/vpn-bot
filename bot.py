import telebot

# === НАСТРОЙКИ ===
TOKEN = "8742890963:AAHkF3akMyOGCQMheJ6RbhMXSmNiQSpPri0"

OWNER_TG = "@b4s1st"
CONFIG_NAME = "b4s1st config"
GITHUB_NICK = "b4s1st"

# Ссылки на конфиги
CONFIGS = {
    "default": f"https://{GITHUB_NICK}.github.io/rjsxrd/githubmirror/default/6.txt",
    "bypass":  f"https://{GITHUB_NICK}.github.io/rjsxrd/githubmirror/bypass/bypass-all.txt",
    "all":     f"https://{GITHUB_NICK}.github.io/rjsxrd/githubmirror/default/all.txt",
}

bot = telebot.TeleBot(TOKEN)

# === Команда /start ===
@bot.message_handler(commands=["start"])
def start(message):
    text = (
        f"👋 Привет! Это бот для раздачи VPN-конфигов.\n\n"
        f"📦 Конфиг: *{CONFIG_NAME}*\n"
        f"👤 Автор: {OWNER_TG}\n\n"
        f"Используй команды:\n"
        f"/link — стандартный конфиг\n"
        f"/bypass — конфиг для мобильного интернета\n"
        f"/all — все серверы сразу\n"
        f"/help — помощь по настройке"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# === Команда /link ===
@bot.message_handler(commands=["link"])
def send_link(message):
    text = (
        f"📦 *{CONFIG_NAME}*\n\n"
        f"Скопируй ссылку и добавь в Happ как подписку:\n\n"
        f"`{CONFIGS['default']}`\n\n"
        f"👤 Автор: {OWNER_TG}"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# === Команда /bypass ===
@bot.message_handler(commands=["bypass"])
def send_bypass(message):
    text = (
        f"📦 *{CONFIG_NAME}* — для мобильного интернета\n\n"
        f"Скопируй ссылку и добавь в Happ как подписку:\n\n"
        f"`{CONFIGS['bypass']}`\n\n"
        f"👤 Автор: {OWNER_TG}"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# === Команда /all ===
@bot.message_handler(commands=["all"])
def send_all(message):
    text = (
        f"📦 *{CONFIG_NAME}* — все серверы\n\n"
        f"Скопируй ссылку и добавь в Happ как подписку:\n\n"
        f"`{CONFIGS['all']}`\n\n"
        f"👤 Автор: {OWNER_TG}"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# === Команда /help ===
@bot.message_handler(commands=["help"])
def send_help(message):
    text = (
        f"📖 *Как добавить конфиг в Happ:*\n\n"
        f"1. Нажми /link и скопируй ссылку\n"
        f"2. Открой Happ\n"
        f"3. Подписки → добавить → вставь ссылку\n"
        f"4. Включи сортировку по пингу\n\n"
        f"Конфиги обновляются автоматически каждые 2 дня 🔄\n\n"
        f"По вопросам: {OWNER_TG}"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# === Запуск ===
print("Бот запущен...")
bot.infinity_polling()
