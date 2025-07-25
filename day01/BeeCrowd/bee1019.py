import datetime

n = input()
n = int(n)

hora = datetime.datetime(n)

print(hora.strftime("%X"))