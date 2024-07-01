#problem 1
# Check a specific word is present or not in a txt file
'''with open ('nn.txt','r') as file:
    x=file.read()
    if 'Nur' in x:
        print("Nur is present in the nn.txt")
    else:
        print("Nur is not present in the nn.txt")'''
# Create a function wich return a integer and create a txt file if integer is getter the the old value replace the old value with new value:
'''def game(a):
    score=a*10
    return score
M=int(input("Enter the number"))
N=game(M)


with open ('highscore.txt','r') as file:
   R=file.read()
   H=int(R)

if N>H:
    with open ('highscore.txt','w') as file2:
        file2.write(str(N))
else:
    pass'''
# write a python program to write multiplacitao n table 2 to 10 in defferent document
'''for i in range(2,21):
    with open(f'Multipalction taples\multiplaction table of {i}.txt','w') as file:
        for j in range(1,11):
            file.write(f'{i}*{j}={i*j}\n')'''
# write a python prgram to replace or adite some specific text froma a txt document

'''with open('rep.txt','r') as file:
    x=file.read()
    x=x.replace("bad","GOOD")
    x=x.replace("not","OBEYES")
    print(x)
with open('rep.txt','w') as file2:
    file2.write(x)'''

# write a python prgram to replace or adite some specific text wich is given to a list and if the text are present int he txt file replace them with "NONE" from a txt document
'''words=["mota","kalo","olosh"]
with open ('rep2.txt','r') as file:
    Reader=file.read()
for word in words:
    Readerupdate=Reader.replace(word,"NONE")
    with open('rep2.txt','w') as file:
        file.write(Readerupdate)'''
# write a python program to find a specific word in log file and get the line number
'''with open ('log.txt','r') as file:
    reader=file.read().lower()

if "nahid" in reader:
    print("Nahid is present in the log file")
else:
    print("Nahid is not present in the log file")'''
NNN=True
LN=1
with open('log.txt','r') as file:
    
    while NNN:
        LN=LN+1
        NNN=file.readline().lower()
        if 'python' in NNN:
            print(f"Yes python is present in line number {LN}")
            #break/continue ব্যবহার করতে পরি



    


    


























