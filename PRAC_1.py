import telepot
token = '1330303327:AAGUyv5OOgRqGZz5q3qM3WTwIpGcvl8Tn1g'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id.format(msg["text"]))

TelegramBot.message_loop(handle)

