from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

next1_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Чем мне это будет полезно?", callback_data="next_1")
        ],
    ]
)

next2_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дальше", callback_data="next_2")
        ],
    ]
)

next3_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Техники, которые я использую на консультациях", callback_data="next_3")
        ],
    ]
)

next4_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дальше", callback_data="next_4")
        ],
    ]
)

next5_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Почему необходимо пройти глубокую профориентацию?", callback_data="next_5")
        ],
    ]
)

next6_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Что такое skills-ориентирование?", callback_data="video")
        ],
    ]
)

final_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выявить свои таланты, найти любимую работу"),
        ],
        [
            KeyboardButton(text="Найти удовлетворение в работе"),
        ],
        [
            KeyboardButton(text="Понять, в какие проекты инвестировать время и энергию"),
        ],
        [
            KeyboardButton(text="Выявить таланты ребёнка, подобрать секции/курсы"),
        ],
        [
            KeyboardButton(text="Определиться с колледжем/ВУЗом"),
        ],
    ]
)

go_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тарифы"),
            KeyboardButton(text="Отзывы")
        ],
        [
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Частые вопросы")
        ]
    ],
    resize_keyboard=True
)

questions_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Где и как проходят занятия?"),
        ],
        [
            KeyboardButton(text="Для какого возраста подходит профориентация подросткам?"),
        ],
        [
            KeyboardButton(text="Кто проводит профориентацию?"),
        ],
        [
            KeyboardButton(text="Нужно ли присутствовать родителю на профориентации для подростков?"),
        ],
        [
            KeyboardButton(text="Что мы получим в результате консультации?"),
        ],
        # [
        #     KeyboardButton(text="В чем заключается ваша методика?(дополнить)"),
        # ],
        [
            KeyboardButton(text="Назад к меню 🔙"),
        ],
    ],
    resize_keyboard=True
)
