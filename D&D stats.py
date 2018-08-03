import os, random

while True:
    Stats = {'Strength': [10,0], 'Dexterity': [10,0], 'Constitution': [10,0], 'Intelligence': [10,0], 'Wisdom': [10,0], 'Charisma': [10,0]}
    #, 'AC': 0, 'Hp': 10

    for a in Stats:
        #print(a)
        q = random.randrange(1,21)
        if q <= 3:
            q += random.randrange(1,7)
        #m = random.randrange(1,21)
        #if m > q:
        #    q = m
        #m = random.randrange(1,21)
        #if m > q:
        #    q = m

        #q = q+1
        zbq = -5
        #print(q)
        for x in range(0, 22, 2):
            #print(zbq+int(x/2))
            if (q == (x + 0)) or (q == (x + 1)):
                Stats[a] = [q, zbq + int(x/2)]
                #print(Stats[a])
                #print(Stats[a])
        #else:
        #    print(x)

    Stats["HP"] = 10 + Stats["Constitution"][1]
    nmn = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma','HP']
    for a in nmn:
        print(a+ ' '+str(Stats[a]),end=', ')
    input()
