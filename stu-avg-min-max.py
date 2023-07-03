
point = []
student_number = int(input("please enter number of students: "))

for i in range(student_number):
    point = int(input())

print("class average: " , sum(point) / student_number)
print("max score: " ,max(point) )
print("min score: " , min(point))