Student_List =["Nahid Isalm", "Akhy Islam", "Fahamida Akter", "Sohev Akhter"]


#print(Student_List[-1])
#print(Student_List [0])
#print(Student_List[1])

# Add A New Item in A list---------
Student_List.append("Rani Roy")
#print(Student_List)
Student_List.insert(3,"Binoy Kishor")
#print(Student_List)



# Deleting A Item from the list------

#Student_List.pop()
#print(Student_List)
Student_List.remove("Akhy Islam")
#print(Student_List)

#Getting The length Of a value-------
#print(len(Student_List))

Student_Roll = ["21661012","21661013","21661014","21661015"]
Student_List.extend(Student_Roll)
#print(Student_List)
#print(len(Student_List))
print("21661012" not in (Student_List))

