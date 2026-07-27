"""
EXERCISE 2:

Agrupar empleados por departamento
Dada una lista de empleados donde cada uno tiene nombre, correo y departamento,
cree un diccionario que agrupe los empleados por su departamento:
Ejemplo:
Entrada:

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
"""

print (" \nEXERCISE 2:\n\n")
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
departments = {}
for employee in employees:
    department = employee['department']
    if department not in departments:
        departments[department] = []
    departments[department].append(employee['name'])

for department, employee in departments.items():
    print (f"{department}: {employee}")

