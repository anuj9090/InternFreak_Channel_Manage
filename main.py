import telebot
from telebot import types

bot = telebot.TeleBot("1866658555:AAG4WdgzUVE3o0pwaE4r2JZEiY99i5Unul4")

@bot.message_handler(commands=['start'])
def gree(msg):
#   print(msg)
  markup = types.ReplyKeyboardMarkup(row_width=2)
  itembtn1 = types.KeyboardButton('/Show_latest_post')
  itembtn2 = types.KeyboardButton('/Show_recently_added_posts')
  itembtn4 = types.KeyboardButton('/start')
  itembtn5 = types.KeyboardButton('/Send_To_Channel')

  markup.add(itembtn1, itembtn2, itembtn4, itembtn5)
  bot.send_message(msg.chat.id, "Hi "+ msg.chat.first_name +"\nIt's the InternFreak bot and here's what I can do. 😀 ", reply_markup=markup)


@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(m):   
 bot.delete_message(m.chat.id,m.message_id)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)