import random
    
class GG:
    name = ""
    gender = ""
    style = ""
    
    hp_gg = 0
    damage_gg = 5
    defense_gg = 0
    
    agility_gg = 0
    critical_gg = 0
    blok_gg = 0
    
    shlem1 = []
    oruhie1 = []
    kirasa1 = []
    persten1 = []
    amulet1 = []
    shit1 = []
    botinky1 = []
    wallet = 100

    inventory_gg = []
    group = []
    
class Mc:
    name_mc = "McGregor"
    hp_mc = 50
    damage_mc = random.randint(2,6)
    defense_mc = 1
    agility_mc = 1
    critical_mc = 1 
    
    inventory_mc = []
    
class Paw:
    name_paw = "Paw"
    hp_paw = 150
    damage_paw = random.randint(7,13)
    defense_paw = 1
    agility_paw = 1
    critical_paw = 1 
    
    inventory_paw = []
    
class Smile:
    name_smile = "Smile"
    hp_smile = 100
    damage_smile = random.randint(2,6)
    mag_damage_smile = random.randint(7,13)
    defense_smile = 1
    agility_smile = 1
    critical_smile = 1 
    
    inventory_smile = []
    
class Cecity:
    name_cecity = "Cecity"
    hp_cecity = 100
    damage_cecity = random.randint(5,10)
    defense_cecity = 1 #5%
    agility_cecity = 2 #10%
    critical_cecity = 2 #10%
    
    inventory_cecity = []
    # создал по чертежу пустого персонажа
warrior = GG()
mc = Mc()
paw = Paw()
smile = Smile()
cecity = Cecity()

# наполняешь данными, сначала имя, пол, стиль
user_name = input("Назовите имя своего героя")
warrior.name = user_name

user_gender = input("Укажите пол Героя")
warrior.gender = user_gender


user_style = input("Укажите стиль Героя: Воин, Лучник, Маг")
warrior.style = user_style
if user_style == "Воин":
    warrior.hp_gg = 100
    warrior.damage_gg = random.randint(warrior.damage_gg , warrior.damage_gg + 5)
if user_style == "Лучник":
    warrior.hp_gg = 80
    warrior.damage_gg = random.randint(warrior.damage_gg + 2, warrior.damage_gg + 7)
    warrior.critical_gg = 1
    warrior.agility_gg = 1
if user_style == "Маг":
    warrior.hp_gg = 80
    warrior.damage_gg = random.randint(warrior.damage_gg + 2,warrior.damage_gg + 7)
    warrior.critical_gg = 2
    warrior.defense_gg = -1


hp_posle = warrior.hp_gg

print(f"Вы {warrior.gender} {warrior.name} {warrior.style}, недавно вами было взято задание - отправиться в жуткое подземелье ради спасения дочери императора, похищенной злым некромантом")
def ploshad():
    print('\nВы вышли на площадь города')
    print(f'{warrior.name}, думает с чего начать свой путь. Перед вами находится:\n|1| Таверна, в которой можно было бы взять с собой путников в приключение,\n|2| Магазин оружия, \
где можно было бы обзавестись хорошей блестяшкой, которая могла бы не только ослепить, но возможно и ранить кого-нибудь,\n|3| Магазин доспехов, в котором можно было \
бы купить какую нибудь банку для защиты,\n|4| Зельеварня, в которой можно купить что-нибудь шипящее, возможно даже не газировку,\n|5| Прямиком в ад, то есть в \
подземелье, \n|i| Для инвентаря')
    b = input("Нажмите цифру, куда бы вы хотели пойти")
    return b
def item(): 
    shlem = ["Кожаный шлем", "Деревяный шлем", "Железная маска"]
    kirasa = ["Кожаная накидка", "Деревяный доспех", "Пластинчитый доспех"]
    oruhie = ['Тупой меч', 'Булава со сколами', 'Маленький клинок', 'Молоток', 'Волшебная палочка', 'Кривой лук']
    shit = ['Деревяный щит с дырами']
    botinky = ["Кожаные сапоги", "Деревяные сапоги", "Полу-железные сандали"]
    amulet = ["Обычный амулет"]
    persten = ["Обычный перстень"]

    
    hochu_nadet = ""


    if b == "i":
       print(warrior.inventory_gg) 
       invent1 = input("Желаете ли вы надеть что-нибудь? д/н") 
       if invent1 == "д":
            for k, item in enumerate(warrior.inventory_gg):
                print(k , item) 
       num = int(input())
       hochu_nadet = warrior.inventory_gg[num]

    for i in shlem:
        if i == hochu_nadet:
           if len(warrior.shlem1) > 0:
               warrior.inventory_gg.append(warrior.shlem1[0])
           shlem1.clear()
           shlem1.append(hochu_nadet)
           print("На вашей голове", shlem1)
       
    for i in amulet:
        if i == hochu_nadet:
           if len(warrior.amulet1) > 0:
               warrior.inventory_gg.append(warrior.amulet1[0])
           amulet1.clear()
           amulet1.append(hochu_nadet)
           print("На вашей шее сияет", amulet1)

    for i in oruhie:
        if i == hochu_nadet:
            if len(warrior.oruhie1) > 0:
                warrior.inventory_gg.append(warrior.oruhie1[0])
            warrior.oruhie1.clear()
            warrior.oruhie1.append(hochu_nadet)
            print("В правой руке", warrior.oruhie1)
        
    for i in shit:
        if i == hochu_nadet:
            if len(warrior.shit1) > 0:
                warrior.inventory_gg.append(warrior.shit1[0])
            shit1.clear()
            shit1.append(hochu_nadet)
            print("В левой руке", shit1)
        
    for i in persten:
        if i == hochu_nadet:
            if len(warrior.persten1) > 0:
                warrior.inventory_gg.append(warrior.persten1[0])
            persten1.clear()
            persten1.append(hochu_nadet)
            print("На вашей руке сияет", persten1)

    for i in kirasa:
       if i == hochu_nadet:
           if len(warrior.kirasa1) > 0:
               warrior.inventory_gg.append(warrior.kirasa1[0])
           kirasa1.clear()
           kirasa1.append(hochu_nadet)
           print("На вас", kirasa1)
       
    for i in botinky:
        if i == hochu_nadet:
            if len(warrior.botinky1) > 0:
                warrior.inventory_gg.append(warrior.botinky1[0])
            botinky1.clear()
            botinky1.append(hochu_nadet)
            print("На ваших ногах", botinky1)
    if len(inventory_gg) > 20:
        print(inventory_gg)
        print("Нужно выкинуть лишний хлам")  
        
def haracter_weapon(item_number):
     print("Урон игрока", warrior.damage_gg)
     if item_number == 0:
         damage_mech = warrior.damage_gg + random.randint(1,1)
         print("Урон игрока с мечом", damage_mech)
         blood = random.randint(1,20)
         #if blood == 1:
             #warrior.damage_gg = warrior.damage_gg + 1 move (3)
     if item_number == 1:
         damage_bulava = warrior.damage_gg + random.randint(1,1)
         stun = random.randint(1,20)
         print("Урон игрока с булавой", damage_bulava)
        # if stun == 1:
             #not monster.damage
     if item_number == 2:
         damage_klinok = warrior.damage_gg + random.randint(2,2)
         print("Урон игрока с клинком", damage_klinok)
     if item_number == 3:
         damage_molotok = warrior.damage_gg + random.randint(1,1)
         stun = random.randint(1,20)
         print("Урон игрока с молотком", damage_molotok)
         #if stun == 1:
             #not monstet.damage
     if item_number == 4:
         defense_gg = 1
         shans_bloka = random.randint(1,20)
         print("Защита игрока", defense_gg)
         #if shans_bloka == 1:
             #not monster.damage
     if item_number == 5:
         damage_palka = warrior.damage_gg + random.randint(1,1)
         shans_magic = random.randint(1,2)
         if shans_magic == 1:
             damage_palka = warrior.damage_gg + random.randint(2,5)
         print("Урон игрока с волшебной палочкой", damage_palka)
     if item_number == 6:
         damage_luk = warrior.damage_gg + random.randint(3,3)  
         promax = random.randint(1,2)
         if promax == 1:
             not warrior.damage_gg
         print("Урон игрока с луком", damage_luk)  
         
def haracter_armor(vibor):    
    print("Жизнь героя:", warrior.hp_gg)
    print("Защита героя:", warrior.defense_gg)
    if vibor == 0:
        warrior.defense_gg += 1
        warrior.hp_gg += 2
    if vibor == 1:
        warrior.defense_gg += 1
        warrior.hp_gg += 5
    if vibor == 2:
        warrior.defense_gg += 1
        warrior.hp_gg += 2
    if vibor == 3:
        warrior.defense_gg += 1
        warrior.hp_gg += 3
    if vibor == 4:
        warrior.defense_gg += 2
        warrior.hp_gg += 10
    if vibor == 5:
        warrior.defense_gg += 1
        warrior.hp_gg += 3
    if vibor == 6:
        warrior.defense_gg += 1
        warrior.hp_gg += 2
    if vibor == 7:
        warrior.defense_gg += 1
        warrior.hp_gg += 5
    if vibor == 8:
        warrior.defense_gg += 1
        warrior.hp_gg += 2
        
        
def haracter_armor_minus(old_item1):
    if old_item1 == "Кожаный шлем":
        warrior.hp_gg -= 2
        warrior.defense_gg -= 1
    if old_item1 == "Кожаная накидка":
        warrior.hp_gg -= 5
        wqrrior.defense_gg -= 1
    if old_item1 == "Кожаные сапоги":
        warrior.hp_gg -= 2
        warrior.defense_gg -= 1
    if old_item1 == "Деревяный шлем":
        warrior.hp_gg -= 3
        warrior.defense_gg -= 1
    if old_item1 == "Деревяный доспех":
        warrior.hp_gg -= 10
        warrior.defense_gg -= 2
    if old_item1 == "Деревяные сапоги":
        warrior.hp_gg -= 3
        warrior.defense_gg -= 1
    if old_item1 == "Железная маска":
        warrior.hp_gg -= 2
        warrior.defense_gg -= 1
    if old_item1 == "Пластинчитый доспех":
        warrior.hp_gg -= 5
        warrior.defense_gg -= 1
    if old_item1 == "Полу-железные сандали":
        warrior.hp_gg -= 2
        warrior.defense_gg -= 1
             
def bonus():
    # Проверяем, есть ли все элементы экипировки
    koh_full_set = (
        "Кожаный шлем" in warrior.shlem1 and
        "Кожаная накидка" in warrior.kirasa1 and
        "Кожаные сапоги" in warrior.botinky1
    )

    # Если все элементы надеты и бонус еще не добавлен
    if koh_full_set and not hasattr(warrior, 'bonus_applied'):
        warrior.agility_gg += 1
        warrior.bonus_applied = True  # Помечаем, что бонус добавлен
        print("Бонус добавлен, ловкость героя:", warrior.agility_gg)

    # Если хотя бы один элемент снят и бонус был добавлен
    elif not koh_full_set and hasattr(warrior, 'bonus_applied'):
        warrior.agility_gg -= 1
        del warrior.bonus_applied  # Убираем отметку о добавленном бонусе
        print("Бонус убран, ловкость героя:", warrior.agility_gg)
        
     # Проверяем, есть ли все элементы экипировки
    der_full_set = (
        "Деревяный шлем" in warrior.shlem1 and
        "Деревяный доспех" in warrior.kirasa1 and
        "Деревяные сапоги" in warrior.botinky1
    )

    # Если все элементы надеты и бонус еще не добавлен
    if der_full_set and not hasattr(warrior, 'bonus_applied1'):
        warrior.blok_gg += 1
        warrior.defense_gg += 1
        warrior.agility_gg -= 2
        warrior.critical_gg -= 1
        warrior.bonus_applied1 = True  # Помечаем, что бонус добавлен
        print("Бонус добавлен, блок героя:", warrior.blok_gg)
        print("Бонус добавлен, защита героя:", warrior.defense_gg)
        print("Бонус добавлен, ловкость героя:", warrior.agility_gg)
        print("Бонус добавлен, крит героя:", warrior.critical_gg)

    # Если хотя бы один элемент снят и бонус был добавлен
    elif not der_full_set and hasattr(warrior, 'bonus_applied1'):
        warrior.blok_gg -= 1
        warrior.defense_gg -= 1
        warrior.agility_gg += 2
        warrior.critical_gg += 1
        del warrior.bonus_applied1 # Убираем отметку о добавленном бонусе
        print("Бонус убран, блок героя:", warrior.blok_gg)
        print("Бонус убран, защита героя:", warrior.defense_gg)
        print("Бонус убран, ловкость героя:", warrior.agility_gg)
        print("Бонус убран, крит героя:", warrior.critical_gg)
        
    # Проверяем, есть ли все элементы экипировки
    zhel_full_set = (
        "Железная маска" in warrior.shlem1 and
        "Пластинчитый доспех" in warrior.kirasa1 and
        "Полу-железные сандали" in warrior.botinky1
    )

    # Если все элементы надеты и бонус еще не добавлен
    if zhel_full_set and not hasattr(warrior, 'bonus_applied2'):
        warrior.critical_gg += 1
        warrior.bonus_applied2 = True  # Помечаем, что бонус добавлен
        print("Бонус добавлен, крит героя:", warrior.critical_gg)

    # Если хотя бы один элемент снят и бонус был добавлен
    elif not zhel_full_set and hasattr(warrior, 'bonus_applied2'):
        warrior.critical_gg -= 1
        del warrior.bonus_applied2  # Убираем отметку о добавленном бонусе
        print("Бонус убран, крит героя:", warrior.critical_gg)
    
             
def tavern():
    print('\nВойдя в таверну, вас одурманивает запах шипящей газировки, однако вы концентрируетесь на посетителях таверны, и вам на глаза попадаются пару столиков, \
за одним из которых сидит маленький полуослик McGregor, за тем же столом сидит мускулистый орк-воин Пушистая лапка, за другим столом сидит угрюмая магичка Улыбка, \
и эльфика-лучница Слепота')
    sput = input("Вы знакомитесь с: |1| полуослик McGregor(Цена 10), |2| орком-воином Пушистой лапкой(Цена 15), |3| магичкой Улыбкой (Цена 15), эльфийкой-лучницей Слепота(Цена 15) |5| выход на площадь")
    if sput == "1":
        if mc in warrior.group:
            print("У вас уже есть полуослик! Вы не осилите двоих!")
            return tavern()
        warrior.group.append(mc)
        for friends in warrior.group:
            if friends == mc:
                print("Теперь с вами настоящий, говорящий полуослик", mc.name_mc)
                warrior.wallet -= 10
                print("В кошельке", warrior.wallet)
    if sput == "2":
        if paw in warrior.group:
            print("У вас уже есть Лапка! Слишком пушисто!")
            return tavern()
        warrior.group.append(paw)
        for friends in warrior.group:
            if friends == paw:
                print("Теперь у вас есть кого погладить", paw.name_paw)
                warrior.wallet -= 15
                print("В кошельке", warrior.wallet)
    if sput == "3":
        if smile in warrior.group:
            print("У вас уже есть Улыбка! Вы слишком счастливы!")
            return tavern()
        warrior.group.append(smile)
        for friends in warrior.group:
            if friends == smile:
                print("Теперь вам будет весело с такой компанией", smile.name_smile)
                warrior.wallet -= 15
                print("В кошельке", warrior.wallet)
    if sput == "4":
        if cecity in warrior.group:
            print("У вас уже есть Слепота! Вы точны, как никогда!")
            return tavern()
        warrior.group.append(cecity)
        for friends in warrior.group:
            if friends == cecity:
                print("С таким выбором, вы не промахнулись", cecity.name_cecity)
                warrior.wallet -= 15
                print("В кошельке", warrior.wallet)
    if sput == "5":
       return ploshad()
        
       

def weapon_magazin(): 
    while True:
        print('\nВойдя в магазин оружия, вы не видите карлика за прилавком, но он там есть. Подойдя ближе и осмотривая витрины, вы наконец-то пнули его и обратили \
на него внимание. Вы на секунду подумали, что это боевой гном и создает высококачественное вооружение, но нет, это оказался просто карлик, а поняли вы это, потому, \
как он отлетел от вашего пинка. Отряхиваясь, он сказал вам: Добро пожаловать ')
        weapon = ['Тупой меч', 'Булава со сколами', 'Маленький клинок', 'Молоток', 'Деревяный щит с дырами', 'Волшебная палочка', 'Кривой лук']
        weapon1 = [5,5,5,5,5,5,5]
        print("Чтобы вы хотели купить?")
        item_number = int(input("[Что вы выберете: '|0| Тупой меч : Цена - 5', '|1| Булава со сколами: Цена - 5', '|2| Маленький клинок: Цена - 5', '|3| Молоток: Цена - 5', '|4| Деревяный щит с дырами: Цена - 5', '|5| Волшебная палочка: Цена - 5', '|6| Кривой лук: Цена - 5', '|7| Вернуться на площадь']"))
        
        if item_number == 0:
            print("Вряд-ли этим можно кого-то зарезать")
            print("Оружие дает: урон 1, кровотечение(1 урон/3 хода) шанс кровотечения 5%")
        if item_number == 1:
            print("Возможно рассыпется при ударе")
            print("Оружие дает: урон 1, шанс оглушения 5% (пропуск монстром хода)")
        if item_number == 2:
            print("Зуботочка")
            print("Оружие дает: урон 2")
        if item_number == 3:
            print("Уникальная возможность, заколотить гвоздь")
            print("Оружие дает: урон 1, шанс оглушения 5% (пропуск монстром хода)")
        if item_number == 4:
            print("Сквозь него видно просторы")
            print("Щит дает: защиту 1, шанс заблокировать удар 5%")
        if item_number == 5:
            print("Точно ли волшебная?")
            print("Оружие дает: урон 1, возможность магического урона 50% с уроном от 2 до 5, мана 50")
        if item_number == 6:
            print("Не факт что попадешь с ним, если конечно не бить им")
            print("Оружие дает: урон 3, шанс промоха 50%")
        if item_number == 7:
            return ploshad()
    # словарь для всех возможных предметов
        categories = {
            "Тупой меч": warrior.oruhie1,
            "Булава со сколами": warrior.oruhie1,
            "Маленький клинок": warrior.oruhie1,
            "Молоток": warrior.oruhie1, 
            "Деревяный щит с дырами": warrior.shit1,
            "Волшебная палочка": warrior.oruhie1,
            "Кривой лук": warrior.oruhie1
            }
        
        # печатаем что сейчас в продаже
        v = input("Хотите ли купить это? д/н")
        if v == "д":
        # добавляем в инвентарь то, что купили
            warrior.wallet = warrior.wallet - weapon1[item_number]
            print(warrior.wallet)
            warrior.inventory_gg.append(weapon[item_number])
        if v == "н":
            return weapon_magazin()
        # выясняем как это называется
        item_name = weapon[item_number]
        print("Сейчас в инвентаре после покупки  предмета:", warrior.inventory_gg)
        decision = input("Хотите надеть? д/н\n")

        # блок если хотим надеть
        if decision == "д":
            haracter_weapon(item_number)   
            # если на персонаже уже что-то надето
            if len(categories[item_name]) > 0:
                # забираем у персонажа текущий предмет
                 old_item = categories[item_name].pop()
                # кладем его обратно в инвентарь
                 warrior.inventory_gg.append(old_item)
                # даем персонажу новый предмет
                 categories[item_name].append(weapon[item_number])

                # ищем индекс предмета в инвентаре, который мы надели
                 item_name = weapon[item_number]
                 item_index = warrior.inventory_gg.index(item_name)
                # убираем его из инвентаря
                 warrior.inventory_gg.pop(item_index)

                 print("На персонаже:", categories[item_name])
                 print("В инвентаре:", warrior.inventory_gg)
            # если на персонаже ничего нет
            else:
                 categories[item_name].append(weapon[item_number])
                 warrior.inventory_gg.pop()
                 print("На персонаже:", categories[item_name])
                 print("В инвентаре:", warrior.inventory_gg)
        else:
             print("На персонаже:", categories[item_name])
             print("В инвентаре:", warrior.inventory_gg)
        exit = input("Хотите покинуть магазин? д/н")
        if exit == "д":
            ploshad()
        if exit == "н":
            weapon_magazin()       

def armor_magazin():
    while True:
        print('\nВойдя в магазин доспехов, вы увидели девушку, которая падает с лесницы, пытаясь ухватиться хоть за что-то, она роняет на себя ещё и коробки с витрин.Немного подождав, чтобы понять остался кто-нибудь в магазине живой, кроме вас. Вы услышали зов о помощи. Вы  подошли и начали раставлять коробки обратно по местам витрины, случайно закинув на полку девушку на которой был одет тяжелый доспех, видимо во время падения.Вы извинились и вытряхнули девушку из доспеха. Девушка сказала: Спасибо, мы всегда рады новым покупателям.')
        armor = ['Кожаный шлем', 'Кожаная накидка','Кожаные сапоги', 'Деревяный шлем','Деревяный доспех','Деревяные сапоги','Железная маска','Пластинчитый доспех','Полу-железные сандали']
        armor1 = [5,10,5,5,10,5,5,10,5]
        print("Чтобы вы хотели купить?")
        vibor = int(input("Что вы выберете: |0| Кожаный шлем, |1| Кожаная накидка, |2| Кожаные сапоги, |3| Деревяный шлем, |4| Деревяный доспех, |5| Деревяные сапоги, |6| Железная маска, |7| Пластинчитый доспех, |8| Полу-железные сандали, |9| Выход"))
        
        if vibor == 0:
            print("Иногда уносит ветром")
            print("Характеристики шлема : защита 1, hp 2")
            print("Бонус комплекта(шлем, накидка,сапоги) = 5% шанс уворота")
        if vibor == 1: 
            print("Если не боитесь холода, она хорошо продувается")
            print("Характеристики накидки: защита 1, hp 5")
            print("Бонус комплекта(шлем, накидка,сапоги из кожи) = 5% шанс уворота")
        if vibor == 2:
            print("Застревают в грязи, ходите по подземелью")
            print("Характеристики сапог: защита 1, hp 2")
            print("Бонус комплекта(шлем, накидка,сапоги) = 5% шанс уворота")
        if vibor == 3:
            print("Дуб для дуба, давит на мозг")
            print("Характеристики шлема: защита 1, hp 3")
            print("Бонус комплекта(шлем, доспех,сапоги из дерева) = защита 1, шанс блока 5%, минус 10% шанс уворота, минус 5% шанс крита")
        if vibor == 4:
            print("Легко воспламеням, не курить в нем")
            print("Характеристики доспеха: защита 2, hp 10")
            print("Бонус комплекта(шлем, доспех,сапоги из дерева) = защита 1, шанс блока 5%, минус 10% шанс уворота, минус 5% шанс крита")
        if vibor == 5:
            print("Ходит молва, что вы можете прирости к земле")
            print("Характеристики сапог: защита 1, hp 3")
            print("Бонус комплекта(шлем, доспех,сапоги из дерева) = защита 1, шанс блока 5%, минус 10% шанс уворота, минус 5% шанс крита")
        if vibor == 6:
            print("Не смотрите в зеркало - испугаетесь")
            print("Характеристики маски: защита 1, hp 2")
            print("Бонус комплекта(маска, доспех,сандали из пластин) крит шанс 5%")
        if vibor == 7:
           print("Не особо защищает, но можете драться им") 
           print("Характеристики доспеха: защита 1, hp 5")
           print("Бонус комплекта(маска, доспех,сандали из пластин) крит шанс 5%")
        if vibor == 8:
            print("Не цепляйте землю, унесете с собой")
            print("Характеристики сандаль: защита 1, hp 2")
        if vibor == 9:
            return ploshad()
            
        categories1 = {
            "Кожаный шлем": warrior.shlem1,
            "Кожаная накидка": warrior.kirasa1,
            "Кожаные сапоги": warrior.botinky1,
            "Деревяный шлем": warrior.shlem1, 
            "Деревяный доспех": warrior.kirasa1,
            "Деревяные сапоги": warrior.botinky1,
            "Железная маска": warrior.shlem1,
            "Пластинчитый доспех": warrior.kirasa1,
            "Полу-железные сандали": warrior.botinky1
            }
            
        v = input("Хотите ли купить это? д/н")
        if v == "д":
        # добавляем в инвентарь то, что купили
            warrior.wallet = warrior.wallet - armor1[vibor]
            print(warrior.wallet)
            warrior.inventory_gg.append(armor[vibor])
        if v == "н":
            return armor_magazin()
        # выясняем как это называется
        item_name1 = armor[vibor]
        print("Сейчас в инвентаре после покупки  предмета:", warrior.inventory_gg)
        decision = input("Хотите надеть? д/н\n")

        # блок если хотим надеть
        if decision == "д":
            haracter_armor(vibor)   
     
            # если на персонаже уже что-то надето
            if len(categories1[item_name1]) > 0:
                # забираем у персонажа текущий предмет
                 
                 old_item1 = categories1[item_name1].pop()
                 haracter_armor_minus(old_item1)
                # кладем его обратно в инвентарь
                 warrior.inventory_gg.append(old_item1)
                # даем персонажу новый предмет
                 categories1[item_name1].append(armor[vibor])

                # ищем индекс предмета в инвентаре, который мы надели
                 item_name1 = armor[vibor]
                 item_index1 = warrior.inventory_gg.index(item_name1)
                # убираем его из инвентаря
                 warrior.inventory_gg.pop(item_index1)
                 bonus()
                 print("На персонаже:", categories1[item_name1])
                 print("Жизнь героя :", warrior.hp_gg)
                 print("Защита героя:", warrior.defense_gg)
                 print("В инвентаре:", warrior.inventory_gg)
            # если на персонаже ничего нет
            else:
                 categories1[item_name1].append(armor[vibor])
                 warrior.inventory_gg.pop()
                 bonus()
                 print("На персонаже:", categories1[item_name1])
                 print("Жизнь героя :", warrior.hp_gg)
                 print("Защита героя:", warrior.defense_gg)
                 print("В инвентаре:", warrior.inventory_gg)
        else:
             bonus()
             print("На персонаже:", categories1[item_name1])
             print("Жизнь героя :", warrior.hp_gg)
             print("Защита героя:", warrior.defense_gg)
             print("В инвентаре:", warrior.inventory_gg)
        exit = input("Хотите покинуть магазин? д/н")
        if exit == "д":
            ploshad()
        if exit == "н":
            armor_magazin()   
                
            
def potion_factory():
    print('\nВойдя в зельеварню вы увидели алхимика который что-то добавляет в котел и превращается в жабу, которая что-то добавляет в котел и получается взрыв, от взрыва вылетает кролик в вас, вы его хватаете и пытаетесь запихнуть в рюкзак, но вас просят отдать кролика. Вы его отдаете, жаба-алхимик кидает его в котел и становится обратно алхимиком, который вам говорит: Вы что-то хотели? Всех сварим.')
    potion = ["Малое зелье жизни"]
    potion1 = [2]
    pokupka_potion = int(input("Что вы выберете: |0| Малое зелье жизни(25хп) - стоимость 2, |1| Выход"))
    
    if pokupka_potion == 0:
        warrior.inventory_gg.append(potion[0])
        warrior.wallet -= potion1[0]
        print("В вашем кошельке:", warrior.wallet)
        print("В вашем рюкзаке",warrior.inventory_gg)
        use = input("Выпить сейчас? д/н")
        if use == "д":
            new_hp = hp_posle + 25
            if new_hp > warrior.hp_gg:
                new_hp = warrior.hp_gg
            item_name2 = potion[pokupka_potion]
            item_index2 = warrior.inventory_gg.index(item_name2)
            warrior.inventory_gg.pop(item_index2)
            print("Жизнь героя:", new_hp)
            print("В вашем рюкзаке:", warrior.inventory_gg)
            return potion_factory()
        if use == "н":
            print("В вашем рюкзаке",warrior.inventory_gg)
            return potion_factory()
    if pokupka_potion == 1:
        return ploshad()
        
        
def dangeon():
    print("Наконец-то проделав огромный путь, среди 3 магазинов и 1 таверны, вы собрались с силами всех возможных Богов, и встали перед огромными вратами подземелья. Вы полны решимости, готовы вынести любые испытания, и встретиться лицом к лицу с самой Смертью! Правда в таверне города. Ну что ж, вы всё ещё можете отступить, прежде чем ступите на путь страданий.")
    pobeg = input("Вы хотите сбежать? д/н")
    if pobeg == "д":
        return ploshad()
    if pobeg == "н":
        return one_storey()

def battle():
    monsters = [
        {"name": "крыса-людоед", "hp": 30, "damage": (1, 5)},
        {"name": "гоблин", "hp": 20, "damage": (2, 4)},
        {"name": "гоблин-шаман", "hp": 15, "damage": (3, 6)},
        {"name": "гоблин-воин", "hp": 25, "damage": (4, 7)},
        {"name": "крыса", "hp": 10, "damage": (1, 3)},
        {"name": "крыса-мутант", "hp": 35, "damage": (2, 6)}
    ]
    
    # Выбираем случайного монстра
    monster = random.choice(monsters)
    print(f"Вы встретили {monster['name']}!")
    
    
    # Бой
    while True:
        # Ход игрока
        damage = random.randint(*warrior.damage_gg)
        # damage = random.randint(warrior.damage[0],warrior.damage[1])
        monster['hp'] -= damage
        print(f"Вы нанесли {damage} урона! У монстра осталось {max(0, monster['hp'])} HP")
        
        if monster['hp'] <= 0:
            print(f"Вы победили {monster['name']}!")
            break
            
        # Ход монстра
        damage = random.randint(*monster['damage'])
        warrior.hp_gg -= damage
        print(f"{monster['name']} нанес вам {damage} урона! У вас осталось {max(0, player_hp)} HP")
        
        if player_hp <= 0:
            print("Вы проиграли...")
            break

# Запуск битвы
battle()
           
def one_storey():
    print("Вы заходите на первый ярус подземелья, и перед вами ничем не примечательная во всех отношениях глубина пещеры, вокруг сплошной камень, песок и темнота... Хоть где-то, но и светятся тускло факелы, освещая дорогу. Добро пожаловать")
    pohod = random.randint(1,100)
    print(pohod)
    if 10 > pohod:
        return two_storey()
    if 35 > pohod:
        sunduk = input("Долго блуждая по комнатам бесконечного, как вам кажеться, лабиринта подземелья, вы наткнулись на сундук, хотите ли его открыть? д/н")
        if sunduk == "д":
            sunduk1 = random.randint(1,2)
            if sunduk1 == 1:
                sunduk2 = random.randint(1,3)
                item_sunduk = ["Дубинка гоблина", "Крысиный хвост", "Щит гоблина", "Амулет гоблина-шамана","Амулет гоблина из зубов", "Обычное кольцо", "Деньги"]           
                for a in range (sunduk2):
                    loot = random.randint(0,6)
                    warrior.inventory_gg.append(item_sunduk[loot])
                    
                    if loot == 6:
                        warrior.wallet += random.randint(1,10)
                        print("В кошельке", warrior.wallet)
                        warrior.inventory_gg.remove("Деньги")
            if sunduk1 == 2:
                lovushka = random.randint(1,3)
                if lovushka == 1:
                    print("Вы попытались открыть сундук, но он никак не поддавался. Вы решили применить силу, и случайно порезались об крышку сундука")
                    warrior.hp_gg -= 1
                    print("Жизнь героя", warrior.hp_gg)
                if lovushka == 2:
                    print("Вы попытались открыть сундук, но он никак не поддавался. Вы решили с помощью оружия, сделать рычаг для открытия сундука, но у вас этот шанс с треском провалился и вы травмировались")
                    warrior.hp_gg -= 3
                    print("Жизнь героя", warrior.hp_gg)
                if lovushka == 3:
                    print("Вы попытались открыть сундук, но он никак не поддавался. Вы с яростью замахнулись оружием и направили всю злость на сундук, но оружие отскочило вам в ногу, вы ранены!")
                    warrior.hp_gg -= 5
                    print("Жизнь героя", warrior.hp_gg)
        print("В рюкзаке:", warrior.inventory_gg)
    if 60 > pohod:
        sobitie = random.randint(1,1)
        print(sobitie)
        if sobitie == 1:
            sobitie_s_krisoy = int(input("Вы в далеке видете гигантскую крысу, которая до сих пор, пока ещё не заметила вас. Чтобы вы захотели бы сделать? 0 = подойти и дать ей предмет, 1 = напасть сзади, чтобы застать в расплох, 2 = уйти, пока она вас не заметила."))
            if sobitie_s_krisoy == 0:

# Вывод списка с нумерацией (индексы начинаются с 0)
                for index, value in enumerate(warrior.inventory_gg):
                    otdal = print(f"{index}. {value}")
                otdal1 = int(input("Какой предмет вы хотите отдать?"))
                del warrior.inventory_gg[otdal1]
                if warrior.inventory_gg == []:
                    return battle
                #warrior.inventory_gg.remove[]
                    
                
            
 
def two_storey():
        print()
        
        
while True:
    b = ploshad()
    if b == "1":
        tavern()
    if b == "2":
        weapon_magazin()
    if b == "3":
        armor_magazin()
    if b == "4":
        potion_factory()
    if b == "5":
        dangeon()
    if b == "i":
        item()
                    
