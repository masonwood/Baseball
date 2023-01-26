while True:
    HR = 0
    BB = 0
    HBP = 0
    K = 0
    IP = 0
    C = 3.15
    name = input('Enter Name: ')
    HR = int(input('Enter the amount of homeruns: '))
    BB = int(input('Enter the amount of walks: '))
    HBP = int(input('Enter the amount of batters hit: '))
    K = int(input('Enter the amount of strikeouts: '))
    IP = int(input('Enter the amount of innings pitched: '))
    FIP = (13*HR + 3*(BB + HBP) - 2*K)/IP + C
    print(FIP)
    with open('fipname.txt', 'w') as f:
        f.write(f'\n Player: {name} | FIP: {FIP}')
        break