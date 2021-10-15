# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(student_heights)
total = 0 
how_many = 0

for count in student_heights:
  how_many += 1
print(how_many)
  

for height in student_heights:
  total+= height
print(total)
print(round(total / how_many))



