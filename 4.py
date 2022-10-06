count_minutes = int(input("Введите кол-во минут: "))
print("Вы просмотрите ", count_minutes//5)

count_exhibits = int(input("Введите кол-во экспонатов: "))
minutes = count_exhibits*5
days = (minutes // (60*24) ) + 1*(minutes%(60*24) != 0 ) * (minutes>1440)
years = days//365 + 1*(days%365!=0)*(days>365)

print("Вы затратите: минут = ",minutes," дней = ",days ," лет =", years)