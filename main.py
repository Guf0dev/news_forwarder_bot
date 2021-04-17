import telebot
import parcer
import menus
import logs_saver as lgs
import config

bot = config.bot
p_rows_amount = 1
w_rows_amount = 1
   
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
    keyboard.row('Главное меню')
    bot.send_message(message.chat.id, 'Привет, ' + message.chat.first_name + '! Я бот, который поможет тебе найти новости по любой теме (на известных источниках). Чтобы продолжить, выбери пункт "Главное меню"', reply_markup=keyboard)
    lgs.create_log(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global p_rows_amount, w_rows_amount
    if message.text.lower() == 'главное меню':
        menus.main_menu_keyboard(message)
        lgs.create_log(message)
    if message.text.lower() == 'политика':
        menus.ria_news_politics(message,0)
        lgs.create_log(message)
    if message.text.lower() == 'новости обо всём':
        menus.ria_news_world(message,0)
        lgs.create_log(message)
    if message.text.lower() == 'ещё новости о политике':
        menus.ria_news_politics(message, 5 * p_rows_amount)
        p_rows_amount = p_rows_amount + 1
        if p_rows_amount > 3:
            alert_no_news(message)
            p_rows_amount = 0
    if message.text.lower() == 'ещё новости о мире':
        menus.ria_news_world(message, 5 * w_rows_amount)
        w_rows_amount = w_rows_amount + 1
        if w_rows_amount > 3:
            alert_no_news(message)
            w_rows_amount = 0


def alert(message):
    bot.send_message(message.chat.id, 'Что-то пошло не так :(')

def alert_no_news(message):
    bot.send_message(message.chat.id, 'Кажется, новости в этом разделе кончились :(')

if __name__ == '__main__': 
     bot.infinity_polling()