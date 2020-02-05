rows = 5
cols = 5
arreglo = [[1,1,0,0,0],[0,0,1,0,0],[1,0,0,0,0],[1,1,0,0,1],[1,1,0,0,0]]

rows2 = 7
cols2 = 7
arreglo2 = [[1,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]




def number_vesion(rows, cols, arreglo):
    version = 0
    dict = {}
    dict = valida_updates(rows, cols, arreglo)
    print(dict)

    if len(dict) == 0:
        print("It's all updated")
    else:
        while len(dict) > 0:
            version +=1
            for tuple in dict:
                x,y = tuple
                print(str(x) + str(y))
                arreglo[int(x)][int(y)] = 1
            dict = valida_updates(rows, cols, arreglo)
            print("----------")
            print(dict)
    print("The number of updates are:" + str(version))
    #print(buildings)



def valida_updates(rows, cols, arreglo):
    dict = {}
    for row in range(rows):
        for col in range(cols):
            if arreglo[row][col] == 1:
                categoria = 0
                #print(str(row) + str(col))
                if col-1 >= 0:
                    categoria +=1
                    #print("hola col-1")
                    if arreglo[row][col-1] == 0:
                        dict[str(row) + str(col-1)] = (row,col-1)
                        
                if col+1 < cols:
                    categoria +=1
                    #print("hola col+1")
                    if arreglo[row][col+1] == 0:
                        dict[str(row) + str(col+1)] = (row,col+1)
                        
                if row-1 >= 0:
                    categoria +=1
                    #print("hola row-1")
                    if arreglo[row-1][col] == 0:
                        dict[str(row-1) + str(col)] = (row-1,col)
                        
                if row+1 < rows:
                    categoria +=1
                    #print("hola row+1")
                    if arreglo[row+1][col] == 0:
                        dict[str(row+1) + str(col)] = (row+1,col)
                        
                #print("----")
                #if tmp_building == categoria:
                #    buildings +=1
                #else:
                #    cont +=1
    return dict
            





number_vesion(rows, cols, arreglo)
#number_vesion(rows2, cols2, arreglo2)