# Python3.0

# FIRST COL
# A = Rock
# B = Paper
# C = Scissors

# SECOND COL
# X = Rock
# Y = Paper
# Z = Scissors

with open('data.txt') as file:
    data = [i for i in file.read().replace(',','').replace(" ","")]
print(data)



def meCalc(you,me):
    if you == 'A' and me == 'Y':
        score += 8
    elif me == 'Y':
        score + y
    elif me == 'Z':
        score + z

    myScore = sum(x,y,z)

    return myScore
