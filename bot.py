import json
import telebot

bot = telebot.TeleBot('6624432064:AAFRd9L4NBuTBSiqIaahsF0qYFSImCNETP4')
total_score = {'дружок': 0, 'роза': 0, 'малыш': 0, 'гена': 0, 'лиза': 0}

questions = {1:
                 ['Что ты предпочитаешь делать в свободное время?',
                  {"Петь": {"дружок": 0, "роза": 2, "малыш": 0, "гена": 0, "лиза": 5},
                   "Играть в футбол": {"дружок": 5, "роза": 0, "малыш": 0, "гена": 0, "лиза": 0},
                   "Прочитать книгу": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 5, "лиза": 1},
                   "Разговаривать по телефону": {"дружок": 0, "роза": 5, "малыш": 0, "гена": 0, "лиза": 2},
                   "Играть в игрушки": {"дружок": 1, "роза": 0, "малыш": 5, "гена": 0, "лиза": 1}
                   }
                  ],
             2:
                 ['Какая порода собак тебе нравится больше всего?',
                  {"Чихуахуа": {"дружок": 0, "роза": 0, "малыш": 5, "гена": 0, "лиза": 0},
                   "Ирландский сеттер": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 0, "лиза": 5},
                   "Джек рассел терьер": {"дружок": 5, "роза": 0, "малыш": 0, "гена": 0, "лиза": 0},
                   "Китайская хохлатая": {"дружок": 0, "роза": 5, "малыш": 0, "гена": 0, "лиза": 0},
                   "Английский бульдог": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 5, "лиза": 0}
                   }
                  ],
             3:
                 ["Как ты учишься?",
                  {"Только на пять": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 3, "лиза": 5},
                   "Всегда по разному": {"дружок": 1, "роза": 5, "малыш": 0, "гена": 0, "лиза": 0},
                   "В основном два и три": {"дружок": 5, "роза": 1, "малыш": 0, "гена": 0, "лиза": 0}
                   }
                  ],
             4:
                 ["Что из этого тебе не нравится?",
                  {"Учеба": {"дружок": 5, "роза": 2, "малыш": 0, "гена": 0, "лиза": 0},
                   "Когда со мной не играют": {"дружок": 3, "роза": 0, "малыш": 5, "гена": 0, "лиза": 0},
                   "Когда мне мешают": {"дружок": 0, "роза": 5, "малыш": 0, "гена": 3, "лиза": 0},
                   "Когда меня не слушают": {"дружок": 0, "роза": 1, "малыш": 2, "гена": 5, "лиза": 1}
                   }
                  ],
             5:
                 ["Какой у тебя характер?",
                  {"Спокойный, рассудительный, умный": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 5, "лиза": 1},
                   "Заботливый, мечтательный и послушный": {"дружок": 0, "роза": 5, "малыш": 1, "гена": 0, "лиза": 0},
                   "Творческий, эгоистичный, ответственный": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 0, "лиза": 5},
                   "Жизнерадостный, любознательный, наивный": {"дружок": 1, "роза": 0, "малыш": 5, "гена": 0, "лиза": 0},
                   "Весёлый, импульсивный, активный": {"дружок": 5, "роза": 0, "малыш": 0, "гена": 0, "лиза": 0}
                   }
                  ],
             6:
                 ["Что для тебя важнее всего?",
                  {"Знания": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 5, "лиза": 3},
                   "Красота": {"дружок": 0, "роза": 5, "малыш": 0, "гена": 0, "лиза": 0},
                   "Игрушки": {"дружок": 2, "роза": 0, "малыш": 5, "гена": 0, "лиза": 5},
                   "Популярность": {"дружок": 0, "роза": 3, "малыш": 0, "гена": 0, "лиза": 5},
                   "Общение, друзья": {"дружок": 5, "роза": 0, "малыш": 0, "гена": 0, "лиза": 0}
                   }
                  ],
             7:
                 ["Какая мечта тебе ближе всего?",
                  {"Быть самой красивой": {"дружок": 0, "роза": 5, "малыш": 0, "гена": 0, "лиза": 3},
                   "Получить Нобелевскую премию": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 5, "лиза": 0},
                   "Дрессированная пчела и полёт в космос.": {"дружок": 0, "роза": 0, "малыш": 5, "гена": 0, "лиза": 0},
                   "Стать актрисой": {"дружок": 0, "роза": 0, "малыш": 0, "гена": 0, "лиза": 5},
                   "Выиграть межгалактический турнир по футболу": {"дружок": 5, "роза": 0, "малыш": 0, "гена": 0, "лиза": 0}
                   }
                  ]
             }


# функция для сохранения прогресса пользователя в JSON файл
def save_progress(user_id, question_number):
    progress = {str(user_id): question_number}
    with open('progress.json', 'w') as file:
        json.dump(progress, file)


# функция для загрузки прогресса пользователя из JSON файла
def load_progress(user_id):
    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)
            return progress.get(str(user_id))
    except FileNotFoundError:
        return None


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Чтобы запустить тест пропиши команду /star_test")


@bot.message_handler(commands=['start_test'])
def handle_start_test(message):
    save_progress(message.chat.id, 1)  # сбросить прогресс пользователя
    bot.send_message(message.chat.id, "Тест состоит из 7 вопросов. Начинаем!")
    show_question(message.chat.id, 1)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n/start - запуск анкеты\n/help - помощь\n/start_test - "
                                      "запуск теста")


# функция для отображения вопроса и вариантов ответа
def show_question(chat_id, question_number):
    global questions
    question_text = questions[question_number][0]  # текст вопроса
    options = questions[question_number][1]  # список вариантов ответа

    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        keyboard.add(telebot.types.KeyboardButton(option))

    bot.send_message(chat_id, question_text, reply_markup=keyboard)


# функция для обработки ответа пользователя
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global total_score
    user_id = message.chat.id
    progress = load_progress(user_id)
    try:
        if progress is not None:
            # обработать ответ пользователя и перейти к следующему вопросу или вывести результат
            if progress < 7:
                for name, scores in questions[progress][1][message.text].items():
                    total_score[name] += scores
                save_progress(user_id,
                              progress + 1)
                show_question(user_id, progress + 1)
            else:  # если последний вопрос
                # вывести результат анкетирования
                bot.send_message(user_id, 'Итоги анкеты!!!')
                max_score = 0
                your_name = ''
                for name, scores in total_score.items():
                    if scores > max_score:
                        max_score = scores
                        your_name = name
                bot.send_message(user_id, f'Поздравляю, вы: {your_name}')
                if your_name == 'дружок':
                    photo = open('dryzok.png', 'rb')
                elif your_name == 'роза':
                    photo = open('roza.jpg', 'rb')
                elif your_name == 'малыш':
                    photo = open('maleysh.jpg', 'rb')
                elif your_name == 'гена':
                    photo = open('gena.png', 'rb')
                elif your_name == 'лиза':
                    photo = open('liza.jpg', 'rb')
                bot.send_photo(user_id, photo)
                save_progress(user_id, 1)  # сбросить прогресс пользователя
        else:
            bot.send_message(user_id, "Чтобы начать анкету, воспользуйтесь командой /start_test.")
    except Exception as e:
        bot.send_message(message.chat.id,
                         'Чтобы пройти тест еще раз, напишите /start_test')


bot.polling()
