import telebot
from text import *
from config import Token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton



bot = telebot.TeleBot(Token)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("оружие и патроны 🔫", callback_data="gun"),
            InlineKeyboardButton("транспорт и перемещение 🚘", callback_data="cars"),
            InlineKeyboardButton("персонажей 👦", callback_data="Skills"))
    markup.add(InlineKeyboardButton("погоду 🌧️", callback_data="weather"),
            InlineKeyboardButton("другое 🛸", callback_data="other"))

    return markup



def gen_markup_Guns():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Всё оружие", callback_data="Allguns"),
            InlineKeyboardButton("Взрывные атаки ближнего боя", callback_data="BoomAttack"),)
    markup.add(InlineKeyboardButton("Взрывные патроны", callback_data="BoomPatrons"),
            InlineKeyboardButton("Поджигающие пули ", callback_data="FirePatrons"),)
    
    return markup

def gen_markup_Cars():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Вызов comet", callback_data="comet"),
            InlineKeyboardButton("мотоцикл для бездорожья", callback_data="sanchez"),
            InlineKeyboardButton("Спроткар", callback_data="Rapid_GT"))
    markup.add(InlineKeyboardButton("спортивный мотоцикл", callback_data="Sportbike"),
            InlineKeyboardButton("маслкар", callback_data="Better_Dominic"),)
    
    return markup

def gen_markup_Skills():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Режим пьяницы", callback_data="drunkard"),
            InlineKeyboardButton("Лунная гравитация", callback_data="gravity"),
            InlineKeyboardButton("Быстрый бег", callback_data="fast_run"))
    markup.add(InlineKeyboardButton("Неуязвимость", callback_data="invulnerability"),
            InlineKeyboardButton("Суперпрыжок", callback_data="super_jump"))
    
    return markup
def gen_markup_Weather():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Скользящие машины", callback_data="Sliding_cars"),
            InlineKeyboardButton("Дождливая погода", callback_data="rainy_weather"))
    return markup

def gen_markup_Other():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Понизить уровень розыска", callback_data="PoliceM"),
               InlineKeyboardButton("Увеличить уровень розыска", callback_data="PoliceP"),)
    markup.add(InlineKeyboardButton("Замедленное время", callback_data="SlowTime"),)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, text_start)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup())
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, text_info)
    


@bot.callback_query_handler(func=lambda call: call.data in [])
def callback_query(call):
    if call.data == "gun":
        first(call.message)
    elif call.data == "cars":
        second(call.message)
    elif call.data == "skins":
        third(call.message)
    elif call.data == "weather":
        fourd(call.message)
    elif call.data == "other":
        fiveth(call.message)
        

# Handle submenu callbacks
@bot.callback_query_handler(func=lambda call: call.data in ["Allguns", "BoomAttack", "BoomPatrons", "FirePatrons"])
def submenu_callback_query(call):
    if call.data == "Allguns":
        bot.send_message(call.message.chat.id, gun_Allguns)
    elif call.data == "BoomAttack":
        bot.send_message(call.message.chat.id, gun_BoomAttack)
    elif call.data == "BoomPatrons":
        bot.send_message(call.message.chat.id, gun_BoomPatrons)
    elif call.data == "FirePatrons":
        bot.send_message(call.message.chat.id, gun_FirePatrons)

@bot.callback_query_handler(func=lambda call: call.data in ["comet", "sanchez", "Rapid_GT", "Sportbike", "Better_Dominic"])
def submenu_callback_query(call):
    if call.data == "comet":
        bot.send_message(call.message.chat.id, car_Comet)
    elif call.data == "sanchez":
        bot.send_message(call.message.chat.id, car_sanchez)
    elif call.data == "Rapid_GT":
        bot.send_message(call.message.chat.id, car_Rapid_GT)
    elif call.data == "Sportbike":
        bot.send_message(call.message.chat.id, car_PKJ)
    elif call.data == "Better_Dominic":
        bot.send_message(call.message.chat.id, car_Better_Dominic)

@bot.callback_query_handler(func=lambda call: call.data in ["drunkard", "gravity", "fast run", "invulnerability", "super_jump"])
def submenu_callback_query(call):
    if call.data == "drunkard":
        bot.send_message(call.message.chat.id, skills_drunkard)
    elif call.data == "gravity":
        bot.send_message(call.message.chat.id, skills_gravity)
    elif call.data == "fast run":
        bot.send_message(call.message.chat.id, skills_fastrun)
    elif call.data == "invulnerability":
        bot.send_message(call.message.chat.id, skills_invulnerability)
    elif call.data == "super_jump":
        bot.send_message(call.message.chat.id, skills_superjump)

@bot.callback_query_handler(func=lambda call: call.data in ["Sliding_cars", "rainy_weather"])
def submenu_callback_query(call):
    if call.data == "Sliding_cars":
        bot.send_message(call.message.chat.id, weather_Sliding)
    elif call.data == "rainy_weather":
        bot.send_message(call.message.chat.id, weather_rainy)

@bot.callback_query_handler(func=lambda call: call.data in ["PoliceM", "PoliceP", "SlowTime"])
def submenu_callback_query(call):
    if call.data == "PoliceM":
        bot.send_message(call.message.chat.id, other_PoliceM)
    elif call.data == "PoliceP":
        bot.send_message(call.message.chat.id, other_PoliceP)
    elif call.data == "SlowTime":
        bot.send_message(call.message.chat.id, other_SlowTime)

# First menu action
def first(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup_Guns())
def second(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup_Cars())
def third(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup_Skills())
def fourd(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup_Weather())
def fiveth(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup_Other())
bot.infinity_polling()


