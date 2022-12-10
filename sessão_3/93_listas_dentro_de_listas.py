salas = [['Maria', 'Helena', ],
         ['Elaine', ],
         ['Luiz', 'João', "Eduarda", (0,10,20,30,40)], ]

# print(salas[1][0]) # Elaine
# print(salas[0][1]) # Helena
# print(salas[2][2]) # Eduarda
# print(salas[2][3][2]) # 20

for sala in salas:
    for aluno in sala:
        if type(aluno) == tuple or type(aluno) == list:
            for item in aluno:
                print(item)
        else:
            print(aluno)
