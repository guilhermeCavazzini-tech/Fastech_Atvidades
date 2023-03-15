print('TECNOLOGIA LTDA')
n = 'S'
while n == 'S':
    funcionario=[]
    name = str(input('NOME DO FUNCIONARIO: ')).upper()
    funcionario.append(name)
    qtdHoras = float(input('HORAS TRABALHADAS: '))
    funcionario.append(qtdHoras)

    turno = str(input('QUAL O TURNO: MATUTINO, VESPERTINO OU NOTURNO: ')).upper() #DEFINE O TURNO
    while ((turno != "MATUTINO") and (turno != "M") and (turno != "VESPERTINO") and (turno !="V") and (turno !="NOTURNO") and (turno !="N")): #CONTROLE DO TURNO
        turno = str(input('OPÇÃO INVALIDA, FAVOR INSIRA NOVAMENTE: ')).upper
    else: print('----'*6)
    funcionario.append(turno)


    categoria = str(input('CATEGORIA DO FUNCIONARIO: GERENTE OU OPERARIO: ')).upper()
    while ((categoria != "GERENTE") and (categoria != "G") and (categoria != "OPERARIO") and (categoria != 'O')):
        categoria = str(input('OPÇÃO INVALIDA, FAVOR INSIRA NOVAMENTE: ')).upper()
    else: print('----'*6)
    funcionario.append(categoria)



    gn = 0.10
    gmv = 0.15
    on = 0.09
    omv = 0.14



    if (categoria == "G") or (categoria == "GERENTE"):
        if (turno == "N") or (turno == "NOTURNO"):
            funcionario=[name,'\nTotal a receber em horas extras: ','R$',((1320*on)*qtdHoras),'\nSalario Total: R$',((1320*gn)*qtdHoras)+(1320)]
        
    if (categoria == "G") or (categoria == "GERENTE"):
        if (turno == "M") or (turno == "V") or (turno == "MATUTINO ") or (turno == "VESPERTINO"):
            funcionario=[name,'\nTotal a receber em horas extras: ','R$',((1320*on)*qtdHoras),'\nSalario Total: R$',((1320*gmv)*qtdHoras)+(1320)]

    if (categoria == "O") or (categoria == "OPERARIO"):
        if (turno == "N") or (turno == "NOTURNO"):
            funcionario=[name,'\nTotal a receber em horas extras: ','R$',((1320*on)*qtdHoras),'\nSalario Total R$',((1320*on)*qtdHoras)+(1320)]

    if (categoria == "O") or (categoria == "OPERARIO"):
        if (turno == "M") or (turno == "V") or (turno == "MATUTINO ") or (turno == "VESPERTINO"):
            funcionario=[name,'\nTotal a receber em horas extras: ','R$',((1320*on)*qtdHoras),'\nSalario Total R$',((1320*omv)*qtdHoras)+(1320)]
        
    print('Nome:',funcionario[0],funcionario[1],funcionario[2],funcionario[3],funcionario[4],funcionario[5])

    n = str(input('Deseja Calcular as Horas de Outro Funcionario? [S/N]')).upper()
    