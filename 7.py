print("Задание 7.1")
import random


def labirint():

    vihodi = random.randint(1,10)
    plotnost = random.random()
    razmer = random.randint(10,20)

    maze = []
    spisok = []

    for i in range(razmer):
        spisok.append(" ")
    for i in range(razmer):
        maze.append(spisok.copy())


    grani = []

    for i in range(razmer):
        maze[0][i] = "#"
        grani.append([0,i])
    for i in range(razmer):
        maze[i][razmer-1] = "#"
        grani.append([i, razmer-1])
    for i in range(razmer):
        maze[razmer-1][i] = "#"
        grani.append([razmer-1, i])
    for i in range(razmer):
        maze[i][0] = "#"
        grani.append([i, 0])
    copygrani = []


    d = 1
    coordvihod = []

    while d <= vihodi:
        a = random.choice(grani)
        maze[a[0]][a[1]] = " "
        coordvihod.append(a)
        grani.remove(a)
        d = d + 1

    dopshans = abs((plotnost - random.random())/15)
    if plotnost == 1:
        dopshans = 0

    postavili = False
    for i in range(1,razmer-1):
        for e in range(1,razmer-1):
            uvelichenie = False
            shans = plotnost
            if ([i+1, e] in coordvihod or [i-1, e] in coordvihod or [i, e+1] in coordvihod or [i, e-1] in coordvihod) and plotnost != 1:  # не ставим стены рядом с выходом
                continue
            else:
                if postavili:
                    shans = plotnost - dopshans
                if maze[i+1][e] == "#" and postavili is False:
                    uvelichenie = True
                postavili = False
                if uvelichenie:
                    shans = plotnost + dopshans
                if random.random() <= shans:
                    maze[i][e] = "#"
                    postavili = True

    return maze, coordvihod


print("Задание 7.2")



def print_maze(maze):
    yi = 0
    while yi < len(maze):
        print("".join(maze[yi]).replace("#", "#"))
        yi += 1

def validate_input(maze):
    x = input("Введите значение x ")
    y = input("Введите значение y ")
    izmenit = False
    dllina = len(maze)


    if x.isdigit() is False:
        print("x - не число")
        izmenit = True
    if y.isdigit() is False:
        print("y - не число")
        izmenit = True
    if int(x) >= dllina or x == "":
        print("недопустимое значение x")
        izmenit = True
    if int(y) >= dllina or y == "":
        print("недопустимое значение y")
        izmenit = True

    x = int(x)
    y = int(y)

    if izmenit is False:
        if maze[y][x] == '#':
            print("Начальная координата - стена")
            izmenit = True

    if izmenit is True:
        vozm_coord = []
        for i in range(len(maze)):
            for e in range(len(maze)):
                if maze[i][e] == " ":
                    vozm_coord.append([i,e])
    else:
        return [y,x]

    coord = random.choice(vozm_coord)


    return coord

labir, vihod = labirint()
y,x = validate_input(labir)



print("3a - координаты начальной точки (y,x)", "-", (y,x))
print("3b")


g = 1
for i in vihod:
    print("Выход", g, "-", i)
    g = g + 1



print("3c")


if [y,x] in vihod:
    if y ==0:
        if labir[y+1][x] == " ":
            labir[y+1][x] = "1"
    elif y == len(labir)-1:
        if labir[y-1][x] == " ":
            labir[y-1][x] = "1"
    elif x ==0:
        if labir[y][x+1] == " ":
            labir[y][x+1] = "1"
    elif x == len(labir)-1:
        if labir[y][x-1] == " ":
            labir[y][x-1] = "1"




labir[y][x] = "0"
labir_copy = []

for i in labir:
    labir_copy.append(i.copy())
labir_copy[y][x] = "0"

dlinlabir = len(labir)

a = False
def iskatimenat():
    global a
    global labir
    global dlinlabir

    i = 1
    while i <= (dlinlabir-1)*2:
        for coordy in range(1,dlinlabir-1):
            for coordx in range(1,dlinlabir-1):
                if labir[coordy][coordx].isdigit() is True:
                    znach = int(labir[coordy][coordx])

                    if labir[coordy-1][coordx].isdigit():
                        if int(labir[coordy - 1][coordx]) > int(labir[coordy][coordx]):
                            labir[coordy - 1][coordx] = str(znach + 1)
                    if labir[coordy + 1][coordx].isdigit():
                        if int(labir[coordy + 1][coordx]) > int(labir[coordy][coordx]):
                            labir[coordy + 1][coordx] = str(znach + 1)
                    if labir[coordy][coordx + 1].isdigit():
                        if int(labir[coordy][coordx + 1]) > int(labir[coordy][coordx]):
                            labir[coordy][coordx + 1] = str(znach + 1)
                    if labir[coordy][coordx - 1].isdigit():
                        if int(labir[coordy][coordx - 1]) > int(labir[coordy][coordx]):
                            labir[coordy][coordx - 1] = str(znach + 1)

                    if labir[coordy - 1][coordx] == " ":
                        labir[coordy - 1][coordx] = str(znach + 1)
                    if labir[coordy + 1][coordx] == " ":
                        labir[coordy + 1][coordx] = str(znach + 1)
                    if labir[coordy][coordx - 1] == " ":
                        labir[coordy][coordx - 1] = str(znach + 1)
                    if labir[coordy][coordx + 1] == " ":
                        labir[coordy][coordx + 1] = str(znach + 1)

        i = i +1

iskatimenat()

l = 0
for i in vihod:
    y1,x1 = i
    l = l + 1
    if labir[y1][x1].isdigit():
        print("Выход", l, "- да")
    else:
        print("Выход", l, '- нет')



print("3d")



a = []

for i in range(0,dlinlabir):
    if labir[0][i].isdigit():
        a.append([0,i])
for i in range(0,dlinlabir):
    if labir[i][dlinlabir-1].isdigit():
        a.append([i,dlinlabir-1])
for i in range(0,dlinlabir):
    if labir[dlinlabir-1][i].isdigit():
        a.append([dlinlabir-1,i])
for i in range(0,dlinlabir):
    if labir[i][0].isdigit():
        a.append([i,0])

def vihoda(a):
    y, x = a
    pyti = [a]

    while True:
        if y - 1 >= 0:
            if labir[y - 1][x].isdigit():
                if int(labir[y - 1][x]) < int(labir[y][x]):
                    y = y-1
                    pyti.append([y,x])
        if y + 1 < len(labir):
            if labir[y + 1][x].isdigit():
                if int(labir[y + 1][x]) < int(labir[y][x]):
                    y = y+1
                    pyti.append([y,x])
        if x - 1 >= 0:
            if labir[y][x - 1].isdigit():
                if int(labir[y][x - 1]) < int(labir[y][x]):
                    x = x-1
                    pyti.append([y,x])
        if x + 1 < len(labir):
            if labir[y][x + 1].isdigit():
                if int(labir[y][x + 1]) < int(labir[y][x]):
                    x = x+1
                    pyti.append([y,x])

        if labir[y][x] == "0":
            break

    return pyti

vihodi = []

for i in a:
    vihodi.append(vihoda(i))

g = []
for i in range(len(vihodi)):
    g.append(len(vihodi[i]))






if len(vihodi) != 0:
    d = 0
    while d < len(g):
        if g[d] == min(g):
            nomervihod = d
            break
        d = d + 1
    print("Кратчайший путь из начальной точки", (y, x), " – ", min(g) - 1, " шагов до выхода в", (vihodi[nomervihod][0][0],vihodi[nomervihod][0][1]))

    for i in vihodi[nomervihod]:
        y,x = i
        labir_copy[y][x] = "+"


else:
    print("ни до одного выхода нельзя добраться")



print("3e")


v = 0
if len(vihodi) != 0:
    for i in range(len(g)):
        v = v + 1
        for e in vihodi[i]:
            y, x = e
            labir_copy[y][x] = "+"
        print("Выход", v, "-", g[i]-1, "Шагов")
else:
    print("ни до одного выхода нельзя добраться")

labir_copy[y][x] = "0"


print_maze(labir_copy)
