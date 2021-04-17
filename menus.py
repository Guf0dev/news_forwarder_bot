import telebot
import parcer
import config

bot = config.bot

def main_menu_keyboard(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Политика','Технологии')
    keyboard.row('Новости обо всём')
    bot.send_message(message.chat.id, 'В этом меню ты можешь выбрать нужную тебе тему', reply_markup=keyboard)

#def politics_menu(message)

def ria_news_politics(message, p_rows):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Ещё новости о политике')
    titles = parcer.ria_news_politics(p_rows)
    bot.send_message(message.chat.id, titles, reply_markup=keyboard, disable_web_page_preview=True)

def ria_news_world(message, w_rows):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Ещё новости о мире')
    titles = parcer.ria_news_world(w_rows)
    bot.send_message(message.chat.id, titles, reply_markup=keyboard, disable_web_page_preview=True)