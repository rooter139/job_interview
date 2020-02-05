rows = 5
cols = 5
arreglo = [[1,1,0,0,0],[0,0,1,0,0],[1,0,0,0,0],[1,1,0,0,1],[1,1,0,0,0]]

rows2 = 7
cols2 = 7
arreglo2 = [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]




def number_buildings(rows, cols, arreglo):
    buildings = 0
    for row in range(rows):
        cont = 0
        for col in range(cols):
            if arreglo[row][col] == 1:
                tmp_building = 0
                categoria = 0
                #print(str(row) + str(col))
                if col-1 >= 0:
                    categoria +=1
                    #print("hola col-1")
                    if arreglo[row][col-1] == 0:
                        tmp_building += 1
                        
                if col+1 < cols:
                    categoria +=1
                    #print("hola col+1")
                    if arreglo[row][col+1] == 0:
                        tmp_building += 1
                        
                if row-1 >= 0:
                    categoria +=1
                    #print("hola row-1")
                    if arreglo[row-1][col] == 0:
                        tmp_building += 1
                        
                if row+1 < rows:
                    categoria +=1
                    #print("hola row+1")
                    if arreglo[row+1][col] == 0:
                        tmp_building += 1
                        
                #print("----")
                if tmp_building == categoria:
                    buildings +=1
                else:
                    cont +=1
            elif arreglo[row][col] == 0:
                cont = 0
            if cont == 2:
                buildings +=1

    print(buildings)

number_buildings(rows, cols, arreglo)
number_buildings(rows2, cols2, arreglo2)