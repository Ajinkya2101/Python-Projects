student_heights = input("Enter the height of students: \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) 

total_heights = 0
for height in student_heights:
    total_heights += height
print(f"Total height = {total_heights}")

number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(f"Total= {number_of_students}")

avg_height= total_heights / number_of_students

print(f"Average Height= {avg_height}")
