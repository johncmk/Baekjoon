n = int(input())

grade = ""

if 90 <= n <= 100:
    grade = "A"
elif 80 <= n <= 89:
    grade = "B"
elif 70 <= n <= 79:
    grade = "C"
elif 60 <= n <= 69:
    grade = "D"
else:
    grade = "F"

print(grade)