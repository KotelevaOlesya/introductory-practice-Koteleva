# Модуль 3. Функции (def, параметры, return)
# Выполнено 5 упражнений

# --------------------------------------------------
# Упражнение 1. calculate_profit() — прибыль
# --------------------------------------------------
def calculate_profit(revenue, costs):
    """Возвращает прибыль = выручка - затраты"""
    return revenue - costs

print("--- Упражнение 1: Прибыль ---")
print(f"Прибыль (100, 70): {calculate_profit(100, 70)}")
print(f"Прибыль (500, 620): {calculate_profit(500, 620)}")
print(f"Прибыль (0, 50): {calculate_profit(0, 50)}")
print()

# --------------------------------------------------
# Упражнение 2. calculate_vat() — НДС
# --------------------------------------------------
def calculate_vat(price, vat_rate=20):
    """Возвращает сумму НДС"""
    return price * vat_rate / 100

print("--- Упражнение 2: НДС ---")
print(f"НДС (1000 руб., ставка 20%): {calculate_vat(1000)} руб.")
print(f"НДС (500 руб., ставка 10%): {calculate_vat(500, 10)} руб.")
print()

# --------------------------------------------------
# Упражнение 3. get_category() — категория бизнеса
# --------------------------------------------------
def get_category(revenue):
    """Возвращает категорию бизнеса по выручке (млн руб.)"""
    if revenue < 1:
        return "Микробизнес"
    elif revenue < 10:
        return "Малый"
    elif revenue < 100:
        return "Средний"
    else:
        return "Крупный"

print("--- Упражнение 3: Категория бизнеса ---")
print(f"Выручка 0.5 млн → {get_category(0.5)}")
print(f"Выручка 5 млн → {get_category(5)}")
print(f"Выручка 50 млн → {get_category(50)}")
print(f"Выручка 200 млн → {get_category(200)}")
print()

# --------------------------------------------------
# Упражнение 4. compound_interest() — сложный процент
# --------------------------------------------------
def compound_interest(capital, rate, years):
    """Возвращает итоговую сумму по вкладу"""
    return capital * (1 + rate / 100) ** years

print("--- Упражнение 4: Сложный процент ---")
print(f"Капитал 1000, ставка 5%, 3 года: {compound_interest(1000, 5, 3):.2f} руб.")
print(f"Капитал 1000, ставка 5%, 5 лет: {compound_interest(1000, 5, 5):.2f} руб.")
print(f"Капитал 1000, ставка 5%, 10 лет: {compound_interest(1000, 5, 10):.2f} руб.")
print()

# --------------------------------------------------
# Упражнение 5. apply_discount() — скидка
# --------------------------------------------------
def apply_discount(price, discount_percent):
    """Возвращает новую цену после скидки"""
    return price * (1 - discount_percent / 100)

prices = [1000, 2500, 3700, 500, 8900]
discount = 15

print(f"--- Упражнение 5: Скидка {discount}% ---")
for original_price in prices:
    new_price = apply_discount(original_price, discount)
    print(f"{original_price} руб. → {new_price:.2f} руб.")