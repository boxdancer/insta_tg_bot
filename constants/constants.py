import enum


class ExamType(str, enum.Enum):
    OGE = "ОГЭ"
    EGE = "ЕГЭ"


# Message Delay Constants Minutes
DELAY_MSG_0 = 0
DELAY_MSG_20 = 20 * 60 * 0
DELAY_MSG_50 = 50 * 60 * 0
DELAY_MSG_80 = 80 * 60 * 0


def __prepare_photo_data(file_name: str):
    with open(f"../constants/static/{file_name}.png", "rb") as photo:
        return photo.read()


# Photos
GREETING_PHOTO = __prepare_photo_data("GREETING_PHOTO")

# Message Text Constants
GREETING_MESSAGE = "Привет\! Я *Наташа Целина*, репетитор по математике для школьников с 5 по 11 класс\. Какой экзамен сдаёшь?"

EGE_MESSAGE_1 = """*Вот обещанный файл по стереометрии, в нём:* 
✅ только нужные формулы для задания 3 и 14
✅ я рассказала как удобно строить объёмные фигуры
✅ в конце тебя ждёт список задач для отработки

*Почему тебе стоит прямо сейчас открыть этот материал:*
• задание 3 и 14 школьники часто пропускают, т\.к\. не понимают геометрию
• ученики совершают ошибки, потому что просто зубрят без понимания"""
TEXT_EGE_BTN_1 = "Вся необходимая стереометрия"
URL_EGE_BTN_1 = (
    "https://www.buildin.ai/share/c1f84b25-3f47-4b20-86e8-4a7a6bec51ea?code=LJYE9L"
)

EGE_MESSAGE_2 = """*Знаешь, почему чаще сливают баллы в стереометрии?* 
– не вспомнили формулы
– забыли из чего состоит фигура
– записали не ту формулу объёма
– не поняли как построить фигуру
_А теперь представь, только на этих задачах можно_ __потерять 4 балла\!__
*Мой подход \= не зубрить, а понять логически задачу\!* 
Не забудь прочитать файл👆"""

EGE_MESSAGE_3 = """*Ты не поверишь, сколько сильных учеников сдуваются ближе к экзамену\.* _Почему?_
• потому что они не понимают, где они и куда идут
• «вроде решаю варианты, но пробники пишу плохо»
• «формулы есть, а уверенности — нет», «вдруг попадется то, чего я не решал или будет сложный вариант»

*Вот тебе пошаговый план подготовки к ЕГЭ, который я даю ученикам:*
✅ Темы выстроены от простых к сложным, чтобы сразу не выгореть из\-за трудного материала
✅ Перечислена вся необходимая теория 
✅ Примеры заданий, которые реально будут на ЕГЭ
✨ _Этот файл — твой маршрут\._ Он спасает от бардака в голове и срыва при стрессе\."""
TEXT_EGE_BTN_3 = "План подготовки"
URL_EGE_BTN_3 = (
    "https://www.buildin.ai/share/f9b58133-3ee5-416e-8d2b-fec4198e96f1?code=LJYE9L"
)

EGE_MESSAGE_4 = """*Давай проверим на сколько ты готов к ЕГЭ?*
Пройди реальный тест и узнай:
💫Где _ты теряешь баллы_
💫Над чем стоит поработать и сделать акцент

_Почему важно пройти тест?_
— Ты можешь быть неплох\(а\) в математике, но сливать баллы на мелких ошибках
— Или сидишь на 40 баллах и не понимаешь, как прыгнуть выше
— Или вообще, откладываешь подготовку, потому что не знаешь, с чего начать
_Этот тест — это не проверка знаний ради галочки\._ *Это шаг к системе\.* После него я отправлю тебе разбор ошибок и рекомендации, как двигаться дальше\. 
__Присылай фото с решением:__ @natashkatse"""
TEXT_EGE_BTN_4 = "Пройти тест"
URL_EGE_BTN_4 = (
    "https://drive.google.com/file/d/1EGWmS-d7UXQ6FHYBcZXOwlCAihM-zWnE/view?usp=sharing"
)

OGE_MESSAGE_1 = """ *Вот обещанный файл по «Шинам», в нём:* 
✅ собраны и решены все прототипы, которые могут попасться в номерах с 1 по 5
✅ лайфхаки с уже готовыми формулами
✅ в конце тебя ждёт список задач для отработки

_Почему тебе стоит прямо сейчас открыть этот материал:_
• задание с 1 по 5 школьники часто пропускают, т\.к\. не понимают как решать
• ученики совершают ошибки, потому невнимательно читают условия и пытаются вызубрить формулы"""
TEXT_OGE_BTN_1 = "Файл по шинам"
URL_OGE_BTN_1 = (
    "https://www.buildin.ai/share/29eca5bd-2765-4566-8119-bbf9c370af34?code=LJYE9L"
)

OGE_MESSAGE_2 = """*Знаешь, почему чаще сливают баллы в первых пяти номерах?* 
– заранее не разобрали номера
– не вспомнили формулы из геометрии
– забыли как решаются прототипы
– невнимательно прочитали условие
_А теперь представь, только на этих задачах_ __можно потерять 5 баллов\!__ Это больше половины проходного😱
*Мой подход \= не зубрить, а понять логически задачу\!* 
Не забудь прочитать файл👆"""

OGE_MESSAGE_3 = """*Ты не поверишь, сколько сильных учеников сдуваются ближе к экзамену\.* _Почему?_
— потому что они не понимают, где они и куда идут
— «вроде решаю варианты, но пробники пишу плохо»
— «формулы есть, а уверенности — нет», «вдруг попадется то, чего я не решал или будет сложный вариант»

*Вот тебе пошаговый план подготовки к ОГЭ, который я даю ученикам:*
✅ Темы выстроены от простых к сложным, чтобы сразу не выгореть из\-за трудного материала
✅ Перечислена вся необходимая теория 
✅ Примеры заданий, которые реально будут на ОГЭ
✨ _Этот файл — твой маршрут\._ Он спасает от бардака в голове и срыва при стрессе\. """
TEXT_OGE_BTN_3 = "План подготовки"
URL_OGE_BTN_3 = (
    "https://www.buildin.ai/share/fd1d6aec-174e-472e-9233-011744fe0328?code=LJYE9L"
)

OGE_MESSAGE_4 = """*Давай проверим на сколько ты готов к ОГЭ?*
Пройди реальный тест и узнай:
— Где ты теряешь баллы
— Над чем стоит поработать и сделать акцент

_Почему важно пройти тест?_
— Ты можешь быть неплох в математике, но сливать баллы на мелких ошибках
— Решаешь ОГЭ на 2 и не понимаешь, как прыгнуть выше
— Или вообще, откладываешь подготовку, потому что не знаешь, с чего начать
_Этот тест — это не проверка знаний ради галочки\._ *Это шаг к системе\.* После него я отправлю тебе разбор ошибок и рекомендации, как двигаться дальше\. 
__Присылай фото с решением:__ @natashkatse"""
TEXT_OGE_BTN_4 = "Пройти тест"
URL_OGE_BTN_4 = (
    "https://drive.google.com/file/d/1SuAsByMtOoxw0j90UMWqcbr5DW5cCu4b/view?usp=sharing"
)
