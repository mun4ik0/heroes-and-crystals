import pgzrun
import random
from pgzero.keyboard import keyboard
from pgzero.actor import Actor

# Игровое окно
cell = Actor('grow')
cell1 = Actor('rock')
cell2 = Actor("rock2")
cell3 = Actor("rock3")
size_w = 10 # Ширина поля в клетках
size_h = 11 # Высота поля в клетках
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

win = 0
mode = "game"
colli = 0
kills = 0
TITLE = "Heroes and crystals" 
FPS = 30 
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 2, 1, 3, 2, 1, 2, 0], 
          [0, 1, 1, 2, 1, 3, 3, 1, 3, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 3, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 1, 0], 
          [0, 1, 1, 2, 3, 1, 1, 2, 1, 0], 
          [0, 1, 2, 1, 1, 3, 1, 1, 3, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]] 

# Главный герой
char = Actor('hero',size=(35,35))
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5
experience = 0
#Второй герой
second_char = Actor("second_hero_left")
second_char.top = cell.height
second_char.left = cell.width * (size_w - 2) 
second_char.health = 100
second_char.attack = 5
second_experience = 0
#Генерация врагов
enemies = []
second_enemies = []
#Максимальный\минимальный уровень здоровья врагов
min_h = 10
max_h = 15
#Максимальный\минимальный уровень атаки врагов
min_ap = 5
max_ap = 10


level = 1
#Отрисовка синих врагов
def enemies_draw():
    global mode
    for i in range(6):
        x = random.randint(1, 7) * cell.width
        y = random.randint(1, 7) * cell.height
        enemy = Actor("diamond", topleft = (x, y),size=(35,35))
        enemy.health = random.randint(min_h, max_h)
        enemy.attack = random.randint(min_ap,max_ap)
        enemy.bonus = random.randint(0, 2)
        enemies.append(enemy)


#Отрисовка зелёных врагов
def second_enemies_draw():
    global mode
    for i in range(6):
        x = random.randint(1, 7) * cell.width
        y = random.randint(1, 7) * cell.height
        second_enemy = Actor("second_enemy", topleft = (x, y),size=(35,35))
        second_enemy.health = random.randint(min_h, max_h)
        second_enemy.attack = random.randint(min_ap,max_ap)
        second_enemy.bonus = random.randint(0, 2)
        second_enemies.append(second_enemy)
enemies_draw()
second_enemies_draw()

# Бонусы
hearts = []
swords = []   

#Отрисовка карты
def my_map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 

#Отрисовка
def draw():
    if mode == 'game':
        screen.fill("#2f3542")
        my_map_draw()
        char.draw()
        second_char.draw()
        #Отрисовка здоровья и  атаки первого героя
        screen.draw.text("HP:", center=(25, 525), color = 'blue', fontsize = 20)
        screen.draw.text(str(char.health), center=(75, 525), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 525), color = 'blue', fontsize = 20)
        screen.draw.text(str(char.attack), center=(425, 525), color = 'white', fontsize = 20)
        screen.draw.text("EX:",center=(WIDTH/2 - 50,525),color = 'blue',fontsize = 20)
        screen.draw.text(str(experience),center=(WIDTH/2,525),color = 'yellow',fontsize = 20)
        #Отрисовка здоровья и атаки второго героя
        screen.draw.text("HP:", center=(25, 545), color = 'green', fontsize = 20)
        screen.draw.text(str(second_char.health), center=(75, 545), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 545), color = 'green', fontsize = 20)
        screen.draw.text(str(second_char.attack), center=(425, 545), color = 'white', fontsize = 20)
        screen.draw.text("EX:",center=(WIDTH/2 - 50,545),color = 'green',fontsize = 20)
        screen.draw.text(str(second_experience),center=(WIDTH/2,545),color = 'yellow',fontsize = 20)
        for i in range(len(enemies)):
            enemies[i].draw()
            #Отрисовка здоровья врага
            screen.draw.text(str(enemies[i].health), topleft=(enemies[i].x + 5, enemies[i].y - 30), color='white', fontsize=18)
        for i in range(len(second_enemies)):
            second_enemies[i].draw()
            screen.draw.text(str(second_enemies[i].health), topleft=(second_enemies[i].x + 5, second_enemies[i].y - 30), color='white', fontsize=18)
        #отрисовка бонусов
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()
        
    #Окно победы или поражения    
    elif mode == "end":
        screen.fill("#2f3542")
        if win == 1:
            if experience == 5000:
                screen.draw.text("Победа!", center=(WIDTH/2, HEIGHT/2), color = 'blue', fontsize = 46)
            elif second_experience == 5000:
                screen.draw.text("Победа!", center=(WIDTH/2, HEIGHT/2), color = 'green', fontsize = 46)
        else:
            screen.draw.text("Поражение!", center=(WIDTH/2, HEIGHT/2), color = 'white', fontsize = 46)


#Управление
def on_key_down(key):
    global colli, mode, win, kills, experience, second_experience
    old_x = char.x
    old_y = char.y
    second_old_x = second_char.x
    second_old_y = second_char.y
# Управление первым персонажем
    if keyboard.d and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'hero'
    elif keyboard.a and char.x - cell.width >= cell.width:
        char.x -= cell.width
        char.image = 'hero_left'
    elif keyboard.s and char.y + cell.height < HEIGHT - cell.height * 2:
        char.y += cell.height
    elif keyboard.w and char.y - cell.height >= cell.height:
        char.y -= cell.height
    if char.colliderect(second_char):
        char.x = old_x
        char.y = old_y
# Управление вторым персонажем
    if keyboard.right and second_char.x + cell.width < WIDTH - cell.width:
        second_char.x += cell.width
        second_char.image = 'second_hero'
    elif keyboard.left and second_char.x - cell.width >= cell.width:
        second_char.x -= cell.width
        second_char.image = 'second_hero_left'
    elif keyboard.up and second_char.y - cell.height >= cell.height:
        second_char.y -= cell.height
    elif keyboard.down and second_char.y + cell.height < HEIGHT - cell.height * 2:
        second_char.y += cell.height
    if second_char.colliderect(char):
        second_char.x = second_old_x
        second_char.y = second_old_y

    #Столкновение с врагами
    enemy_index = char.collidelist(enemies)
    if enemy_index != -1:
        char.x = old_x
        char.y = old_y
        colli = 1
        enemy = enemies[enemy_index]
        enemy.health -= char.attack
        char.health -= enemy.attack
        if enemy.health <= 0:
            experience += 100
            kills += 1
            #Добавление бонусов
            if enemy.bonus == 1:
                heart = Actor('heart')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Actor('sword')
                sword.pos = enemy.pos
                swords.append(sword)
            enemies.pop(enemy_index)

    #Столкновение второго регоря с врагами
    second_enemy_index = second_char.collidelist(second_enemies)
    if second_enemy_index != -1:
        second_char.x = second_old_x
        second_char.y = second_old_y
        colli = 1
        second_enemy = second_enemies[second_enemy_index]
        second_enemy.health -= second_char.attack
        second_char.health -= second_enemy.attack
        if second_enemy.health <= 0:
            second_experience += 100
            kills += 1
            #Добавление бонусов
            if second_enemy.bonus == 1:
                heart = Actor('heart')
                heart.pos = second_enemy.pos
                hearts.append(heart)
            elif second_enemy.bonus == 2:
                sword = Actor('sword')
                sword.pos = second_enemy.pos
                swords.append(sword)
            second_enemies.pop(second_enemy_index)
    

#Логика победы или поражения
def victory():
    global mode, win, level, max_h, max_ap, min_ap, min_h
    if kills >= 20 and level == 1:
        level +=1
        char.health = 120
        second_char.health = 120
    if level == 2:
        min_h = 15
        max_h = 20
        max_ap = 15
        min_ap = 10
    if experience >= 5000:
        mode = "end"
        win = 1
    elif second_experience >= 5000:
        mode = "end"
        win = 1
    if char.health <= 0 or second_char.health <= 0:
        mode = "end"
        win = -1
    


#Логика бонусов
def update(dt):
    global mode, win, enemies, hearts, swords, second_enemies, experience, second_experience, kills
    victory()
    for i in range(len(hearts)):
        if char.colliderect(hearts[i]):
            health_bonus = random.randint(10,20)
            char.health += health_bonus
            hearts.pop(i)
            break
        elif second_char.colliderect(hearts[i]):
            health_bonus = random.randint(10,20)
            second_char.health += health_bonus
            hearts.pop(i)
            break
        
    for i in range(len(swords)):
        if char.colliderect(swords[i]):
            sword_bonus = random.randint(5,15)
            char.attack += sword_bonus
            swords.pop(i)
            break
        elif second_char.colliderect(swords[i]):
            sword_bonus = random.randint(5,15)
            second_char.attack += sword_bonus
            swords.pop(i)
            break
    if len(enemies) <= 3:
            x = random.randint(1, 7) * cell.width
            y = random.randint(1, 7) * cell.height
            enemy = Actor("diamond", topleft = (x, y))
            enemy.health = random.randint(min_h, max_h)
            enemy.attack = random.randint(min_ap, max_ap)
            enemy.bonus = random.randint(0, 2)
            enemies.append(enemy)
    if len(second_enemies) <= 3:
            x = random.randint(1, 7) * cell.width
            y = random.randint(1, 7) * cell.height
            second_enemy = Actor("second_enemy", topleft = (x, y))
            second_enemy.health = random.randint(min_h, max_h)
            second_enemy.attack = random.randint(min_ap, max_ap)
            second_enemy.bonus = random.randint(0, 2)
            second_enemies.append(second_enemy)

    if mode == 'end' and keyboard.RETURN:
        mode = 'game'
        char.top = cell.height
        char.left = cell.width
        char.health = 100
        char.attack = 5
        enemies = []
        second_enemies = []
        second_char.top = cell.height
        second_char.left = cell.width * (size_w - 2) 
        second_char.health = 100
        second_char.attack = 5
        hearts = []
        swords = []   
        win = 0
        kills = 0
        enemies_draw()
        second_enemies_draw()
        experience = 0
        second_experience = 0
pgzrun.go()
