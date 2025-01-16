import random
inventory_gg = []
if len(inventory_gg) > 20:
    print(inventory_gg)
    print("Нужно выкинуть лишний хлам")
    
class GG:
    name = input("Введите имя вашего Героя")
    print(name)
    gender = input("Пол Героя - парень/девушка")
    print(gender)
    style = input("Класс Героя - Воин, Лучник, Маг")
    print(style)
    wallet = 100

if GG.style == "Воин":
    hp_gg = 100
    damage_gg = random.randint(5,10)
    defense_gg = 1
    agility_gg = 1
    critical_gg = 1
if GG.style == "Лучник":
    hp_gg = 80
    damage_gg = random.randint(7,12)
    defense_gg = 1
    agility_gg = 2
    critical_gg = 2
if GG.style == "Маг":
    hp_gg = 80
    damage_gg = random.randint(7,12)
    defense_gg = 0
    agility_gg = 1
    critical_gg = 2
warrior = GG()
print(f"Вы {GG.gender} {GG.name} {GG.style}, недавно вами было взято задание - отправиться в жуткое подземелье ради спасения дочери императора, похищенной злым некромантом")
def ploshad():
    print('\nВы вышли на площадь города')
    print(f'{GG.name}, думает с чего начать свой путь. Перед вами находится:\n|1| Таверна, в которой можно было бы взять с собой путников в приключение,\n|2| Магазин оружия, \
где можно было бы обзавестись хорошей блестяшкой, которая могла бы не только ослепить, но возможно и ранить кого-нибудь,\n|3| Магазин доспехов, в котором можно было \
бы купить какую нибудь банку для защиты,\n|4| Зельеварня, в которой можно купить что-нибудь шипящее, возможно даже не газировку,\n|5| прямиком в ад, то есть в \
подземелье')
    b = input("Нажмите цифру, куда бы вы хотели пойти")
    return b
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
            if confidence == "д":
                inventory_gg.append(weapon[0])
                print(inventory_gg)
                warrior.wallet -= weapon1[0]
                print(warrior.wallet)
                print('Вряд-ли сможете этим кого-то зарезать')
            if confidence == "н":
                return weapon_magazin()      
        if a == "1":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":
                inventory_gg.append(weapon[1])
                print(inventory_gg)
                warrior.wallet -= weapon1[1]
                print(warrior.wallet)
                print('Возможно расыпется при ударе')
            if confidence == "н":
                return weapon_magazin()      
        if a == "2":
             confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
             if confidence == "д":
                inventory_gg.append(weapon[2])
                print(inventory_gg)
                warrior.wallet -= weapon1[2]
                print(warrior.wallet)   
                print('Зуботочка')
             if confidence == "н":
                return weapon_magazin()    
        if a == "3":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":
                inventory_gg.append(weapon[3])
                print(inventory_gg)
                warrior.wallet -= weapon1[3]
                print(warrior.wallet)   
                print('Можно заколотить гвоздь')
            if confidence == "н":
                return weapon_magazin()    
        if a == "4":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":
                inventory_gg.append(weapon[4])
                print(inventory_gg)
                warrior.wallet -= weapon1[4]
                print(warrior.wallet)   
                print('Сквозь него видишь просторы')
            if confidence == "н":
                return weapon_magazin()    
        if a == "5":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":            
                inventory_gg.append(weapon[5])
                print(inventory_gg)
                warrior.wallet -= weapon1[5]
                print(warrior.wallet)   
                print('Точно ли волшебная?')
            if confidence == "н":
                return weapon_magazin()    
        if a == "6":
            confidence = input("Вы уверены, что хотите приобрести эту вещь? д/н")
            if confidence == "д":     
                inventory_gg.append(weapon[6])
                print(inventory_gg)
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
