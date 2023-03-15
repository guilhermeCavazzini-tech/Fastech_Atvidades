print('Torre de Pizza')

a = 0
b = 0
c = 0

m = 0
v = 0
n = 0

Elevador = [a,b,c]
Periodo = [m,v,n]


VerificaoElevador = str(input('QUAL O ELEVADOR DESSEJA UTILIZAR [A],[B] ou [C]?')).upper()
while (VerificaoElevador != 'A') and (VerificaoElevador != 'B') and (VerificaoElevador != 'C'):
    VerificaoElevador = str(input('OPÇÃO INVALIDA ,DESSEJA UTILIZAR O A,B OU C ?')).upper()
if VerificaoElevador == 'A':
    a = a+1
if VerificaoElevador == 'B':
    b = b+1
if VerificaoElevador == 'C':
    c = c+1

m = 0
v = 0
n = 0

