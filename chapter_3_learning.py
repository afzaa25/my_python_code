password_one = {
    'acebook_password': 'password123',
    'acebook_added': '22/03/02',
}

#Option 1: Add another key value pair for each service
password_two = {
    'acebook_password' : 'password123',
    'acebook_added' : '22/03/22',
    'makersbnb_password' : 'qwerty789',
    'makersbnb_added' : '22/03/22'
}

print(password_two['acebook_password'])




#Option 2: A nested dictionary
password_three = {
    'acebook' : {
    'password' : 'password123',
    'added_on' : '22/03/22',
    },
    'makersbnb' : {
    'password' : 'qwerty789',
    'added_on' : '22/03/22',
    }
}

print(password_three['acebook'])



#Option 3: A list of dictionaries
password_four = [
    {'service' : 'acebook', 'password' : 'password123', 'added_on' : '22/03/22'},
    {'service' : 'makersbnb', 'password' : 'qwerty789', 'added_on' : '22/03/22'}
]
def find(service):
    for pwd in password_four:
        if pwd['service'] == service:
            return pwd
print(find('acebook'))

def hello(name):
    return "hello" + name
print(hello(' afzaa'))

def add(num1, num2):
    return num1 + num2

adder = add
print(adder(1,2))

def calculate_tax_for_the_shire(grossPay):
    # The friendly Shire has a 20% tax rate
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    # Dodgy Mirkwood has a 90% tax rate
    return grossPay * 0.9


def calculate_tax_for_mordor(grossPay):
    # Terrible Mordor has a 90% tax rate plus a fixed tax of £500.
    return grossPay * 0.9 + 500


def report_pay(gross_pay, calculate_tax):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"


print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(4320.0, calculate_tax_for_mirkwood))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0


def report_weather(temp, weather_func):
    return f"The weather today is {weather_func(temp)} for {temp} celsius."

def as_sun_lover(temp):
    if temp >= 25:
        return 'great'
    else:
        return 'not great'

def as_snow_lover(temp):
    if temp <= 0:
        return 'great'
    else:
        return 'not great'
    

temp = 20
print(report_weather(temp, as_sun_lover))
print(report_weather(temp, as_snow_lover))
