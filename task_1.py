from datetime import datetime

def get_days_from_today(date):
	#Перевірка на коректність даних
	try:
		date_obj = datetime.strptime(date, "%Y-%m-%d").date()
	except ValueError:
		print("Введіть дату в форматі 'РРРР-ММ-ДД'") #Повідомлення у разі некоректно введених даних
		return None #Програма нічого не повертає у разі ValueError
	
	date_now = datetime.today().date() #Отримання поточної дати, без часу

	result = (date_obj - date_now).days #Обчислення 

	return result #Виведення результату у днях

print(f"Результат: {get_days_from_today("2024-12-10")}") #Виклик функції




#Варіант програми, де користувач сам вводить дату
#date = input("Введіть Вашу дату у форматі 'РРРР-ММ-ДД': ") #Введення дати користувачем

#def get_days_from_today(date):
	#Перевірка на коректність даних
	#try:
		#date_obj = datetime.strptime(date, "%Y-%m-%d").date()
	#except ValueError:
		#print("Введіть дату в форматі 'РРРР-ММ-ДД'") #Повідомлення у разі некоректно введених даних
		#return #Програма зупиняється у разі ValueError
	
	#date_now = datetime.today().date() #Отримання поточної дати, без часу

	#result = date_obj - date_now #Обчислення різниці між поточною датою та заданою датою

	#return print (f"Результат: {result.days}") #Виведення результату у днях

#get_days_from_today(date) #Виклик функції
