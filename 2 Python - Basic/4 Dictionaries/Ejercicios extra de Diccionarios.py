"""
EXERCISE 1:

Dada una lista de ventas con la siguiente información:
date
customer_email
items

Y cada item teniendo la siguiente información:
name
upc
unit_price

Cree un diccionario que guarde el total de ventas de cada UPC.
Ejemplos:

Entrada:
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

Salida:
result = {
	'ITEM-453': 131.52,
	'ITEM-324': 32.45,
	'ITEM-432': 30.08,
	'ITEM-23': 8.84,
}
"""

print (" \nEXERCISE 1:\n\n")
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
sales_total ={}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        if upc not in sales_total:
            sales_total[upc] = item['unit_price']
        else:
            sales_total[upc] += item['unit_price']

for item, price in sales_total.items():
    print (f"{item}: {price},")

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

"""
EXERCISE 3:

Dada una lista de productos vendidos, donde cada uno tiene categoría y precio,
cree un diccionario que acumule el total por categoría.
Ejemplo:
Entrada:
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
"""

print (" \nEXERCISE 3:\n\n")
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
total_per_category = {}
for product in products:
    category = product['category']
    if category not in total_per_category:
        total_per_category[category] = product['price']
    else:
        total_per_category[category] += product['price']

for category, price in total_per_category.items():
    print (f"{category}: {price}")