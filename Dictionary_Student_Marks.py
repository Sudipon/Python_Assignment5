Dict1 = {'Alice': 85, 'Morish': 90, 'Rebecca': 87, 'timur': 80}
a = input("Enter the Student's Name: ")
if a in Dict1.keys():
    print(a + "'s marks:",Dict1[a])
else:
    print("Student not found.")