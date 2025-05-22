import telebot
from text import *
from config import Token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(Token)

# --- Menu Generators ---

def gen_markup():
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton("оружие и патроны 🔫", callback_data="gun"),
        InlineKeyboardButton("транспорт и перемещение 🚘", callback_data="cars"),
        InlineKeyboardButton("персонажей 👦", callback_data="Skills")
    )
    markup.add(
        InlineKeyboardButton("погоду 🌧️", callback_data="weather"),
        InlineKeyboardButton("другое 🛸", callback_data="other")
    )
    return markup

def gen_markup_Guns():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Всё оружие", callback_data="Allguns"),
        InlineKeyboardButton("Взрывные атаки ближнего боя", callback_data="BoomAttack"),
        InlineKeyboardButton("Взрывные патроны", callback_data="BoomPatrons"),
        InlineKeyboardButton("Поджигающие пули ", callback_data="FirePatrons")
    )
    return markup

def gen_markup_Cars():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Вызов comet", callback_data="comet"),
        InlineKeyboardButton("мотоцикл для бездорожья", callback_data="sanchez"),
        InlineKeyboardButton("Спроткар", callback_data="Rapid_GT"),
        InlineKeyboardButton("спортивный мотоцикл", callback_data="Sportbike"),
        InlineKeyboardButton("маслкар", callback_data="Better_Dominic")
    )
    return markup

def gen_markup_Skills():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Режим пьяницы", callback_data="drunkard"),
        InlineKeyboardButton("Лунная гравитация", callback_data="gravity"),
        InlineKeyboardButton("Быстрый бег", callback_data="fast_run"),
        InlineKeyboardButton("Неуязвимость", callback_data="invulnerability"),
        InlineKeyboardButton("Суперпрыжок", callback_data="super_jump")
    )
    return markup

def gen_markup_Weather():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Скользящие машины", callback_data="Sliding_cars"),
        InlineKeyboardButton("Дождливая погода", callback_data="rainy_weather")
    )
    return markup

def gen_markup_Other():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Понизить уровень розыска", callback_data="PoliceM"),
        InlineKeyboardButton("Увеличить уровень розыска", callback_data="PoliceP"),
        InlineKeyboardButton("Замедленное время", callback_data="SlowTime")
    )
    return markup

# --- Command Handlers ---

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, text_start)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список Читов", reply_markup=gen_markup())

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, text_info)

# --- Main Menu Callback Handler ---

@bot.callback_query_handler(func=lambda call: call.data in ["gun", "cars", "Skills", "weather", "other"])
def callback_query(call):
    if call.data == "gun":
        bot.send_message(call.message.chat.id, "Список Читов", reply_markup=gen_markup_Guns())
    elif call.data == "cars":
        bot.send_message(call.message.chat.id, "Список Читов", reply_markup=gen_markup_Cars())
    elif call.data == "Skills":
        bot.send_message(call.message.chat.id, "Список Читов", reply_markup=gen_markup_Skills())
    elif call.data == "weather":
        bot.send_message(call.message.chat.id, "Список Читов", reply_markup=gen_markup_Weather())
    elif call.data == "other":
        bot.send_message(call.message.chat.id, "Список Читов", reply_markup=gen_markup_Other())

# --- Guns Submenu ---

@bot.callback_query_handler(func=lambda call: call.data in ["Allguns", "BoomAttack", "BoomPatrons", "FirePatrons"])
def guns_callback(call):
    if call.data == "Allguns":
        bot.send_message(call.message.chat.id, gun_Allguns)
    elif call.data == "BoomAttack":
        bot.send_message(call.message.chat.id, gun_BoomAttack)
    elif call.data == "BoomPatrons":
        bot.send_message(call.message.chat.id, gun_BoomPatrons)
    elif call.data == "FirePatrons":
        bot.send_message(call.message.chat.id, gun_FirePatrons)

# --- Cars Submenu ---

@bot.callback_query_handler(func=lambda call: call.data in ["comet", "sanchez", "Rapid_GT", "Sportbike", "Better_Dominic"])
def cars_callback(call):
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

# --- Skills Submenu ---

@bot.callback_query_handler(func=lambda call: call.data in ["drunkard", "gravity", "fast_run", "invulnerability", "super_jump"])
def skills_callback(call):
    if call.data == "drunkard":
        bot.send_message(call.message.chat.id, skills_drunkard)
    elif call.data == "gravity":
        bot.send_message(call.message.chat.id, skills_gravity)
    elif call.data == "fast_run":
        bot.send_message(call.message.chat.id, skills_fastrun)
    elif call.data == "invulnerability":
        bot.send_message(call.message.chat.id, skills_invulnerability)
    elif call.data == "super_jump":
        bot.send_message(call.message.chat.id, skills_superjump)

# --- Weather Submenu ---

@bot.callback_query_handler(func=lambda call: call.data in ["Sliding_cars", "rainy_weather"])
def weather_callback(call):
    if call.data == "Sliding_cars":
        bot.send_message(call.message.chat.id, weather_Sliding)
    elif call.data == "rainy_weather":
        bot.send_message(call.message.chat.id, weather_rainy)

# --- Other Submenu ---

@bot.callback_query_handler(func=lambda call: call.data in ["PoliceM", "PoliceP", "SlowTime"])
def other_callback(call):
    if call.data == "PoliceM":
        bot.send_message(call.message.chat.id, other_PoliceM)
    elif call.data == "PoliceP":
        bot.send_message(call.message.chat.id, other_PoliceP)
    elif call.data == "SlowTime":
        bot.send_message(call.message.chat.id, other_SlowTime)

# --- Run Bot ---
bot.infinity_polling()
