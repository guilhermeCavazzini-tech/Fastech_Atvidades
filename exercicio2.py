print('Torre de Pizza')

a = 0
b = 0
c = 0
r = 'S'
m = 0
v = 0
n = 0

Elevador = [a,b,c]
Periodo = [m,v,n]

while r == "S":
    VerificaoElevador = str(input('QUAL O ELEVADOR DESEJA UTILIZAR [A],[B] ou [C]?')).upper()
    while (VerificaoElevador != 'A') and (VerificaoElevador != 'B') and (VerificaoElevador != 'C'):
        VerificaoElevador = str(input('OPÇÃO INVALIDA ,DESSEJA UTILIZAR O A,B OU C ?')).upper()
    if VerificaoElevador == 'A':
        a = a+1
    if VerificaoElevador == 'B':
        b = b+1
    if VerificaoElevador == 'C':
        c = c+1

    VerificaoPeriodo = str(input('QUAL O PERIODO QUE O ELEVADOR FOI USADO MATUTINO, VERSPERTINO, NOTURNO')).upper()
    while (VerificaoPeriodo != 'M') and (VerificaoPeriodo != "MATUTINO") and (VerificaoPeriodo != 'V') and (VerificaoPeriodo != "VESPERTINO") and (VerificaoPeriodo != 'N') and (VerificaoPeriodo != "NOTURNO"):
        VerificaoPeriodo = str(input('OPÇÃO INVALIDA ,DESSEJA UTILIZAR O A,B OU C ?')).upper()
    if (VerificaoPeriodo == 'M') and (VerificaoPeriodo == 'MATUTINO') :
        m = m+1
    if (VerificaoPeriodo == 'V') and (VerificaoPeriodo == 'VESPERTINO') :
        v = v+1
    if (VerificaoPeriodo == 'N') and (VerificaoPeriodo == 'NOTURNO') :
        n = n+1
    r = str(input('DESEJA UTILIZAR O ELEVDOR [S/N]? ')).upper()

if a>b and a>c:
    print('O elevador A foi o mais utilizado : ', a)
if b>a and b>c:
    print('O elevador A foi o mais utilizado : ', b)
if c>a and c>b:
    print('O elevador A foi o mais utilizado : ', c)

if m>v and m>n:
    print('O periodo Matutino foi mais utilizado : ', m)
if v>m and v>n:
    print('O periodo Vespertino foi mais utilizado : ', v)
if n>m and n>v:
    print('O periodo Noturno foi mais utilizado : ', n)
    