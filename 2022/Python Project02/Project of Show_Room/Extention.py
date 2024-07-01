with open('Freez.txt') as f:
    line_num = 0
    for a in f:
        if a.find('5051002') !=-1: # 'c' is found in the line
            a=line_num          
            break      
    line_num += 1
file = open('Freez.txt', 'r')
lines = file.readlines()
print(lines[a])
print(lines[a+1])
print(lines[a+2])
file.close()
