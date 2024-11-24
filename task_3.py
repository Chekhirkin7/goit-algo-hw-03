import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та символу '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())
    
    # Якщо номер починається з '+', залишаємо тільки допустимі символи
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+380'):
            return cleaned_number  # Номер вже має міжнародний код України
        else:
            return cleaned_number  # Інші міжнародні коди залишаємо без змін
    else:
        # Якщо номер починається з '380', додаємо '+'
        if cleaned_number.startswith('380'):
            return '+' + cleaned_number
        # Якщо номер не має коду, додаємо код України '+38'
        else:
            return '+38' + cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
