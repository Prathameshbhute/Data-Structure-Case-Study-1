
# Student Performance Ranking System
# Using Divide and Conquer - Merge Sort

def merge_sort(students):
    if len(students) <= 1:
        return students

    # Divide
    mid = len(students) //2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    # Combine
    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        # Sort by marks: highest to lowest
        if left[0][1] >= right[0][1]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


# Input student details
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students.append((name, marks))

# Sort students
ranked_students = merge_sort(students)

# Display ranking
print("\n--- Student Merit List ---")
for rank, student in enumerate(ranked_students, start=1):
    print(rank, student[0], ":-", student[1], "marks")