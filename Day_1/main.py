
#Python script for Day 1 challange

with open('elfcal.txt') as file:
    elf = [i for i in file.read().strip().split("\n")]

#print(elf)

#Time for the real calculations!

cal = 0 #Elf with highest calories
cal2 = 0 #Elf with second highest calories
cal3 = 0 #Elf with third highest calories
count = 0

for item in elf:
    if item == '':
        count = 0
    else:
        calNum = int(item)
        count += calNum

    if count > cal:
        cal = count
    elif count > cal2:
        cal2 = count
    elif count > cal3:
        cal3 = count

print("Elf with the most calories:", cal, "(part 1)")

print("The sum of calories carried by top 3 elves is: ", cal+cal2+cal3, "(part 2)")