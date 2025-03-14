import telebot

from config import APItoken

bot = telebot.TeleBot(APItoken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Вас приветствует бот Decay timer! Он создан для того чтобы помогать людям узнать про время разложения разных отходов в природе!\nИспользуйте /help чтобы посмотреть список команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Список команд:\n /food - пищевые отходы\n /paper - бумага\n /wood - дерево\n /metal - металл\n /batery - батерейки и аккумуляторы\n /tires - покрышки\n /plastic - пластик\n /poly - полиэтилен\n /glass - стекло")
	
@bot.message_handler(commands=['food'])
def send_food(message):
	bot.reply_to(message, "🍕Пищевые отходы разлагются в природе до 1 месяца🍕\nУровень загрязнения: ♻️минимальный♻️")

@bot.message_handler(commands=['paper'])
def send_paper(message):
	bot.reply_to(message, "📄Бумага разлагется в природе от 1 до 3 лет📄\nУровень загрязнения: ❇️низкий❇️")
	
@bot.message_handler(commands=['wood'])
def send_wood(message):
	bot.reply_to(message, "🪵Дерево разлагется в природе от 1 до 10 лет🪵\nУровень загрязнения: ♻️минимальный♻️")
	
@bot.message_handler(commands=['metal'])
def send_metal(message):
	bot.reply_to(message, "🦾Металл разлагется в природе до 10 лет🦿\nУровень загрязнения: ❗средний❗")
	
@bot.message_handler(commands=['batery'])
def send_batery(message):
	bot.reply_to(message, "🔋Батареи и аккумуляторы разлагются в природе до 100 лет🪫\nУровень загрязнения: ☣️критический☣️")
	
@bot.message_handler(commands=['tires'])
def send_tires(message):
	bot.reply_to(message, "🛞Покрышки разлагются в природе до 100 лет🛞\nУровень загрязнения: ⚠️высокий⚠️")
	
@bot.message_handler(commands=['plastic'])
def send_plastic(message):
	bot.reply_to(message, "🛍️Пластик разлагются в природе более 100 лет🛍️\nУровень загрязнения: ☣️критический☣️")
	
@bot.message_handler(commands=['poly'])
def send_poly(message):
    bot.reply_to(message, "🛍️Полиэтилен разлагется в природе до 200 лет🛍️\nУровень загрязнения: ☣️критический☣️")

@bot.message_handler(commands=['glass'])
def send_glass(message):
	bot.reply_to(message, "🍷Стекло разлагется в природе более 1000 лет🍷\nУровень загрязнения: ⚠️высокий⚠️")

bot.infinity_polling()