import datetime
ahora = datetime.date.today()
years = int(ahora.year)

bday = int(input('dime la fecha de tu nacimiento, primero el día\n'))
bmonth = int(input('dime el mes\n'))
byear = int(input('dime el año\n'))

birthdate = datetime.date(day=bday, month=bmonth, year=byear)
deadday = birthdate + datetime.timedelta(days=28105)
edad = ahora - birthdate
dias = edad.days
años = edad.days / 365

queda = 28105 - dias
quedanaños = queda / 365


print('Hasta ahora has vivido ', dias,'días, que son', años, 'años')
print('De acuerdo a la estadística los mexicanos vivimos 77 años en promedio')
print('Eso significa que te quedan un promedio de', queda, 'días de vida, esto son ',quedanaños,'años')
print('y estarías muriendo en el día',deadday)
input('Presiona enter para continuar')
print('Ahora que tienes esta información, ¿qué vas a hacer con los días que te quedan?')
