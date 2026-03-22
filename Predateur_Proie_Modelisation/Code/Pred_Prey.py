import time
import pygame
import numpy as np
import random
from matplotlib import pyplot as plt

#Color setup
#COLOR_BASE = (0,0,0)
COLOR_BASE = (128,128,128)
#COLOR_BG = (0,100,0)
COLOR_BG = (255,255,255)
COLOR_SHEEP = (0, 0, 255)
COLOR_WOLF = (255, 0, 0)
#COLOR_OBSTACLE = (105,105,105)
COLOR_OBSTACLE = (0,0,0)

SIZE = (45,55)
#SIZE = (50,50)


def update(screen, cells, list_SHEEP, list_WOLF, SHEEP_BREED, WOLF_BREED, WOLF_STARVE, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            updated_cells[i][j] = cells[i][j]
    if with_progress:
        #Sheep move
        list_birth = []
        for i_sheep in range(len(list_SHEEP)):
            x,y,breed = list_SHEEP[i_sheep]
            voisin_sheep = neighborhood(updated_cells,(x,y),True,False)

            if len(voisin_sheep)!=0:
                x_dep, y_dep = random.choice(voisin_sheep)
                updated_cells[x][y] = 0
                updated_cells[x_dep][y_dep] = 1

                if breed == SHEEP_BREED-1:
                    voisin_sheep = neighborhood(updated_cells, (x_dep, y_dep), True, False)
                    if len(voisin_sheep) != 0:
                        x_born, y_born = random.choice(voisin_sheep)
                        updated_cells[x_born][y_born] = 1
                        list_birth.append((x_born, y_born))
                        breed = 0
                else:
                    breed += 1
                list_SHEEP[i_sheep] = (x_dep, y_dep,breed)
            else:
                if breed != SHEEP_BREED-1:
                    breed += 1
                list_SHEEP[i_sheep] = (x, y, breed)
        for x_b, y_b in list_birth:
            list_SHEEP.append((x_b,y_b,0))
        #Wolf move
        for i_wolf in range(len(list_WOLF)):
            eaten = False
            x,y,breed,starve = list_WOLF[i_wolf]
            voisin_wolf = neighborhood(updated_cells,(x,y),False,True)

            if len(voisin_wolf)!=0:
                x_dep, y_dep = random.choice(voisin_wolf)
                if updated_cells[x_dep][y_dep] == 1:
                    eaten = True
                    for i_sheep in range(len(list_SHEEP)):
                        x_sheep, y_sheep,_ = list_SHEEP[i_sheep]
                        if x_sheep == x_dep and y_sheep == y_dep:
                            list_SHEEP.remove(list_SHEEP[i_sheep])
                            break


                updated_cells[x][y] = 0
                updated_cells[x_dep][y_dep] = -1

                if breed == WOLF_BREED-1:
                    voisin_wolf = neighborhood(updated_cells, (x_dep, y_dep), False, True)
                    if len(voisin_wolf) != 0:
                        x_born, y_born = random.choice(voisin_wolf)
                        updated_cells[x_born][y_born] = -1
                        list_WOLF.append((x_born, y_born,0,starve))
                        breed = 0
                else:
                    breed += 1

                if eaten:
                    starve = 0
                    list_WOLF[i_wolf] = (x_dep, y_dep, breed, starve)
                else:
                    if starve == WOLF_STARVE-1:
                        updated_cells[x_dep][y_dep] = 0
                        list_WOLF[i_wolf] = (-1, -1, -1, -1)

                    else:
                        starve += 1
                        list_WOLF[i_wolf] = (x_dep, y_dep, breed, starve)
            else:
                if breed == WOLF_BREED-1:
                    voisin_wolf = neighborhood(updated_cells, (x, y), False, True)
                    if len(voisin_wolf) != 0:
                        x_born, y_born = random.choice(voisin_wolf)
                        updated_cells[x_born][y_born] = -1
                        list_WOLF.append((x_born, y_born,0,starve))
                        breed = 0
                else:
                    breed += 1

                if starve == WOLF_STARVE-1:
                    updated_cells[x][y] = 0
                    for i_wolf_live in range(len(list_WOLF)):
                        x_wolf, y_wolf, _, _ = list_WOLF[i_wolf_live]
                        if x_wolf == x and y_wolf == y:
                            list_WOLF[i_wolf_live] = (-1, -1, -1, -1)
                            break
                elif not eaten:
                    starve += 1
                    list_WOLF[i_wolf] = (x, y, breed, starve)

        while (-1, -1, -1, -1) in list_WOLF:
            list_WOLF.remove((-1, -1, -1, -1))







    for row, col in np.ndindex(cells.shape):
                
        if updated_cells[row, col] == 0:
            color = COLOR_BG
        elif updated_cells[row, col] == 1:
            color = COLOR_SHEEP
        elif updated_cells[row, col] == -1:
            color = COLOR_WOLF
        elif updated_cells[row, col] == -2:
            color = COLOR_OBSTACLE


        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updated_cells

'''def neighborhood(cells,coords,is_sheep,is_wolf):
    x, y = coords
    voisin = []
    voisin_sheep = []
    voisin_wolf = []
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if (max(abs(x-i),abs(y-j))==1) and (max(abs(x-i),abs(y-j)) == 1):
                voisin.append((i,j))
    for x_voisin, y_voisin in voisin:
        if cells[x_voisin][y_voisin] == 0:
            voisin_sheep.append((x_voisin,y_voisin))
            voisin_wolf.append((x_voisin, y_voisin))
        elif is_wolf:
            if cells[x_voisin][y_voisin] == 1:
                voisin_wolf.append((x_voisin, y_voisin))
    if is_wolf:
        return voisin_wolf
    elif is_sheep:
        return voisin_sheep
'''




def neighborhood(cells,coords,is_sheep,is_wolf):
    x, y = coords
    voisin = []
    if is_sheep:
        if x != 0 and cells[x-1][y] == 0:
            voisin.append((x-1,y))
        if y != 0 and cells[x][y-1] == 0:
            voisin.append((x,y-1))
        if x != len(cells)-1 and cells[x+1][y] == 0:
            voisin.append((x+1,y))
        if y != len(cells[0])-1 and cells[x][y+1] == 0:
            voisin.append((x,y+1))
    elif is_wolf:
        if x != 0 and cells[x-1][y] >= 0:
            voisin.append((x-1,y))
        if y != 0 and cells[x][y-1] >= 0:
            voisin.append((x,y-1))
        if x != len(cells)-1 and cells[x+1][y] >= 0:
            voisin.append((x+1,y))
        if y != len(cells[0])-1 and cells[x][y+1] >= 0:
            voisin.append((x,y+1))
    return voisin

def compte(cells):
    res = [0,0]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j] == 1:
                res[0] += 1
            if cells[i][j] == -1:
                res[1] += 1
    return res
def main():
    pygame.init()
    y, x = SIZE
    loop = True
    # Sheep/Wolf proportion
    SHEEP = 250
    WOLF = 50
    OBSTACLE = 50

    SHEEP_BREED = 3
    WOLF_BREED = 8
    WOLF_STARVE = 3
    screen = pygame.display.set_mode((x*10, y*10))

    cells = np.zeros(SIZE)
    list_SHEEP = []
    list_WOLF = []
    count_SHEEP = []
    count_WOLF = []
    screen.fill(COLOR_BASE)
    update(screen, cells,list_SHEEP, list_WOLF,SHEEP_BREED, WOLF_BREED,WOLF_STARVE, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False


    while loop:

        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                while SHEEP > 0:
                    i = random.randint(0, y - 1)
                    j = random.randint(0, x - 1)
                    sheep_breed = random.randint(0, SHEEP_BREED-1)
                    if cells[i][j] == 0:
                        cells[i][j] = 1
                        list_SHEEP.append((i,j,sheep_breed))
                        SHEEP = SHEEP - 1
                while WOLF > 0:
                    i = random.randint(0, y - 1)
                    j = random.randint(0, x - 1)
                    wolf_breed = random.randint(0, WOLF_BREED-1)
                    wolf_starve = random.randint(0, WOLF_STARVE- 1)
                    if cells[i][j] == 0:
                        cells[i][j] = -1
                        list_WOLF.append((i, j, wolf_breed, wolf_starve))
                        WOLF = WOLF - 1
                while OBSTACLE > 0:
                    i = random.randint(0, y - 1)
                    j = random.randint(0, x - 1)
                    if cells[i][j] == 0:
                        cells[i][j] = -2
                        OBSTACLE = OBSTACLE-1
                update(screen, cells,list_SHEEP, list_WOLF,SHEEP_BREED, WOLF_BREED,WOLF_STARVE, 10)
                pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not running:
                    running = not running
                    update(screen, cells,list_SHEEP, list_WOLF,SHEEP_BREED, WOLF_BREED,WOLF_STARVE, 10)
                    pygame.display.update()
                elif event.key == pygame.K_SPACE and running:
                    loop = False

        if running:
            count_SHEEP.append(compte(cells)[0])
            count_WOLF.append(compte(cells)[1])
            cells = update(screen, cells,list_SHEEP, list_WOLF,SHEEP_BREED, WOLF_BREED,WOLF_STARVE, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)
    list_time = [t for t in range(len(count_SHEEP))]
    plt.plot(list_time,count_SHEEP,color="blue",label="Prey")
    plt.plot(list_time, count_WOLF,color="red",label="Predateur")
    plt.plot([list_time[np.argmax(count_WOLF)],list_time[np.argmax(count_WOLF)]],[0,2000])



    plt.title("Pred vs Prey")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()
    pygame.quit()
    '''list_time = [t for t in range(len(count_SHEEP))]
    # plt.plot(list_time,count_SHEEP,color="blue",label="Prey")
    # plt.plot(list_time, count_WOLF,color="red",label="Predateur")
    # plt.plot([list_time[np.argmax(count_WOLF)],list_time[np.argmax(count_WOLF)]],[0,2000])
    iter_list = [96.4,41.8,31,30.4,30]
    propor = [i for i in range(1,6)]
    plt.plot(propor, iter_list, color="Grey")
    plt.title("Pred vs Prey")
    plt.xlabel("Temp de reproduction")
    plt.ylabel("Itéation")
    plt.legend()
    plt.show()
    pygame.quit()'''

if __name__ == '__main__':
    main()