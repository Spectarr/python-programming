# -*- coding: utf-8 -*-
import random

HEART_SYMBOL = "\u2764"

words_dict = {
    "1": "сервис, педаль, парфюм, очевидец, хлам, матрёшка, кастрюля, пионер, оптика, алгебра, килт, сирена, клюв, кепка, олимп, дровосек, гольф, цикл, задник, король, крот, клык, порох, вратарь, клумба, деревня, метод, базар, вирус, чеснок, марш, улица, импорт, казино, аппликация, клубника, организатор, завивка, инженер, рукавица, стакан, экспорт, папа, вентилятор, обшивка, рубаха, запеканка, традиция, стрела, балалайка, биография, банан, отдел, стройка, бугор, интерн, калибр, композитор, название, балка, вакансия, глянец, нагреватель, кабриолет, дикарь, кит, снегопад, уха, клиника, картина, приятель, осьминог, ровесник, прибыль, крыжовник, посол, активность, спина, шов, вывод, креветка, запись, чулок, подтяжки, эксперимент, беседа, житель, песочница, закат, зелень, ежиха, завет, досье, кёрлинг, охотник, горло, заклинание, кукуруза, козерог, внимание, объектив, код, оборона, гадалка, факел, паркет, памятник, болельщик, зрение, одиночество, стадо, тир, зона, премия, оптика, полдень, скульптура, матрос, кобыла, гол",
    "2": "взяточник, матерщинник, ответчик, стерлядь, попрыгун, канцероген, аристократизм, апекс, куропатка, колкость, балдахин, мегаполис, кунжут, тендер, бизон, постскриптум, праотец, гарантия, дедовщина, токсикоз, взломщик, мыловарение, пандемия, марсельеза, дьяк, распространитель, филиал, фальшивомонетчик, созерцание, загашник, чужестранец, минерал, оборванец, тяжба, вознаграждение, зачинщик, колледж, империалист, купорос, анаконда, соавторство, стекловолокно, райцентр, произношение, костолом, мгла, просторечие, чебурек, счастливец, вето, консерватор, реформист, ведомость, проделка, скольжение, транслитерация, вогнутость, утреня, крупинка, прорва, страхователь, ростбиф, блокировка, самооборона, сожительство, континент, атомщик, уринотерапия, ясность, утрата, агитация, аэростат, оленеводство, телескоп, пенициллин, абракадабра, синь, утолщение, перфоманс, основатель, обход, утренник, торговля, смирение, ондатра, стряпня, кедровник, натура, холера, универсиада, церковнослужитель, тореадор, протекция, округа, возможность, веха, критикан, запасник, комплементарность, комбайнёр, старание, спецкор, презрение, ревизор, фаска, предплечье, разгулье, черничник, арматурщик, лихорадка, рецидивист, результат, кушак, зачинщик, впадина, гранатомёт, живопись, помарка, оппонент, пенс",
    "3": "стрежень, арпеджиатор, апробация, хартия, мадригал, разномыслие, жердина, подмастерье, оппортунист, опреснитель, выскабливание, животновод, комиссариат, одноголосие, женоненавистник, муфтий, веление, гауптвахта, стяжательство, затворник, эссеист, молибден, зуботычина, уроборос, чинопочитание, гасиенда, космы, авторитаризм, перигей, социал-демократия, гарпунщик, пролетариат, судосборщик, рачитель, голем, многозадачность, вооружённость, нейтрино, вместилище, единодержавие, пигмент, сунна, мракобес, желвак, величание, корабельщик, всевластие, протока, полнокровие, неликвид, персонификация, реструктуризация, бутоньерка, измывательство, геополитика, дизъюнкция, втирание, враль, комиссариат, лапидарность, брандмауэр, жадеит, сухопутье, кистень, чертовня, коллективизм, гиацинт, конфорка, реминисценция, грифон, эквилибрист, бегония, вероучение, табаковод, мензура, конногвардеец, епархия, каверзник, бесприданница, изюбр, семантика, фельдъегерь, песчаник, бугай, компрачикос, исламоведение, притворщик, акциденция, басмач, восшествие, канонир, злопыхатель, урюк, сребролюбец, артериосклероз, разночинец, конкистадор, капрал, штрейкбрехер, аншлюс, атриум, рефрактор, семинария, эукариот, конверсия, казнокрадство, религиовед, карабинер, обличье, фонограмма, маловодье, комиссар, паренхима, забавник, сальдо, прихлебатель, шерстопрядение, креатин, примиренчество, вознесение",
}


def get_lives_count(difficulty):
    if difficulty == "1":
        lives = 12
    elif difficulty == "2":
        lives = 9
    elif difficulty == "3":
        lives = 6    
    return lives


def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    match = False
    index = 0
    while index < len(secret_word):
        if guessed_letter.lower() == secret_word[index].lower():
            match = True
            clue[index] = guessed_letter
            unknown_letters -= 1
        index = index + 1
    if match:
        print("Есть такая буква! [ {} ]".format(guessed_letter))
    return unknown_letters


def input_difficulty():
    difficulty = input(
        "Выберите уровень сложности (1, 2 или 3):\n 1 Лёгкий\n 2 Средний\n 3 Сложный\n"
    )
    return difficulty


def quiz():

    difficulty = input_difficulty()
    lives = get_lives_count(difficulty)
    words = words_dict[difficulty].split(", ")

    secret_word = random.choice(words)
    unknown_letters = len(secret_word)

    clue = list("?" * unknown_letters)
    guessed_word_correctly = False

    while lives > 0:

        print(clue)

        print("Осталось жизней: " + HEART_SYMBOL * lives)

        guess = input("Угадайте букву или слово целиком: ")

        if guess.lower() == secret_word.lower():
            guessed_word_correctly = True
            break

        if guess.lower() in secret_word.lower():
            unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        else:
            print("Неправильно. Вы теряете жизнь")
            lives = lives - 1
        if unknown_letters == 0:
            guessed_word_correctly = True
            break

    if guessed_word_correctly:
        print('Победа! Было загадано слово "' + secret_word + '"')
    else:
        print('Проигрыш! Было загадано слово "' + secret_word + '"')


if __name__ == "__main__":
    
    quiz()