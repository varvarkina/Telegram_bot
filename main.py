import asyncio
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

keyboard_remove = types.ReplyKeyboardRemove()

available_decision_answer1 = ("культурные достопримечательности, история", "природные красоты", "красивая архитектура")
available_decision_answer2 = ("времяпровождение на свежем воздухе", "прогулки по городу",
                              "не люблю много ходить, предпочитаю пассивный отдых")
available_decision_answer3 = ("изучать историю своей страны, узнавать о жизни великих людей",
                              "я интересуюсь архитектурными стилями",
                              "я увлекаюсь геологическими и этимологическими сведениями о памятниках природы")
available_decision_answer4 = ("восхищаюсь скульптурными композициями", "увлекаюсь искусством и живописью",
                              "мне нравится любоваться живописными пейзажами")
available_decision_answer5 = ("полезный досуг, хочу узнать что-то новое, посмотреть на вещи, созданные людьми в различные времена",
                              "досуг для активного отдыха с семьей, компанией или уединение на природе",
                              "досуг для прогулок по городу, создания фотографий на фоне различных сооружений архитектуры")
available_decision_answer6 = ("1")

class TestQuestions(StatesGroup):
    decision1 = State()
    decision2 = State()
    decision3 = State()
    decision4 = State()
    decision5 = State()
    decision6 = State()
    decision7 = State()

async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Здравствуйте!")
    await message.answer("Чтобы приступить к тесту используйте команду /test", reply_markup=keyboard_remove)

async def cmd_stop(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Тест принудительно завершён", reply_markup=keyboard_remove)

async def cmd_help(message: types.Message):
    await message.answer("Тех. поддержка:\n@li_lhiver",
                         reply_markup=keyboard_remove)

async def cmd_info(message: types.Message):
    await message.answer("Этот бот поможет Вам изучить Республику Марий Эл \nс готовыми маршрутами, "
                         "составленными специально для вас!\n", reply_markup=keyboard_remove)

user_data = {}

async def test_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["культурные достопримечательности, история", "природные красоты", "красивая архитектура"]
    keyboard.add(*buttons)
    await message.answer("Мне интересны:", reply_markup=keyboard)
    global culture_res, nature_res, arch_res
    culture_res = 0
    nature_res = 0
    arch_res = 0
    await TestQuestions.decision1.set()

async def decision1(message: types.Message, state: FSMContext):
    decision = message.text.lower()
    if decision not in available_decision_answer1:
        await message.answer("Пожалуйста, используйте клавиатуру ниже")
        return
    if message.text == "культурные достопримечательности, история":
        global culture_res
        culture_res += 1
    elif message.text == "природные красоты":
        global nature_res
        nature_res += 1
    elif message.text == "красивая архитектура":
        global arch_res
        arch_res += 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["времяпровождение на свежем воздухе", "прогулки по городу",
               "не люблю много ходить, предпочитаю пассивный отдых"]
    keyboard.add(*buttons)
    await TestQuestions.decision2.set()
    await message.answer("Я люблю:", reply_markup=keyboard)

async def decision2(message: types.Message, state: FSMContext):
    global culture_res, nature_res, arch_res
    decision = message.text.lower()
    if decision not in available_decision_answer2:
        await message.answer("Пожалуйста, используйте клавиатуру ниже")
        return
    if message.text == "не люблю много ходить, предпочитаю пассивный отдых":
        culture_res += 1
    elif message.text == "времяпровождение на свежем воздухе":
        nature_res += 1
    elif message.text == "прогулки по городу":
        arch_res += 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["изучать историю своей страны, узнавать о жизни великих людей", "я интересуюсь архитектурными стилями",
               "я увлекаюсь геологическими и этимологическими сведениями о памятниках природы"]
    keyboard.add(*buttons)
    await TestQuestions.decision3.set()
    await message.answer("Мне нравится:", reply_markup=keyboard)

async def decision3(message: types.Message, state: FSMContext):
    global culture_res, nature_res, arch_res
    decision = message.text.lower()
    if decision not in available_decision_answer3:
        await message.answer("Пожалуйста, используйте клавиатуру ниже")
        return
    if message.text == "изучать историю своей страны, узнавать о жизни великих людей":
        culture_res += 1
    elif message.text == "я увлекаюсь геологическими и этимологическими сведениями о памятниках природы":
        nature_res += 1
    elif message.text == "я интересуюсь архитектурными стилями":
        arch_res += 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["восхищаюсь скульптурными композициями", "увлекаюсь искусством и живописью",
               "мне нравится любоваться живописными пейзажами"]
    keyboard.add(*buttons)
    await TestQuestions.decision4.set()
    await message.answer("Я скорее:", reply_markup=keyboard)

async def decision4(message: types.Message, state: FSMContext):
    global culture_res, nature_res, arch_res
    decision = message.text.lower()
    if decision not in available_decision_answer4:
        await message.answer("Пожалуйста, используйте клавиатуру ниже")
        return
    if message.text == "увлекаюсь искусством и живописью":
        culture_res += 1
    elif message.text == "мне нравится любоваться живописными пейзажами":
        nature_res += 1
    elif message.text == "восхищаюсь скульптурными композициями":
        arch_res += 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
    buttons = ["досуг для прогулок по городу, создания фотографий на фоне различных сооружений архитектуры",
               "досуг для активного отдыха с семьей, компанией или уединение на природе",
               "полезный досуг, хочу узнать что-то новое, посмотреть на вещи, созданные людьми в различные времена"]
    keyboard.add(*buttons)
    await TestQuestions.decision5.set()
    await message.answer("Я ищу:", reply_markup=keyboard)

async def decision5(message: types.Message, state: FSMContext):
    global culture_res, nature_res, arch_res
    decision = message.text.lower()
    if decision not in available_decision_answer5:
        await message.answer("Пожалуйста, используйте клавиатуру ниже")
        return
    if message.text == "полезный досуг, хочу узнать что-то новое, посмотреть на вещи, созданные людьми в различные времена":
        culture_res += 1
    elif message.text == "досуг для активного отдыха с семьей, компанией или уединение на природе":
        nature_res += 1
    elif message.text == "досуг для прогулок по городу, создания фотографий на фоне различных сооружений архитектуры":
        arch_res += 1
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["восхищаюсь скульптурными композициями", "увлекаюсь искусством и живописью",
               "мне нравится любоваться живописными пейзажами"]
    keyboard.add(*buttons)
    await TestQuestions.decision6.set()
    await message.answer("Я скорее:", reply_markup=keyboard)

async def decision6(message: types.Message, state: FSMContext):
    global culture_res, nature_res, arch_res
    if max(culture_res,nature_res,arch_res) == arch_res:
        await message.answer("Вам подойдет маршрут по архитектурным достопримечательствам города")
    await TestQuestions.decision7.set()
    await message.answer("Я скорее:")#, reply_markup=keyboard

from aiogram.types import BotCommand

logger = logging.getLogger(__name__)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/test", description="Начать тест"),
        BotCommand(command="/stop", description="Завершить тест"),
        BotCommand(command="/info", description="Ссылки и полезная информация"),
        BotCommand(command="/help", description="Помощь")
    ]
    await bot.set_my_commands(commands)

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_stop, commands="stop", state="*")
    dp.register_message_handler(cmd_help, commands="help", state="*")
    dp.register_message_handler(cmd_info, commands="info", state="*")

def register_handlers_question(dp: Dispatcher):
    dp.register_message_handler(test_start, commands="test", state="*")
    dp.register_message_handler(decision1, state=TestQuestions.decision1)
    dp.register_message_handler(decision2, state=TestQuestions.decision2)
    dp.register_message_handler(decision3, state=TestQuestions.decision3)
    dp.register_message_handler(decision4, state=TestQuestions.decision4)
    dp.register_message_handler(decision5, state=TestQuestions.decision5)
    dp.register_message_handler(decision6, state=TestQuestions.decision6)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    bot = Bot(token="5330757094:AAEBAv-n4DpkuXSeAmswRiTS50wg3Wahj7o")
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_common(dp)
    register_handlers_question(dp)
    await set_commands(bot)

    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
