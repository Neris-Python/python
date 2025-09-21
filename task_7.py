seconds = int(input("Введите количество секунд: "))
minute = seconds // 60
ostatok = seconds % 60
if minute == 1:
    min_text = "минута"
elif minute >= 2 and minute <= 4:
    min_text = "минуты"
else:
    min_text = "минут"
if ostatok == 1:
    sek_text = "секунда"
elif ostatok >= 2 and ostatok <= 4:
    sek_text = "секунды"
else:
    sek_text = "секунд"
print(minute, min_text, ostatok, sek_text)