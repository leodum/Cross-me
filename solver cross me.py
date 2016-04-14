
def solver(b,c):
    #grille de taille x,y où b est la liste des indications des lignes et c des colonnes
    x=len(c)
    y=len(b)
    print("grille à",y,"lignes et",x,"colonnes")
    #on construit la grille appelée a, a[i][j] est l'élément de la i-ième colonne et j-ieme ligne
    a=[[" " for q in range(0,x)] for p in range(0,y)]


    #on remplit les cases évidentes pour les lignes
    for i in range(y):
        av=0
        ap=0
        # av est le nombre de case minimum occupé par les i-1 premieres indications
        # ap est le nombre de case minimum occupé par les indications après l'indication numero i

        #calcul de ap pour le premier index
        for k in range(1,len(b[i])):
            ap=ap+1+b[i][k]

        #si la place restante est inferieur à deux fois la taille de l'indication on peut remplir des cases par des "X"
        if x-ap-av-2*b[i][0]<0:
            for l in range(2*b[i][0]-(x-ap-av)):
                a[i][av+((x-ap-av)-b[i][0])+l]="X"
                
        # on fait la même chose en parcourant toutes les indications de la ligne        
        for j in range(1,len(b[i])):
            av = av+1+b[i][j-1]
            ap = ap-1-b[i][j]
            if x-ap-av-2*b[i][j]<0:
                for l in range(2*b[i][j]-(x-ap-av)):
                    a[i][av+((x-ap-av)-b[i][j])+l]="X"


    #on fait la meme chose mais avec les colonnes cette fois
    for i in range(len(c)):
        av=0
        ap=0
        for k in range(1,len(c[i])):
            ap=ap+1+c[i][k]
        #pour le premier élément de c[i]
        if y-ap-av-2*c[i][0]<0:
            for l in range(2*c[i][0]-(y-ap-av)):
                a[av+(y-ap-av-c[i][0])+l][i]="X"
        for j in range(1,len(c[i])):
            av = av+1+c[i][j-1]
            ap = ap-1-c[i][j]
            if y-ap-av-2*c[i][j]<0:
                for l in range(2*c[i][j]-(y-ap-av)):
                    a[av+(y-ap-av-c[i][j])+l][i]="X"

    #resultat intermediaire grille
    print()
    for i in range(y):
        print(a[i])




    modif=1
    while modif>0:
        modif=0
        #on complète les éléments obligatoires de chaque ligne du à la première indication (possible si on a une croix vers le debut). Par ex premiere indication de 4 et la deuxieme case et coché on peut alors aussi coché 3 et 4.          
        for i in range(len(b)):
            k=0
            while k<b[i][0]:
                if a[i][k] == "X":
                    for j in range(k,b[i][0]-1):
                        if a[i][j]!="X":
                            a[i][j]="X"
                            modif=modif+1
                k=k+1
            #puis les éléments obligatoires de chaque ligne du à la dernière indication (possible si on a une croix vers la fin) 
            k=x-1
            while k>x-b[i][len(b[i])-1]-1:
                if a[i][k] == "X":
                    for j in range(x-b[i][len(b[i])-1],k):
                        if a[i][j]!="X":
                            a[i][j]="X"
                            modif=modif+1
                k=k-1

        #meme chose pour les colonnes
        for i in range(len(c)):
            k=0
            while k<c[i][0]:
                if a[k][i] == "X":
                    for j in range(k,c[i][0]-1):
                        if a[j][i]!="X":
                            a[j][i]="X"
                            modif=modif+1
                k=k+1
             
            k=y-1
            while k>y-c[i][len(c[i])-1]-1:
                if a[k][i] == "X":
                    for j in range(y-c[i][len(c[i])-1],k):
                        if a[j][i]!="X":
                            a[j][i]="X"
                            modif=modif+1
                k=k-1
        #on boucle pour car des croix qui s'ajoutent peuvent en amener d'autres
        

                
    #resultat intermediaire grille
    print()
    for i in range(y):
        print(a[i])

    


    #on met des Zéros là où l'on peut lorsque on a une seule indication ou sinon (else:) un zero si la case correspondant à l'index indication+1 est cohée (par ex si la premiere indication est 4 et que la 5eme case est cochée alors necessairement la première est vide)
    for i in range(len(b)):
        if len(b[i])==1:
            k=0
            while a[i][k]!="X" and k<x-1:
                k=k+1
            if k+b[i][0]<x:
                for l in range (k+b[i][0],x):
                    a[i][l]="O" 
            k=x-1
            while a[i][k]!="X" and k>0:
                k=k-1
            if k-b[i][0]>-1:
                for l in range (0,k-b[i][0]+1):
                    a[i][l]="O"         
        else:
            if a[i][b[i][0]]=="X":
                a[i][0]="O"
            if a[i][x-1-b[i][len(b[i])-1]]=="X":
                a[i][x-1]="O"
    #meme chose avec les colonnes            
    for j in range(len(c)):
        if len(c[j])==1:
            k=0
            while a[k][j]!="X" and k<y-1:
                k=k+1
            if k+c[j][0]<y:
                for l in range (k+c[j][0],y):
                    a[l][j]="O"          
            k=y-1
            while a[k][j]!="X" and k>0:
                k=k-1
            if k-c[j][0]>-1:
                for l in range (0,k-c[j][0]+1):
                    a[l][j]="O"
        else:
            if a[c[j][0]][j]=="X":
                a[0][j]="O"
            if a[y-1-c[j][len(c[j])-1]][j]=="X":
                a[y-1][j]="O"


    #truc plus compliqué et qui ne fonctionne pas encore :p
    """for i in range(len(b)):
        k=0
        m=0
        print(i)
        while a[i][k]!=" " and k<x-1:
            print("1",k)
            if a[i][k]=="O":
                print("2",k)
                while a[i][k]=="O":
                    k=k+1
            if a[i][k]=="X":
                print("3",k)
                for l in range(b[i][m]):
                    a[i][k+l]="X"
                k=k+b[i][m]
                m=m+1
                if k<x-1:
                    a[i][k]="O"
                k=k+1
                print(k,m,len(b[i]))
                if m==len(b[i]):
                    print("act")
                    while k<x:
                        print(k)
                        a[i][k]="O"
                        k=k+1
                    k=x-2
            k=k+1
            print(k)"""
            
    print()
    for i in range(y):
        print(a[i])

#fonction construite pour checker la maniere de calculer l'espace possible (fonction non appelée dans le code)
def count(a):
    l=len(a)
    ap=0
    av=0
    for k in range(1,len(a)):
        ap=ap+1+a[k]
    print (av,ap)
    for j in range(len(a)-1):
        av=av+a[j]+1
        ap=ap-1-a[j+1]
        print(av,ap)
            

#solver([[2],[1],[1,1],[1,3],[5],[2,5],[3,4],[9],[2,5],[6]],[[4],[4],[2,2],[1],[1,1],[6],[6],[7],[1,7],[6,2]])

#solver([[2,1],[1,3],[1,3],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[2]])
#solver([[3],[3],[1,3],[1],[1,1]],[[3,1],[2],[3],[1],[3]])

#solver([[3],[4,2],[6,6],[6,2,1],[1,4,2,1],[6,3,2],[6,7],[6,8],[1,10],[1,10],[1,10],[1,1,4,4],[3,4,4],[4,4],[4,4]],[[1],[11],[3,3,1],[7,2],[7],[15],[1,5,7],[2,8],[14],[9],[1,6],[1,9],[1,9],[1,10],[12]])
