"""
EXERCISE 5 - Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
"""

NOTE_COUNTER = 1
PASSED_COUNT = 0
FAILED_COUNT = 0
PASSED_AVERAGE = 0
FAILED_AVERAGE = 0
TOTAL_AVERAGE = 0

TOTAL_NOTES = int(input("Enter the total number of grades: "))

while NOTE_COUNTER <= TOTAL_NOTES:
    CURRENT_NOTE = int(input("Enter grade number " + str(NOTE_COUNTER) + ": "))
    if CURRENT_NOTE < 70:
        FAILED_COUNT = FAILED_COUNT + 1
        FAILED_AVERAGE = FAILED_AVERAGE + CURRENT_NOTE
    else:
        PASSED_COUNT = PASSED_COUNT + 1
        PASSED_AVERAGE = PASSED_AVERAGE + CURRENT_NOTE
    TOTAL_AVERAGE = TOTAL_AVERAGE + (CURRENT_NOTE / TOTAL_NOTES)
    NOTE_COUNTER = NOTE_COUNTER + 1

if FAILED_COUNT > 0:
    FAILED_AVERAGE = FAILED_AVERAGE / FAILED_COUNT
else:
    FAILED_AVERAGE = 0

if PASSED_COUNT > 0:
    PASSED_AVERAGE = PASSED_AVERAGE / PASSED_COUNT
else:
    PASSED_AVERAGE = 0

print("The student has this number of passed grades: " + str(PASSED_COUNT))
print("This is the average of passed grades: " + str(PASSED_AVERAGE))
print("The student has this number of failed grades: " + str(FAILED_COUNT))
print("This is the average of failed grades: " + str(FAILED_AVERAGE))
print("This is the total average of grades: " + str(TOTAL_AVERAGE))