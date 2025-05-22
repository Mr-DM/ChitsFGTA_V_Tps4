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
            InlineKeyboardButton("персонажей 👦", callback_data="skins"))

    markup.add(InlineKeyboardButton("погоду 🌧️", callback_data="weather"),
            InlineKeyboardButton("другое 🛸", callback_data="other"))

    return markup



def gen_markup_1():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Всё оружие", callback_data="Allguns"),
            InlineKeyboardButton("Взрывные атаки ближнего боя", callback_data="BoomAttack"),)
    markup.add(InlineKeyboardButton("Взрывные патроны", callback_data="BoomPatrons"),
            InlineKeyboardButton("Поджигающие пули ", callback_data="FirePatrons"),)
    
    return markup

def gen_markup_2():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Вызов comet", callback_data="comet"),
            InlineKeyboardButton("мотоцикл для бездорожья", callback_data="sanchez"),
            InlineKeyboardButton("Спроткар", callback_data="Rapid_GT"))
    markup.add(InlineKeyboardButton("спортивный мотоцикл", callback_data=" ПКJ-600"),
            InlineKeyboardButton("маслкар", callback_data="Duke O’Death Car"))
    
    return markup

def gen_markup_3():

    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("🥟 Баоцзы", callback_data="cb_baozzi"),
            InlineKeyboardButton("🥟 Кундюмы ", callback_data="cb_koondymy"),
            InlineKeyboardButton("🥟 Курзе ", callback_data="cb_koorze"))
    markup.add(InlineKeyboardButton("🥟 Бораки ", callback_data="cb_boraki"),
            InlineKeyboardButton("🥟 Равиоли", callback_data="cb_ravioli"))
    
    return markup

def gen_markup_4():
    
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("🥟 Подкогыльо", callback_data="cb_podkogylyo"),
            InlineKeyboardButton("🥟 Чучвара ", callback_data="cb_choochvara"),
            InlineKeyboardButton("🥟 Дюшбара ", callback_data="cb_dyshbara"))
    markup.add(InlineKeyboardButton("🥟 Креплах ", callback_data="cb_kreplah"),
            InlineKeyboardButton("🥟 Манду", callback_data="cb_mandoo"))
    
    return markup

def gen_markup_5():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Понизить уровень розыска", callback_data="PoliceM"),
               InlineKeyboardButton("Увеличить уровень розыска", callback_data="PoliceP"),)
    markup.add(InlineKeyboardButton("Замедленное время", callback_data="SlowTime"),)


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
@bot.callback_query_handler(func=lambda call: call.data in ["cb_Pelmeni", "cb_Vareniki", "cb_Hinkali", "cb_Manti", "cb_Buuz"])
def submenu_callback_query(call):
    if call.data == "cb_Pelmeni":
            bot.send_photo(call.message.chat.id, open('img/pelmeni.jpg', 'rb'), text_pelmeni)
    elif call.data == "cb_Vareniki":
        bot.send_photo(call.message.chat.id, open('img/vareniki.jpg', 'rb'), text_vareniki)
    elif call.data == "cb_Hinkali":
        bot.send_photo(call.message.chat.id, open('img/Hinkali.jpg', 'rb'), text_hinkali)
    elif call.data == "cb_Manti":
        bot.send_photo(call.message.chat.id, open('img/Manti.jpg', 'rb'), text_mantu)
    elif call.data == "cb_Buuz":
        bot.send_photo(call.message.chat.id, open('img/Buzz.jpg', 'rb'), text_buuz)

@bot.callback_query_handler(func=lambda call: call.data in ["cb_szaosz","cb_gedza" , "cb_dimSams", "cb_momo", "cb_votons"])
def submenu_callback_query(call):
    if call.data == "cb_szaosz":
        bot.send_photo(call.message.chat.id, open('img/szasz.jpg', 'rb'), text_szaosz)
    elif call.data == "cb_gedza":
        bot.send_photo(call.message.chat.id, open('img/gedza.jpg', 'rb'), text_gedza)
    elif call.data == "cb_dimSams":
        bot.send_photo(call.message.chat.id, open('img/dimSams.jpg', 'rb'), text_dimSams)
    elif call.data == "cb_momo":
        bot.send_photo(call.message.chat.id, open('img/momo.jpg', 'rb'), text_momo)
    elif call.data == "cb_votons":
        bot.send_photo(call.message.chat.id, open('img/votons.jpg', 'rb'), text_votons)

@bot.callback_query_handler(func=lambda call: call.data in ["cb_baozzi", "cb_koondymy", "cb_koorze", "cb_boraki", "cb_ravioli"])
def submenu_callback_query(call):
    if call.data == "cb_baozzi":
        bot.send_photo(call.message.chat.id, open('img/baozzi.jpg', 'rb'), text_baozzi)
    elif call.data == "cb_koondymy":
        bot.send_photo(call.message.chat.id, open('img/koondymy.jpg', 'rb'), text_koondymy)
    elif call.data == "cb_koorze":
        bot.send_photo(call.message.chat.id, open('img/koorze.jpg', 'rb'), text_koorze)
    elif call.data == "cb_boraki":
        bot.send_photo(call.message.chat.id, open('img/boraki.jpg', 'rb'), text_boraki)
    elif call.data == "cb_ravioli":
        bot.send_photo(call.message.chat.id, open('img/ravioli.jpg', 'rb'), text_ravioli)

@bot.callback_query_handler(func=lambda call: call.data in ["cb_podkogylyo", "cb_choochvara", "cb_dyshbara", "cb_kreplah", "cb_mandoo"])
def submenu_callback_query(call):
    if call.data == "cb_podkogylyo":
        bot.send_photo(call.message.chat.id, open("img/podkogylyo.jpg", "rb"), text_podkogylyo)
    elif call.data == "cb_choochvara":
        bot.send_photo(call.message.chat.id, open("img/choochvara.jpg", "rb"), text_choochvara)
    elif call.data == "cb_dyshbara":
        bot.send_photo(call.message.chat.id, open("img/dyshbara.jpg", "rb"), text_dyshbara )
    elif call.data == "cb_kreplah":
        bot.send_photo(call.message.chat.id, open("img/kreplah.jpg", "rb"), text_kreplah)
    elif call.data == "cb_mandoo":
        bot.send_photo(call.message.chat.id, open("img/mandoo.jpg", "rb"), text_mandoo)
        

# First menu action
def first(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_1())

def second(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_2())

def third(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_3())
def fourd(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_4())
def fiveth(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_5())
bot.infinity_polling()


