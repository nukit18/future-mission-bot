from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data import config
from keyboards.inline.keyboards import next1_keyboard, next2_keyboard, next3_keyboard, next4_keyboard, \
    next5_keyboard, next6_keyboard, go_menu_keyboard, final_keyboard
from loader import dp, bot


class Form(StatesGroup):
    question = State()
    name = State()
    phone = State()
    mail = State()


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет, меня зовут Марина Илаловна. Я - Профориентолог, ТАЛАНТориентолог, "
                         "карьерный консультант, создатель первой онлайн-платформы skills-ориентирования «Миссия будущего»",
                         reply_markup=next1_keyboard)


@dp.callback_query_handler(text="next_1")
async def next1(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id, "Я смогу найти дело жизни для вас или вашего ребенка всего за 3 часа. "
                                    "Вам не придется заполнять никаких предварительных анкет или тестов. "
                                    "Вы просто приходите на консультацию, я диагностирую ваши таланты и показываю все возможности их "
                                    "применения на реальном рынке.В результате вы получаете план вашей реализации на ближайшие "
                                    "несколько лет, чтобы работать с удовольствием и получать за это достойное вознаграждение.",
                           reply_markup=next2_keyboard)


@dp.callback_query_handler(text="next_2")
async def next2(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id, "Немного обо мне:\n"
                                    "Карьерный консультант, профориентолог, ТАЛАНТориентолог, автор методики выявления природных талантов и "
                                    "создатель первого Центра skills-ориентирования 'Миссия будущего'\n"
                                    "Более 17 лет работы в сфере рекрутмента и управления HR-службами\n"
                                    "Психологическое, экономическое и бизнес-образование\n"
                                    "Проходила стажировки в Швейцарии, Германии и Франции по управлению бизнесом\n"
                                    "Занимаю должность старшего преподавателя в рейтинговом ВУЗе.\n"
                                    "Спикер технопарка “Сколково”",
                           reply_markup=next3_keyboard)


@dp.callback_query_handler(text="next_3")
async def next3(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "На консультациях я использую собственную методику по выявлению талантов и природных soft-skills.\n"
                           "Специальные вопросы и интерактивные задания помогают диагностировать ваши сильные стороны и понять, как ваши таланты проявляются в повседневных действиях.\n"
                           "Эта методика позволяет подойти к выбору профессии как способу реализации ВАШИХ дарований, и не зависеть от стремительно меняющихся рыночных условий.\n"
                           "Профессии появляются и исчезают, а таланты остаются с вами на всю жизнь. На них и стоит основывать свою карьеру! И я с радостью вам в этом помогу.\n",
                           reply_markup=next4_keyboard)


@dp.callback_query_handler(text="next_4")
async def next4(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    photo1 = open('data/Screenshot_1.jpg', 'rb')
    photo2 = open('data/Screenshot_2.jpg', 'rb')
    await bot.send_photo(user_id, photo=photo1)
    await bot.send_photo(user_id, caption="Наша миссия - это...", photo=photo2, reply_markup=next5_keyboard)


@dp.callback_query_handler(text="next_5")
async def next5(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "1) Меньше 27% россиян работают по своей специальности ВУЗа. Остальные потратили время и деньги зря"
                           "\n2) Больше 70% школьников не знают своих талантов, не понимают в какой профессии они будут успешны"
                           "\n3) 83% людей не получают удовольствие от своей работы и заставляют себя ходить на нее из-за денег"
                           "\n4) Больше 54% людей сталкивались с проблемой выгорания и необходимостью искать новую сферу"
                           "\n5) Больше 20% профессий становятся неактуальными каждые 5-7 лет, оставшиеся видоизменяются",
                           reply_markup=next6_keyboard)


@dp.callback_query_handler(text_contains="video")
async def video(call: types.CallbackQuery, state: FSMContext):
    await Form.question.set()
    await call.message.edit_reply_markup()
    user_id = call.from_user.id
    await bot.send_message(user_id,
                           "Посмотрите короткое видео о нас и узнайте подробнее зачем нужно глубокое skills-ориентирование в современном мире"
                           " \nhttps://www.youtube.com/watch?v=VbzqAek2p2A")
    await bot.send_message(user_id, "Какую задачу вы хотите решить с помощью консультации?", reply_markup=final_keyboard)


@dp.message_handler(content_types=['text'], state=Form.question)
async def form_question(message: types.Message, state: FSMContext):
    await message.answer("Хорошо, назовите, пожалуйста, свое имя")
    async with state.proxy() as data:
        data['question'] = message.text
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.name)
async def form_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Напишите номер телефона")
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.phone)
async def form_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer("Напишите, пожалуйста, вашу электронную почту")
    await Form.next()


@dp.message_handler(content_types=['text'], state=Form.mail)
async def form_mail(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        admin_id = config.ADMINS[0]
        data['mail'] = message.text
        msg = ("Получена новая заявка"
               + "\nИмя: " + data['name']
               + "\nНомер телефона: " + data['phone']
               + "\nПочта: " + data['mail']
               + "\nВопрос: " + data['question']
               )
        await bot.send_message(admin_id, msg)

    await message.answer("Спасибо, ваша заявка была отправлена, а пока можете ознакомиться со всем более подробно", reply_markup=go_menu_keyboard)
    await state.finish()
