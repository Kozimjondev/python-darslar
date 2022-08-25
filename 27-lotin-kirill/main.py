
from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("5614263656:AAGsUD4MtSa_zQHjGb9jjJU1FVocDfmupxU", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum, Xush kelibsiz!"
    javob+="\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

# matn=input("Matn kiriting: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))







