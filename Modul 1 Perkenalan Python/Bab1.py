nilai = int(input("Inputkan nilaimu: "))

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "AB"
elif nilai >= 70:
    grade = "B"
else:
    grade = "C"

print("Grade: %s" % grade)
