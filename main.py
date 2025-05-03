from telebot.types import Message
from telebot import TeleBot
import telebot
import random

bot = telebot.TeleBot("")


@bot.message_handler(commands=["start"])
def start_cmd(message: Message):
    bot.send_message(message.chat.id, "Привет! Я экобот. Нажми /about чтобы узнать больше информации о боте ")


@bot.message_handler(commands=["about"])
def about_cmd(message: Message):
    text = ('Привет! Я Эко-Бот. Я помогу тебе заботиться об окружающей среде.\n\nНапиши /tips - советы \nНапиши /facts - интересные факты \nНапиши /decompose - показывает время разложения разных видов мусора \nНапиши /recycle – как сортировать мусор')
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(commands=["tips"])
def tips(message):
    tips_list = [
        " Выключай воду, пока чистишь зубы — можно сэкономить до 6 литров за минуту.",
        " Ходи в магазин со своей сумкой, а не бери пакеты.",
        " Не оставляй зарядки в розетке — они продолжают тратить электроэнергию!",
        " Ходи пешком или езди на велосипеде — это полезно и для здоровья, и для планеты.",
        " Сортируй отходы — это увеличивает шанс повторной переработки."
    ]
    bot.send_message(message.chat.id, random.choice(tips_list))


@bot.message_handler(commands=["recycle"])
def recycle(message):
    text = (" Как сортировать мусор:\n\n"
            " Бумага – газеты, коробки\n"
            " Стекло – бутылки, банки\n"
            " Пластик – упаковки, бутылки\n"
            " Металл – банки от напитков\n"
            " Остальное – в обычный мусор")
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["facts"])
def facts(message):
    facts_list = [
        " Каждый год в океан попадает более 8 миллионов тонн пластика.",
        " Переработка одной алюминиевой банки экономит энергию, достаточную для работы телевизора 3 часа.",
        " Одно дерево может поглотить до 22 кг CO₂ в год.",
        " До 70% питьевой воды используется на сельское хозяйство.",
        " Человек в среднем производит более 400 кг мусора в год."
    ]
    bot.send_message(message.chat.id, random.choice(facts_list))

@bot.message_handler(commands=["decompose"])
def decompose(message):
    decompose_text = (
        " <b>Сколько разлагается мусор:</b>\n\n"
        " Пластиковая бутылка — <i>450 лет</i>\n"
        " Пластиковый пакет — <i>100–200 лет</i>\n"
        " Банановая кожура — <i>2–5 недель</i>\n"
        " Бумага — <i>2 месяца</i>\n"
        " Алюминиевая банка — <i>200–500 лет</i>\n"
        " Одежда из синтетики — <i>до 40 лет</i>\n"
        " Стекло — <i>4000+ лет</i> (почти не разлагается)\n"
        " Окурок сигареты — <i>10–12 лет</i>\n"
        " Дерево — <i>10–15 лет</i>\n"
        " Картон — <i>1–2 месяца</i>\n"
    )
    bot.send_message(message.chat.id, decompose_text, parse_mode='HTML')



bot.infinity_polling()
