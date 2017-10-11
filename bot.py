import telebot
import re
import Algorithmia
API_KEY = "426302909:AAEmSebWRENNIkHl7UCVl8XLQnCeC67cToE"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def strt(message):
    start="Hi, this is webnoid, i am a summarizer bot  made by Abhinay and Nanda,i take in a url as a input and i give out the summary of that website as an output "
    bot.reply_to(message,start)

@bot.message_handler(commands=['hi'])
def strt(message):
    name=input("Give me your name:")
    user="hi,there"+" "+name+"!"+" "+"give me the url i need to summarize,hit me with anything!"
    bot.reply_to(message,user)

@bot.message_handler(commands=['whatcanyoudo?'])
def strt(message):
    msg="i can summarize the website of any url you provide!,go on..feed me"
    bot.reply_to(message,msg)

@bot.message_handler(commands=['whomadeyou?'])
def strt(message):
    create="i was created by my creators Abhinay and Nanda:)"
    bot.reply_to(message,create)

@bot.message_handler(commands=['wherewereyouborn?'])
def strt(message):
    create="i was created at Hindustan University,:)"
    bot.reply_to(message,create)
@bot.message_handler(commands=['wherewereyoucreatedwith?'])
def strt(message):
    created="i was created on Telegram platform with tools like python and natural language processing"
    bot.reply_to(message,created)

@bot.message_handler(func=lambda message: True)
def blab(message):
    try:
        input = message.text
        client = Algorithmia.client('simpHSXyYyDC1HAzBafYSouCOwc1')
        if "://" in input and "https" in input:
            input = input.rsplit('://', 1)[1]
            assert not input == input.rsplit('/', 1)[1]
            input = "https://" + input
        elif "://" in input and "http" in input:
            input = input.rsplit('://', 1)[1]
            assert not input == input.rsplit('/', 1)[1]
            input = "http://" + input
        else:
            assert not input == input.rsplit('/', 1)[0]
        algo = client.algo('nlp/SummarizeURL/0.1.4')
        bot.reply_to(message, (algo.pipe(input)).result)
    except:
        bot.reply_to(message, "your link is not correct  or you have entered a base url...")


bot.polling()
