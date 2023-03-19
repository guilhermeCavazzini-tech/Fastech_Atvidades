print('Torre de Pizza')

Elevador = ['A','B','C']
Periodo = ['M','MATUTINO','V','VESPERTINO','N','NOTURNO',]
registro = []
m = 0
while (True):
    VerificaoElevador = str(input('QUAL O ELEVADOR DESEJA UTILIZAR A,B ou C?')).upper()
    while not VerificaoElevador in Elevador:
        print('OPÇÃO INVALIDA ,DESEJA UTILIZAR O A,B OU C ?')
        VerificaoElevador = str(input('QUAL O ELEVADOR DESEJA UTILIZAR A,B ou C?')).upper()

    VerificaoPeriodo = str(input('QUAL O PERIODO QUE O ELEVADOR FOI USADO MATUTINO, VERSPERTINO, NOTURNO')).upper()
    while not VerificaoPeriodo in Periodo:
        print('OPÇÃO INVALIDA ,UTILIZE MATUTINO ,VESPERTINO OU NOTURNO ?')
        VerificaoPeriodo = str(input('QUAL O PERIODO QUE O ELEVADOR FOI USADO MATUTINO, VERSPERTINO, NOTURNO')).upper()
    r = str(input('DESEJA UTILIZAR O ELEVDOR [S/N]? ')).upper()



    if r == 'N':
        break

if (VerificaoPeriodo == 'M') and (VerificaoPeriodo == 'MATUTINO'):
    registro.append[0](m+1)
    print(registro)

    #print('O elevador A foi o mais utilizado : ' )
#if b>a and b>c:
    #print('O elevador A foi o mais utilizado : ')
#if c>a and c>b:
    #print('O elevador A foi o mais utilizado : ')

#if VerificaoElevador == 'M' and VerificaoElevador == 'MATUTINO':
    #registro.append('Matutino:', m+1 )

    #print('O periodo Matutino foi mais utilizado : ', )
#if v>m and v>n:
    #print('O periodo Vespertino foi mais utilizado : ' )
#if n>m and n>v:
   #print('O periodo Noturno foi mais utilizado : ' )



#while (VerificaoPeriodo != 'M') and (VerificaoPeriodo != "MATUTINO") and (VerificaoPeriodo != 'V') and (VerificaoPeriodo != "VESPERTINO") and (VerificaoPeriodo != 'N') and (VerificaoPeriodo != "NOTURNO"):
        #VerificaoPeriodo = str(input('OPÇÃO INVALIDA ,DESSEJA UTILIZAR O A,B OU C ?')).upper()
    #if (VerificaoPeriodo == 'M') and (VerificaoPeriodo == 'MATUTINO') :
        #m = m+1
    #if (VerificaoPeriodo == 'V') and (VerificaoPeriodo == 'VESPERTINO') :
        #v = v+1
    #if (VerificaoPeriodo == 'N') and (VerificaoPeriodo == 'NOTURNO') :
        #n = n+1