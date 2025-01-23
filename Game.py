import random
    
class GG:
    name = ""
    gender = ""
    style = ""
    wallet = 0
    hp_gg = 0
    damage_gg = 0
    defense_gg = 0
    agility_gg = 0
    critical_gg = 0
    
    shlem1 = []
    oruhie1 = []
    kirasa1 = []
    persten1 = []
    amulet1 = []
    shit1 = []
    botinky1 = []
    wallet = 100

    inventory_gg = []
    # создал по чертежу пустого персонажа
warrior = GG()
# наполняешь данными, сначала имя, пол, стиль
user_name = input("Назовите имя своего героя")
warrior.name = user_name

user_gender = input("Укажите пол Героя")
warrior.gender = user_gender

user_style = input("Укажите стиль Героя: Воин, Лучник, Маг")
warrior.style = user_style
if user_style == "Воин":
    hp_gg = 100
    damage_gg = random.randint(5,10)
if user_style == "Лучник":
    hp_gg = 80
    damage_gg = random.randint(7,12)
    critical_gg = 1
    agility_gg = 1
if user_style == "Маг":
    hp_gg = 80
    damage_gg = random.randint(7,12)
    critical_gg = 2
    defense_gg = -1

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
           shlem1.clear()
           shlem1.append(hochu_nadet)
           print("На вашей голове", shlem1)
       
    for i in amulet:
        if i == hochu_nadet:
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
            shit1.clear()
            shit1.append(hochu_nadet)
            print("В левой руке", shit1)
        
    for i in persten:
        if i == hochu_nadet:
            persten1.clear()
            persten1.append(hochu_nadet)
            print("На вашей руке сияет", persten1)

    for i in kirasa:
       if i == hochu_nadet:
           kirasa1.clear()
           kirasa1.append(hochu_nadet)
           print("На вас", kirasa1)
       
    for i in botinky:
        if i == hochu_nadet:
            botinky1.clear()
            botinky1.append(hochu_nadet)
            print("На ваших ногах", botinky1)
    if len(inventory_gg) > 20:
        print(inventory_gg)
        print("Нужно выкинуть лишний хлам")        
    
def tavern():
    print('\nВойдя в таверну, вас одурманивает запах шипящей газировки, однако вы концентрируетесь на посетителях таверны, и вам на глаза попадаются пару столиков, \
за одним из которых сидит маленький полуослик McGregor, за тем же столом сидит мускулистый орк-воин Пушистая лапка, за другим столом сидит угрюмая магичка Улыбка, \
и эльфика-лучница Слепота')
    input("Вы знакомитесь с: |1| полуослик McGregor(Цена 10), |2| орком-воином Пушистой лапкой(Цена 15), |3| магичкой Улыбкой (Цена 15), эльфийкой-лучницей Слепота(Цена 15)")

def weapon_magazin(): 
    while True:
        weapon = ['Тупой меч', 'Булава со сколами', 'Маленький клинок', 'Молоток', 'Деревяный щит с дырами', 'Волшебная палочка', 'Кривой лук']
        weapon1 = [5,5,5,5,5,5,5]
        print("Чтобы вы хотели купить?")
        a = input("[Что вы выберете: '|0| Тупой меч : Цена - 5', '|1| Булава со сколами: Цена - 5', '|2| Маленький клинок: Цена - 5', '|3| Молоток: Цена - 5', '|4| Деревяный щит с дырами: Цена - 5', '|5| Волшебная палочка: Цена - 5', '|6| Кривой лук: Цена - 5', '|7| Вернуться на площадь']") 
        if a == "0":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            print("Даёт характеристики: урон(1), шанс кровотечения 5% (по 1 урон/3 хода)")
            if confidence == "д":
                warrior.inventory_gg.append(weapon[0])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[0]
                print(warrior.wallet)
                print('Вряд-ли сможете этим кого-то зарезать')
                damage = 1
                
            if confidence == "н":
                return weapon_magazin()    
            item = input("Хотите ли вы надеть оружие? д/н")
            if item == "д":
                warrior.oruhie1.append(weapon[0])
                print("В правой руке", warrior.oruhie1)
                oruhie1_0 = warrior.inventory_gg.index(weapon[0])
                warrior.inventory_gg.pop(oruhie1_0)
                print("В рюкзаке", warrior.inventory_gg)
                damage_gg = random.randint(6,11)
                bleeding_b = random.randint(1,20)
   # if bleeding_b == damage 1:
        # bleeding_a = hp_monster - 1 < 3 move
            if item == "н":
                warrior.inventory_gg.append(weapon[0])  
        if a == "1":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            print("Даёт характеристики: урон(1), шанс оглушения 5%(противник пропускает ход)")
            if confidence == "д":
                warrior.inventory_gg.append(weapon[1])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[1]
                print(warrior.wallet)
                print('Возможно расыпется при ударе')
            if confidence == "н":
                return weapon_magazin()     
            item = input("Хотите ли вы надеть оружие? д/н")
            if item == "д":
                warrior.oruhie1.append(weapon[1])
                print("В правой руке", warrior.oruhie1)
                oruhie1_1 = warrior.inventory_gg.index(weapon[1])
                warrior.inventory_gg.pop(oruhie1_1)
                print("В рюкзаке", warrior.inventory_gg)
                damage_gg = random.randint(6,11)
   # if stun_b == 1 move: 
        # if stun_c = random.randint(1,20)
             # stun_a = not damage_monster   
            if item == "н":
                warrior.inventory_gg.append(weapon[1])   
        if a == "2":
             confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
             if confidence == "д":
                warrior.inventory_gg.append(weapon[2])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[2]
                print(warrior.wallet)   
                print('Зуботочка')
             if confidence == "н":
                return weapon_magazin()    
        if a == "3":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":
                warrior.inventory_gg.append(weapon[3])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[3]
                print(warrior.wallet)   
                print('Можно заколотить гвоздь')
            if confidence == "н":
                return weapon_magazin()    
        if a == "4":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":
                warrior.inventory_gg.append(weapon[4])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[4]
                print(warrior.wallet)   
                print('Сквозь него видишь просторы')
            if confidence == "н":
                return weapon_magazin()    
        if a == "5":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":            
                warrior.inventory_gg.append(weapon[5])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[5]
                print(warrior.wallet)   
                print('Точно ли волшебная?')
            if confidence == "н":
                return weapon_magazin()    
        if a == "6":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":     
                warrior.inventory_gg.append(weapon[6])
                print(warrior.inventory_gg)
                warrior.wallet -= weapon1[6]
                print(warrior.wallet)   
                print('Не факт, что попадешь в цель, если конечно не бить им')
            if confidence == "н":
                return weapon_magazin()        
        if a == "7":
            exit = (input("Хотите ли вы выйти с магазина? 1 - выход, 0 - нет"))
            if exit == "1":
                break

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
                
