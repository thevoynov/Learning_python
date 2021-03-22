name = input("Введите своё имя: ")
print("Hello " + name )
age = int(input("Введите сколько вам лет: "))

if age <= 4:
    print('Вследующем году вам будет ', age + 1, ' года.')
elif age > 4:
    print('Вследующем году вам будет ', age + 1, ' лет.')
else:
    print('Вы написани не число')