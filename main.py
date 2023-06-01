import telebot
import datetime

# Словник з відповідностями англійських назв днів тижня до українських
days_of_week = {
    'Monday': 'Понеділок',
    'Tuesday': 'Вівторок',
    'Wednesday': 'Середа',
    'Thursday': 'Четвер',
    'Friday': "П'ятниця",
    'Saturday': 'Субота',
    'Sunday': 'Неділя'
}


#@P33botbot
bot = telebot.TeleBot('6098126284:AAGkdJt9BGoIkUbBvvp6Mqysuj0ZAmzxd_A')

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, f'Привіт <b>{message.from_user.first_name} {message.from_user.last_name}</b>, ось'
                                      f' довідник по Python.\n'
                                      'Список команд:'
                                      '\n <b>Перша ДЗ по боту:</b>' 
                                      '\n/while'
                                      '\n/def'
                                      '\n/try'
                                      '\n/break'
                                      '\n/await'
                                      '\n/for'
                                      '\n/import'
                                      '\n/if'
                                      '\n/and'
                                      '\n/del'
                                      '\n/return'
                                      '\n<b>Друга дз по боту, відправка Файлів на текст і дія з часом:</b>'
                                      '\n/<b>list</b>'
                                      '\n<b>/time</b>'
                                      '\n<b>Особисті команди:</b>'
                                      '\n<b>#/calculator</b>', parse_mode='html')


@bot.message_handler(commands=['while'])
def while_1(message):
    text = 'while Цикл Python використовує ключове слово while і працює як while цикл в інших мовах програмування. ' \
           'Поки умова, яка слідує за while ключовим словом, відповідає дійсності, блок, наступний за while оператором,' \
           ' продовжуватиме виконуватися знову і знову.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['def'])
def def_1(message):
    text = 'Ключове слово Python def використовується для визначення функції або методу класу. Це еквівалентно function' \
           ' JavaScript і PHP. Основний синтаксис для визначення функції defвиглядає так: \ndef <function>(<params>):' \
           '\n\t\t\t\t\t<body>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['try'])
def try_1(message):
    text = 'Будь-який блок обробки винятків починається з ключового слова Python try. Це те ж саме в більшості інших ' \
           'мов програмування, які мають обробку винятків. Код у try блоці – це код, який може викликати виключення.' \
           ' Кілька інших ключових слів Python пов’язані з try і використовуються для визначення того, що слід робити,' \
           ' якщо виникають різні винятки або в різних ситуаціях.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['break'])
def break_1(message):
    text = 'Ключове break слово. Якщо вам потрібно вийти з циклу раніше, ви можете використати break ключове слово. ' \
           'Це ключове слово працюватиме в обох циклах for і while'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['await'])
def await_1(message):
    text = 'Ключове слово Python await використовується в асинхронних функціях, щоб визначити точку у функції, де' \
           ' керування повертається циклу подій для виконання інших функцій. Ви можете використовувати його, ' \
           'розмістивши await ключове слово перед викликом будь-якої async функції'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['for'])
def for_1(message):
    text = 'Найбільш поширеним циклом у Python є for цикл. Він створений шляхом поєднання ключових слів Python for і' \
           ' in пояснений раніше. Основний синтаксис циклу for такий: \nfor <element> in <container>:' \
           ' \n\t\t\t\t\t<statements>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['import'])
def import_1(message):
    text = 'Ключове слово Python import використовується для імпорту або включення модуля для використання у вашій' \
           ' програмі Python. Основний синтаксис використання виглядає так: \nimport <module>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['if'])
def if_1(message):
    text = 'Ключове if слово використовується для початку умовного оператора . Інструкція if дозволяє вам написати блок' \
           ' коду, який буде виконано, лише якщо вираз після if є правдивим. Синтаксис оператора if починається з' \
           ' ключового слова if на початку рядка, за яким слідує дійсний вираз, значення якого буде оцінено на його' \
           ' правдивість'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['and'])
def and_1(message):
    text = 'Ключове слово Python and використовується, щоб визначити, чи лівий, і правий операнди правдиві чи хибні. ' \
           'Якщо обидва операнди правдиві, то результат буде правдивим. Якщо один хибний, то результат буде хибним'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['del'])
def del_1(message):
    text = 'del використовується в Python для скасування змінної або імені. Ви можете використовувати його для імен ' \
           'змінних, але більш поширеним є видалення індексів зі списку або словника . Щоб скасувати змінну, ' \
           'використовуйте, del а потім змінну, яку потрібно скасувати'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['return'])
def return_1(message):
    text = 'Ключове слово Python return дійсне лише як частина функції, визначеної за допомогою def. Коли Python' \
           ' зустрічає це ключове слово, він вийде з функції в цей момент і поверне результати того, що йде після' \
           ' ключового return слова'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['list'])
def list(message):
    bot.send_message(message.chat.id, 'Список текстових команд по html файлам новини Python:' \
           '\n<u><b>april_2022</b></u>' \
           '\n<u><b>april_2023</b></u>' \
           '\n<u><b>august_2022</b></u>' \
           '\n<u><b>february_2022</b></u>' \
           '\n<u><b>february_2023</b></u>' \
           '\n<u><b>january_2022</b></u>' \
           '\n<u><b>january_2023</b></u>' \
           '\n<u><b>july_2022</b></u>' \
           '\n<u><b>june_2022</b></u>' \
           '\n<u><b>march_2022</b></u>' \
           '\n<u><b>march_2023</b></u>' \
           '\n<u><b>may_2022</b></u>' \
           '\n<u><b>november_2022</b></u>' \
           '\n<u><b>october_2022</b></u>' \
           '\n<u><b>september_2022</b></u>', parse_mode='html')

@bot.message_handler(commands=['time'])
def time(message):
    bot.send_message(message.chat.id, 'Список текстових команд часу та дати:' \
           '\n<u><b>дата</b></u> - Отримати поточну дату' \
           '\n<u><b>час</b></u> - Дізнатися поточний час' \
           '\n<u><b>день тижня</b></u> - Дізнатися день тижня' \
           '\n<u><b>залишилось</b></u> - Розрахувати кількість днів до вказаної дати' \
           '\n<u><b>розрахувати дату</b></u> - Розрахувати дату через певну кількість днів' \
           '\n<u><b>годино дні</b></u> - Перевести години в дні', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'і тобі привіт')
    elif message.text == 'python':
        bot.send_message(message.chat.id, 'о ти вивчаєш пайтон')
    elif message.text == 'python logo':
        photo = open('python.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'cod':
        doc = open('1.docx', 'rb')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'april_2022':
        doc = open('april_2022.html', 'r', encoding='utf-8')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'april_2023':
        doc = open('april_2023.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'august_2022':
        doc = open('august_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'february_2022':
        doc = open('february_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'february_2023':
        doc = open('february_2023.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'january_2022':
        doc = open('january_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'january_2023':
        doc = open('january_2023.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'july_2022':
        doc = open('july_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'june_2022':
        doc = open('june_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'march_2022':
        doc = open('march_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'march_2023':
        doc = open('march_2023.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'may_2022':
        doc = open('may_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'november_2022':
        doc = open('november_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'october_2022':
        doc = open('october_2022.html', 'r')
        bot.send_document(message.chat.id, doc)

    elif message.text == 'september_2022':
        doc = open('september_2022.html', 'r')
        bot.send_document(message.chat.id, doc)


    elif message.text.lower() == 'дата':
        date_now = datetime.date.today()
        bot.send_message(message.chat.id, date_now)

    elif message.text.lower() == 'день тижня':
        date_now = datetime.date.today().strftime("%A")
        ukr_day = days_of_week.get(date_now)
        bot.send_message(message.chat.id, ukr_day)

    elif message.text.lower() == 'час':
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.chat.id, time_now)

    elif message.text.lower() == 'залишилось':
        bot.send_message(message.chat.id, 'Введіть дату у форматі РРРР-ММ-ДД:')
        bot.register_next_step_handler(message, get_user_date)

    elif message.text.lower() == 'розрахувати дату':
        bot.send_message(message.chat.id, 'Введіть кількість днів:')
        bot.register_next_step_handler(message, calculate_date)

    elif message.text.lower() == 'годино дні':
        bot.send_message(message.chat.id, 'Введіть кількість годин:')
        bot.register_next_step_handler(message, calculate_date1)

    else:
        bot.send_message(message.chat.id, 'Я тебе не розумію')

def get_user_date(message):
    try:
        user_date = datetime.datetime.strptime(message.text, "%Y-%m-%d").date()
        today = datetime.date.today()
        diff = user_date - today
        bot.send_message(message.chat.id, f"До <b>{user_date}</b> залишилось: <b>{diff.days}</b> днів", parse_mode='html')
    except ValueError:
        bot.send_message(message.chat.id,
                             'Некоректний формат дати. Введіть ще раз "залишилось" і дату у форматі РРРР-ММ-ДД.')

def calculate_date(message):
    try:
        days = int(message.text)
        today = datetime.date.today()
        calculated_date = today + datetime.timedelta(days=days)
        bot.send_message(message.chat.id, f"Дата через <b>{days}</b> днів: <b>{calculated_date}</b>", parse_mode='html')
    except ValueError:
        bot.send_message(message.chat.id, 'Некоректне значення кількості днів. Введіть ціле число.')

def calculate_date1(message):
    try:
        days = int(message.text)
        calculated_date1 = round(days/24, 2)
        bot.send_message(message.chat.id, f"<b>{days}</b> годин це: <b>{calculated_date1}</b> днів", parse_mode='html')
    except ValueError:
        bot.send_message(message.chat.id, 'Некоректне значення кількості днів. Введіть ціле число.')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Класна фото')

bot.polling(none_stop=True)

