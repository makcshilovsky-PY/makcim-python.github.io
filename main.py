import requests
# import json
# import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_base1_label(_event):
    code = base1_combobox.get()
    name = currencies[code]
    base1_label.config(text=name)
    # print("Выбрана базовая валюта 1:", code, name)


def update_base2_label(_event):
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)
    # print("Выбрана базовая валюта 2:", code, name)


def update_target_label(_event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)
    # print("Выбрана целевая валюта:", code, name)


def exchange():
    # code = entry.get().strip().upper()
    target_code = target_combobox.get()
    base1_code = base1_combobox.get()
    base2_code = base2_combobox.get()

    if target_code and base1_code and base2_code:
        try:
            # Запрос для первой базовой валюты
            res1 = requests.get(f"https://open.er-api.com/v6/latest/{base1_code}")
            res1.raise_for_status()
            # data1 = json.loads(res1.text)
            data1 = res1.json()
            # print("Ответ API 1:", data1)

            # Запрос для второй базовой валюты
            res2 = requests.get(f"https://open.er-api.com/v6/latest/{base2_code}")
            res2.raise_for_status()
            # data2 = json.loads(res2.text)
            data2 = res2.json()
            # print("Ответ API 2:", data2)

            if target_code in data1['rates'] and target_code in data2['rates']:
                rate1 = data1['rates'][target_code]
                rate2 = data2['rates'][target_code]

                base1_name = currencies[base1_code]
                base2_name = currencies[base2_code]
                target_name = currencies[target_code]

                # print(f"Курс 1: 1 {base1_name} = {rate1} {target_name}")
                # print(f"Курс 2: 1 {base2_name} = {rate2} {target_name}")

                msg = (f"Курсы обмена относительно {target_name}:\n\n"
                       f"1 {base1_name} = {rate1:.2f} {target_name}\n"
                       f"1 {base2_name} = {rate2:.2f} {target_name}")

                mb.showinfo(title='Курсы обмена', message=msg)
            else:
                mb.showerror(title='Ошибка', message=f'Валюта {target_code} не найдена')
        except Exception as e:
            # print("Ошибка при запросе:", e)
            mb.showerror(title='Ошибка', message=f'error 400 {e}')
    else:
        mb.showwarning(title='Внимание', message='Выберите все валюты из списка!')


currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "GBP": "Британский фунт стерлингов",
    "JPY": "Японская иена",
    "CHF": "Швейцарский франк",
    "KZT": "Казахстанский тенге",
    "BYN": "Белорусский рубль",
    "TRY": "Турецкая лира",
    "AED": "Дирхам ОАЭ",
    "GEL": "Грузинский лари",
    "AMD": "Армянский драм",
    "KGS": "Киргизский сом",
    "UZS": "Узбекский сум",
    "CAD": "Канадский доллар",
    "AUD": "Австралийский доллар",
    "INR": "Индийская рупия",
    "THB": "Тайский бат",
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY', 'GBP', 'KZT', 'BYN', 'AED', 'TRY']

root = Tk()
# root.title("Курс валют по отношению к доллару США")
root.title("Курсы обмена валют")
root.geometry("320x380")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use('classic')

# Первая базовая валюта
Label(root, text='Базовая валюта', bg="#f0f0f0", fg="black").pack(pady=(10, 2))
base1_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base1_combobox.pack()
base1_combobox.bind("<<ComboboxSelected>>", update_base1_label)

base1_label = Label(root, bg="#f0f0f0", fg="black")
base1_label.pack(pady=2)

# Вторая базовая валюта
Label(root, text='Вторая базовая валюта', bg="#f0f0f0", fg="black").pack(pady=(10, 2))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.pack()
base2_combobox.bind("<<ComboboxSelected>>", update_base2_label)

base2_label = Label(root, bg="#f0f0f0", fg="black")
base2_label.pack(pady=2)

# Целевая валюта
Label(root, text='Целевая валюта', bg="#f0f0f0", fg="black").pack(pady=(10, 2))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack()
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = Label(root, bg="#f0f0f0", fg="black")
target_label.pack(pady=2)

# entry = Entry(width=10)
# entry.pack()

button = Button(root, text='Получить курс обмена', command=exchange, highlightbackground="#f0f0f0")
button.pack(pady=15)

root.mainloop()