count_years = int(input("Введите кол-во лет: "))
print("Вы просмотрите ", count_years*365*8*60//5 , " экспонатов")

count_exhibits = int(input("Введите кол-во экспонатов: "))
minutes = count_exhibits*5
days = (minutes // (60*8) ) + 1*(minutes%(60*8) != 0 ) * (minutes>480)
years = days//365 + 1*(days%365!=0)*(days>365)

print("Вы затратите: минут = ",minutes," дней = ",days ," лет =", years)