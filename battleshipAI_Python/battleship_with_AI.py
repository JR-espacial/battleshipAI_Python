import turtle
from alphabet import alphabet
import random
import winsound as wav
import time



def lee_click(x,y):
    turtle.onscreenclick(None)
    turtle.clearscreen()
    despliega_instrucciones()
    time.sleep(30)
   
    # Quitar Musica
    wav.PlaySound(None, wav.SND_PURGE)
    
    turtle.clearscreen()
    
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(2)
    font_size = 30
    font = "Arial"
    font_color = "blue"
    
    #Tablero de Mis Tiros
    wav.PlaySound("bladeintro.wav", wav.SND_ASYNC)
    draw_board(posix_mis_tiros,posiy_mis_tiros,"Enemy ships")
    display_letters(font_size,font_color,150,210)
    draw_numbers(105,155,font,font_size)
    
    #Tablero de Mis Barcos
    draw_board(-440,250,"My Ships")
    display_letters(font_size,font_color,-390,210)
    draw_numbers(-435,155,font,font_size)
    
    # Musica Juego
    wav.PlaySound("videogame.wav", wav.SND_LOOP | wav.SND_ASYNC)
    
    # Evento principal Click
    turtle.onscreenclick(mouseclick)
 
 
def presentacion():
    turtle.ht()
    turtle.bgcolor("black")
    turtle.pendown
    turtle.bgpic("battleship.gif")
    turtle.penup ()
    turtle.goto(-200,170)
    turtle.pendown
    turtle.color("white")
    turtle.write("BATTLESHIP", True, align="left",font=("Arial", 50, "normal"))
    turtle.penup ()
    turtle.goto(-310,-250)
    turtle.pendown
    turtle.color("cyan")
    # Musica Presentación
    wav.PlaySound("battle_boom2.wav", wav.SND_NOSTOP)
    wav.PlaySound("music.wav", wav.SND_LOOP | wav.SND_ASYNC)
    turtle.write("Click on the screen to start", True, align="left",font=("Arial", 36, "normal"))
    turtle.onscreenclick(lee_click)
    
def despliega_instrucciones():
    turtle.ht()
    turtle.penup()
    turtle.goto(-320,-200)
    turtle.pendown()
    archivo = open("instrucciones.txt","r")
    cadena = archivo.read()
    turtle.write(cadena, move = False, align="left", font=("Arial", 11, "normal"))   
   
def draw_board(posx,posy,titulo):
    #Trazar cuadro externo
    turtle.home()
    turtle.color("black")
    turtle.penup()
    turtle.setpos(posx + 150,posy + 50)
    turtle.write(titulo, font=(font,30, "normal"))
    turtle.setpos(posx,posy)
    turtle.pendown()    
    turtle.forward(495)
    turtle.right(90)
    turtle.forward(495)
    turtle.right(90)
    turtle.forward(495)
    turtle.right(90)
    turtle.forward(495)
    cont=1
    while (cont < 11):
        if (cont % 2 == 0):
            turtle.left(90)
            turtle.forward(45)
            turtle.left(90)
            turtle.forward(495)
        else:   
            turtle.right(90)
            turtle.forward(45)
            turtle.right(90)
            turtle.forward(495)
        cont +=  1
    turtle.right(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    cont = 1
    while (cont < 11):
        if (cont % 2 == 0):
            turtle.left(90)
            turtle.forward(495)
            turtle.right(90)
            turtle.forward(45)
        else:   
            turtle.right(90)
            turtle.forward(495)
            turtle.left(90)
            turtle.forward(45)
        cont += 1
        
def display_letters(font_size,color,x,y):
    #dibuja las letras
    letters=["A","B","C","D","E","F","G","H","I","J"]
    turtle.color(color)
    characterSpacing = 20
    for character in letters:
        if character in alphabet:
            letter=alphabet[character]
            turtle.penup()
            for dot in letter:
                turtle.goto(x + dot[0] * font_size, y + dot[1] * font_size)
                turtle.pendown()
        
            x += font_size        
            if character == "C":
                characterSpacing = 15    
            x += characterSpacing

def draw_numbers(x,y,font,font_size):
    #dibuja los numeros
    numbers = ["1","2","3","4","5","6","7","8","9","10"]  
    turtle.penup()
    turtle.goto(x,y)
    for num in numbers:
        turtle.write(num, font = (font,font_size, "normal"))
        y -= 45
        if num == "9":
           turtle.goto(x-10,y)
        else:
          turtle.goto(x,y)
                   
def crea_matriz(matriz): #crea una matriz de ceros con dimenciones de 10*10 
    for  ren in range(10):
        matriz.append([0]*10)
        
def inicializa_informacion_barcos_jugador_y_compu(informacion_barcos_jugador,informacion_barcos_compu):
    #inicializa matrices en ls que se guarda ra informacion relevante sobre los barcos tanto de la computadora como de el jugador
    #se guardaran los datos en el siguiente orden: posicion inicialren,posicion inicial col,tamaño,orientacion,aciertos,posx,posy
    for ren in range (5):
        nueva_lista = []
        for col in range (7):
            nueva_lista.append(0)
        informacion_barcos_jugador.append(nueva_lista)
    for ren in range (5):
        nueva_lista = []
        for col in range (7):
            nueva_lista.append(0)
        informacion_barcos_compu.append(nueva_lista)
        
def genera_cambio(orientacion):
#esta fucion genera el cambio y el eje correspondientes de acuerdo a la orientacion
#donde 0 es a la derecha,1 es abajo, 2  es a la izquierda y 3 es arriba
#las variables eje y cambio se utilizaran varias veces durante el programa para generar calculos
    if orientacion == 0:
        cambio = 1
        eje = "horizontal"
    elif orientacion == 1:
        cambio = 1
        eje = "vertical"
    elif orientacion == 2:
        cambio = -1
        eje = "horizontal"
    elif orientacion == 3:
        cambio = -1
        eje = "vertical"
    return (eje,cambio)
   
def coloca_barco_compu(matriz,ren,col,num,tam,orientacion,informacion_barcos_compu):
#coloca los barcos de la computadora en posiciones random
    for i in range(tam):
        if orientacion == 0:
            matriz [ren][col+i] = num
        elif orientacion == 1:
            matriz [ren+i][col] = num
        elif orientacion == 2:
            matriz [ren][col-i] = num
        elif orientacion == 3:
            matriz [ren-i][col] = num  
        informacion_barcos_compu[num-1][0] = ren
        informacion_barcos_compu[num-1][1] = col
        informacion_barcos_compu[num-1][2] = tam
        informacion_barcos_compu[num-1][3] = orientacion
        posx,posy,mcol,mren =localiza_tiro(((col+1)*45+100),(250-(ren+1)*45),100)
        informacion_barcos_compu[num-1][5] = posx
        informacion_barcos_compu[num-1][6] = posy
        print("informacion_barcos_compu", informacion_barcos_compu)       
    
def valida_barco_compu(matriz,ren,col,tam,orientacion): #coloca un barco en la matriz correspondiente
#valida que un barco se puea colocar en la orietacion y posicion que se quiere
    print(" ",ren + 1,"   ",col + 1,"   ",tam ,"   ",orientacion)
    if matriz [ren][col] != 0:
        print(" Ya colocaste un barco en esta casilla por favor coloca tu nuevo barco en una casilla libre")
        return 0
    else:
        for i in range(1,tam):
            if orientacion == 0:
                if matriz [ren][col+i] !=0:
                    print(" El barco no cabe")
                    return 0
            elif orientacion == 1:
                if matriz [ren+i][col] !=0:
                    print(" El barco no cabe")
                    return 0
            elif orientacion == 2:
                if matriz [ren][col-i] !=0:
                    print(" El barco no cabe")
                    return 0
            elif orientacion == 3:
                if matriz [ren-i][col] !=0:
                    print(" El barco no cabe")
                    return 0
        return 1
    
def valida_pos_ini_barco_usario(matriz,ren,col,tam,num,espacios_disponibles,informacion_barcos_jugador):
    global pos_ini_barco_col
    global pos_ini_barco_ren
    global posicion_inicial_barco
    derecha=0
    izquierda=0
    arriba=0
    abajo=0
  
    while (col + derecha) < 10 and matriz [ren][col + derecha] == 0:
        derecha += 1
    while (col - izquierda) >= 0 and matriz [ren][col - izquierda] == 0:
        izquierda += 1
    while (ren + abajo) < 10 and matriz [ren  + abajo][col] == 0:
        abajo += 1
    while (ren - arriba) >= 0 and matriz [ren - arriba][col] == 0:
        arriba += 1
        
    espacios_disponibles[0] = derecha
    espacios_disponibles[1] = abajo
    espacios_disponibles[2] = izquierda
    espacios_disponibles[3] = arriba
    print("espacios_disponibles",espacios_disponibles)
    if derecha >= tam or izquierda >= tam or abajo >= tam or arriba >= tam:
        informacion_barcos_jugador[num-1][0] = ren
        informacion_barcos_jugador[num-1][1] = col
        informacion_barcos_jugador[num-1][2] = tam
        pos_ini_barco_col = col
        pos_ini_barco_ren = ren
        posicion_inicial_barco = True 
        return 1
    else:
        print("no se puede colocar un barco en esta casilla")
        return 0
    #codigo pendiente

def coloca_barco(matriz,posx,posy,col,ren,tam,num,espacios_disponibles,informacion_barcos_jugador):#coloca un barco en la matriz correspondiente
    print(" ",col + 1,"   ",ren + 1)
    if valida_pos_ini_barco_usario(matriz,ren,col,tam,num,espacios_disponibles,informacion_barcos_jugador)== 0:
        return 0
    else:
        matriz[ren][col]=num
        turtle.color("gray")
        informacion_barcos_jugador[num-1][5] = posx
        informacion_barcos_jugador[num-1][6] = posy
        fill_square(posx,posy)
        return 1

def coloca_el_resto_de_el_barco(x,y,mi_matriz,iniciombx,posx,posy,mcol,mren,tam,num,espacios_disponibles,informacion_barcos_jugador):
    global pos_ini_barco_col
    global pos_ini_barco_ren
    
    if (mcol - 1) == pos_ini_barco_col and mren == pos_ini_barco_ren or (mcol + 1) == pos_ini_barco_col and mren == pos_ini_barco_ren:
        if (mcol - 1) == pos_ini_barco_col and mren == pos_ini_barco_ren:
            orientacion = 0
        elif (mcol + 1) == pos_ini_barco_col and mren == pos_ini_barco_ren:
            orientacion = 2
        informacion_barcos_jugador[num-1][3] = orientacion
        eje,cambio = genera_cambio(orientacion)
        #print("****orientacion",orientacion,"****espacios_disponibles", espacios_disponibles)
        if espacios_disponibles[orientacion] >= tam:
            cont = 0
            while cont < (tam-1):
                turtle.color("gray")
                mi_matriz[mren][mcol + (cambio * cont)] = num
                fill_square(posx + (45 * (cont * cambio)),posy)
                cont = cont + 1
            return 1
        else:
            print("tu barco no cabe en esta direccion")
            return 0
    elif (mren - 1) == pos_ini_barco_ren and mcol == pos_ini_barco_col or(mren + 1) == pos_ini_barco_ren and mcol == pos_ini_barco_col:
        if (mren - 1) == pos_ini_barco_ren and mcol == pos_ini_barco_col:
            orientacion = 1
        elif (mren + 1) == pos_ini_barco_ren and mcol == pos_ini_barco_col:
            orientacion = 3
        informacion_barcos_jugador[num-1][3] = orientacion
        eje,cambio = genera_cambio(orientacion)
        #print("**ren**orientacion",orientacion,"****espacios_disponibles", espacios_disponibles)
        if espacios_disponibles[orientacion] >= tam:
            cont = 0
            while cont < (tam-1):
                turtle.color("gray")
                mi_matriz[mren + (cambio * cont)][mcol] = num
                fill_square(posx,posy - (45 * (cont * cambio)))
                cont = cont + 1
            return 1
        else:
            print("tu barco no cabe en esta direccion")
            return 0
              
    else:
        print("debe clickear en una casilla contigua a la inicial")
        return 0

def coloca_mis_barcos(x,y,mi_matriz,iniciombx,barcos_colocados,espacios_disponibles,informacion_barcos_jugador): #coloca tus barcos donde hagas click
    global posicion_inicial_barco
    
    posx,posy,mcol,mren = localiza_tiro(x,y,iniciombx)
    if barcos_colocados  == 0:
        tam = 5
        num = 1
    elif barcos_colocados  == 1:
        tam = 4
        num = 2
    elif barcos_colocados  == 2:
        tam = 3
        num = 3
    elif barcos_colocados  == 3:
        tam = 3
        num = 4
    elif barcos_colocados  == 4:
        tam = 2
        num = 5
    if posicion_inicial_barco == False:
      if coloca_barco(mi_matriz,posx,posy,mcol,mren,tam,num,espacios_disponibles,informacion_barcos_jugador) == 0:
            return 0
    else:
        if coloca_el_resto_de_el_barco(x,y,mi_matriz,iniciombx,posx,posy,mcol,mren,tam,num,espacios_disponibles,informacion_barcos_jugador) == 1:
            print("mi matriz",mi_matriz)
            posicion_inicial_barco = False
            print("informacion_barcos_jugador", informacion_barcos_jugador)
            return 1
        else:
            return 0
     #codigo return pendiente
    
def genera_coordenadas(tam,matriz):
    i = 0
    while i == 0:
        orientacion = random.randrange(0,4)  #0 es horizontal a la derecha, 1 es vertical hacia abjajo,2 es horizontal a la izquierda, 3 vertical arriba
        if orientacion == 0:
            ren = random.randrange(0,10)
            col = random.randrange(0,10-(tam-1))
        elif orientacion == 1:
            ren = random.randrange(0,10-(tam-1))
            col = random.randrange(0,10)
        elif orientacion == 2:
            ren = random.randrange(0,10)
            col = random.randrange(0+(tam-1),10)
        elif orientacion == 3:
            ren = random.randrange(0+(tam-1),10)
            col = random.randrange(0,10)
        i = i + valida_barco_compu(matriz,ren,col,tam,orientacion)
    return (ren,col,orientacion)
    
def coloca_barcos_compu(matriz,informacion_barcos_compu):
    #coloca los 5 barcos de la computadora en posiciones random dentro del tablero Mis Tiros
    print("Los barcos estan en")
    print(" ren   col   tam   orientacion")
    ren,col,orientacion = genera_coordenadas(5,matriz)
    coloca_barco_compu(matriz,ren,col,1,5,orientacion,informacion_barcos_compu)
    ren,col,orientacion = genera_coordenadas(4,matriz)
    coloca_barco_compu(matriz,ren,col,2,4,orientacion,informacion_barcos_compu)
    ren,col,orientacion = genera_coordenadas(3,matriz)
    coloca_barco_compu(matriz,ren,col,3,3,orientacion,informacion_barcos_compu)
    ren,col,orientacion = genera_coordenadas(3,matriz)
    coloca_barco_compu(matriz,ren,col,4,3,orientacion,informacion_barcos_compu)
    ren,col,orientacion = genera_coordenadas(2,matriz)
    coloca_barco_compu(matriz,ren,col,5,2,orientacion,informacion_barcos_compu)
    
def coloca_y_colorea_barco_hundido(matriz,informacion_barcos,eje,cambio,num):
    turtle.color("red")
    if eje == "vertical":
        matriz[informacion_barcos[num-1][0]+(1*cambio)][informacion_barcos[num-1][1]] = "H"
        print("posx",informacion_barcos[num-1][5],"posy",informacion_barcos[num-1][6] -(45*cambio))
        fill_square(informacion_barcos[num-1][5],informacion_barcos[num-1][6] -(45*cambio))       
    elif eje == "horizontal":
        matriz[informacion_barcos[num-1][0]][informacion_barcos[num-1][1] +(1*cambio)] = "H"
        fill_square(informacion_barcos[num-1][5] +(45*cambio),informacion_barcos[num-1][6])
        print("posx",informacion_barcos[num-1][5] +(45*cambio),"posy",informacion_barcos[num-1][6])
    
def actualiza_informacion(matriz,informacion_barcos,num):
    global aciertos_compu
    informacion_barcos[num-1][4]+=1
    #print ("ACIERTOS AL ACTUALIZAR INFORMACION",aciertos_compu)
    orientacion = informacion_barcos[num-1][3]
    print("aciertos",informacion_barcos[num-1][4],"tamaño", informacion_barcos[num-1][2])
    if informacion_barcos[num-1][4] == informacion_barcos[num-1][2]:
        for i in range (informacion_barcos[num-1][2]):
            eje,cambio = genera_cambio(orientacion)
            coloca_y_colorea_barco_hundido(matriz,informacion_barcos,eje,(cambio*i),num)
            
        print("matriz barco hundido",matriz)
        return 1
    else:
        return 0
            
def checa_aciertos_compu(informacion_barcos_jugador, aciertos,aciertos_esperados):
    global aciertos_compu
    print("informacion_barcos_jugador",informacion_barcos_jugador)
    for i in range (5):
        if informacion_barcos_jugador[i][4] == aciertos_esperados:
            aciertos += 1
            aciertos_compu[0] = i
            aciertos_compu[1] = aciertos
    return aciertos

def checa_acierto_actual(acierto_actual):
    for lista in acierto_actual:
         if lista != [0,0,0,0,0,0]:
             return 1
    return 0
               
def checa_otros_aciertos_y_cambia(otros_aciertos):
    print("E N T R O a checa_otros_aciertos")
    global acierto_actual
    global aciertos_compu
    global casillas_aciertos
    aciertos_compu[1] = 0
    if otros_aciertos[0] != [0,0,0,0,0,0]:
        print("ECONTRO OTROS ACIERTOS")
        acierto_actual[0] = otros_aciertos[0]
        casillas_aciertos[0][0]= otros_aciertos[0][0]
        casillas_aciertos[0][1]= otros_aciertos[0][1]
        aciertos_compu[1] = 1
        cont=0
        for lista in otros_aciertos:
            if cont > 0:
                otros_aciertos[cont-1] = lista
            cont+=1
        otros_aciertos[4] = [0,0,0,0,0,0]
    
def inicializa_matrices_tiros_compu(matrices_tiros_compu):
    for elemento in range (3):
        for ren in range (10):
            new_list=[]
            for col in range (6):
                new_list.append(matrices_tiros_compu[elemento][1])
            matrices_tiros_compu[elemento][0].append(new_list)

def casilla_disponible(ren,col):
    global mi_matriz
    global valores_aceptables
    if (ren > 9 or ren < 0) or (col > 9 or col < 0):
        return False
    disponibilidad = False
    for i in valores_aceptables:#[0,1,2,3,4,5]
        if mi_matriz[ren][col] == i:
            disponibilidad = True
    return disponibilidad

def genera_tiro_acierto1(aciertos):
    global acierto_actual
    ren = 0
    col = 0
    disponibilidad = False
    while (ren > 9 or ren < 0) or (col > 9 or col < 0) or  (disponibilidad == False):
        #if acierto_actual[aciertos-1][4] == 0:
        orientacion = random.randrange(0,4)
        eje,cambio= genera_cambio(orientacion)
        if eje == "horizontal":
            ren = acierto_actual[0][0]
            col = acierto_actual[0][1] + cambio
            posx =acierto_actual[0][2] +(45*cambio)
            posy = acierto_actual[0][3] 
        elif eje == "vertical":
            ren = acierto_actual[0][0] + cambio
            col = acierto_actual[0][1]
            posx = acierto_actual[0][2] 
            posy = acierto_actual[0][3] -(45*cambio)
        disponibilidad = casilla_disponible(ren,col)
        print("1ER ACIERTO ren,col,posx,posy",ren,col,posx,posy)
    return (ren,col,posx,posy,eje,cambio)

def genera_primer_tiro_acierto2_o_mas(aciertos):
    global acierto_actual
    eje = acierto_actual[aciertos-1][4] 
    cambio = acierto_actual[aciertos-1][5]
    ren=0
    col=0
    posx=0
    posy=0
    bandera = True
    if eje == "horizontal":
            ren = acierto_actual[aciertos-1][0]
            col = acierto_actual[aciertos-1][1] + cambio
            posx = acierto_actual[aciertos-1][2] +(45*cambio)
            posy = acierto_actual[aciertos-1][3] 
    elif eje == "vertical":
            ren = acierto_actual[aciertos-1][0] + cambio
            col = acierto_actual[aciertos-1][1]
            posx = acierto_actual[aciertos-1][2] 
            posy = acierto_actual[aciertos-1][3] -(45*cambio)
    if (ren > 9 or ren < 0) or (col > 9 or col < 0):
        bandera = False
    elif  False == casilla_disponible(ren,col):
        bandera = False
    print("ACIERTO",aciertos,"ren,col,posx,posy,eje,cambio",ren,col,posx,posy,eje,cambio)
    return (ren,col,posx,posy,eje,cambio,bandera)

def genera_cambio_de_direcion(aciertos):
    global acierto_actual
    global temp
    temp[1] = 1
    eje = acierto_actual[aciertos-1][4]
    print("CAMBIO DE DIRECCION EJE =",eje)
    cambio = acierto_actual[aciertos-1][5]
    print("CAMBIO DE DIRECCION CAMBI0 ANTERIOR =",cambio)
    cambio = (cambio * -1)
    print (" NUEVO CAMBI0  =",cambio)    
    bandera = True
    ren=0
    col=0
    posx=0
    posy=0
    if eje == "horizontal":
            ren = acierto_actual[0][0]
            col = acierto_actual[0][1] + cambio
            posx =acierto_actual[0][2] +(45*cambio)
            posy = acierto_actual[0][3] 
    elif eje == "vertical":
            ren = acierto_actual[0][0] + cambio
            col = acierto_actual[0][1]
            posx = acierto_actual[0][2] 
            posy = acierto_actual[0][3] -(45*cambio)
    if (ren > 9 or ren < 0) or (col > 9 or col < 0):
        bandera = False
    elif  False == casilla_disponible(ren,col):
        bandera = False
    print("ACIERTO",aciertos,"ren,col,posx,posy,eje,cambio,bandera",ren,col,posx,posy,eje,cambio,bandera)
    return (ren,col,posx,posy,eje,cambio,bandera)

def reinicia_casillas_aciertos(casillas_aciertos):
    cont=0
    for lista in casillas_aciertos:
        if cont > 0:
            casillas_aciertos[cont] = ["V","V","V","V","V","V"]
        cont+=1

def genera_cambio_de_eje(aciertos):
    global acierto_actual
    global temp
    global aciertos_compu
    global  casillas_aciertos
    print("CAMBIO DE EEE JJJ EEE")
    temp[1] = 0
    temp[0] = 0
    aciertos_compu[1] = 1
    #aciertos =1
    reinicia_casillas_aciertos(casillas_aciertos)
    eje = acierto_actual[aciertos-1][4]
    for i in range (aciertos-1,0,-1):
        otros_aciertos [i-1] = acierto_actual[i]
        acierto_actual[i] =[0,0,0,0,0,0]
    ren = 0
    col = 0
    cambio=0
    posx=0
    posy=0
    disponibilidad = False
    while (ren > 9 or ren < 0) or (col > 9 or col < 0) or  (disponibilidad == False):
        cambio = random.choice([-1,1])
        if eje == "vertical":
            eje ="horizontal"
            ren = acierto_actual[0][0]
            col = acierto_actual[0][1] + cambio
            posx =acierto_actual[0][2] +(45*cambio)
            posy = acierto_actual[0][3] 
        elif eje == "horizontal":
            eje = "vertical"
            ren = acierto_actual[0][0] + cambio
            col = acierto_actual[0][1]
            posx = acierto_actual[0][2] 
            posy = acierto_actual[0][3] -(45*cambio)
        disponibilidad = casilla_disponible(ren,col)
        print( "ren,col,posx,posy,eje,cambio, disponibilidad",ren,col,posx,posy,eje,cambio, disponibilidad)
    return (ren,col,posx,posy,eje,cambio)

def valida_Hs(aciertos):
    global aciertos_compu
    global casillas_aciertos
    global mi_matriz
    global temp
    print("VALIDA HS",casillas_aciertos)
    bandera = False
    reiniciar = False
    for i in range( len(casillas_aciertos)):
        if casillas_aciertos[i][0]== "V":
            pass
        elif mi_matriz [casillas_aciertos[i][0]][casillas_aciertos[i][1]]== "H":
            #print("LA CASILLA",i+1,"CONTIENE UNA H")
            reiniciar = True
            bandera = True
    if bandera == True:
        cont = 0
        for i in range( len(casillas_aciertos)):
            print("TODOS LOS VALORES SON H")
            if casillas_aciertos[i][0]== "V":
                pass
            elif mi_matriz [casillas_aciertos[i][0]][casillas_aciertos[i][1]]!= "H":
                cont+=1
                acierto_actual[0][4]=acierto_actual[len(casillas_aciertos)-1][4]
                acierto_actual[0][5]=acierto_actual[len(casillas_aciertos)-1][5]
                acierto_actual[cont-1]= acierto_actual[i]
                
                print("DETECTO QUE UN VALOR NO ES H")
                reiniciar = False
                temp[1] = 0
                temp[0] = 0
            elif mi_matriz [casillas_aciertos[i][0]][casillas_aciertos[i][1]]== "H":
                acierto_actual[i]= [0,0,0,0,0,0]
                casillas_aciertos[i][0] = "V"
                casillas_aciertos[i][1] = "V"
        aciertos_compu[1] = cont
    print("REINICIAR",reiniciar)            
    if reiniciar == True:
        aciertos_compu[1] = 0
        temp[1] = 0
        temp[0] = 0
        for i in range (len(casillas_aciertos)):
              casillas_aciertos[i]=["V","V","V","V","V","V"]
    return aciertos_compu[1]
    
def arbol_de_deciciones(aciertos,mi_matriz):
    global temp
    global aciertos_compu
    global casillas_aciertos
    bandera = True
    if aciertos == 1:
        print("A C I E R T O S  C O M P U  == 1")
        ren,col,posx,posy,eje,cambio = genera_tiro_acierto1(aciertos)
        temp[1] = 0#fallos
        temp[0] = 0
        return(ren,col,posx,posy,eje,cambio)
    elif aciertos > 1:
        print("A C I E R T O S  C O M P U  == ",aciertos)
        #if valida_Hs(aciertos) in [0,1]:
            #return(0,0,0,0,0,0)
        if temp[0] == aciertos:
            cambio = 0
            eje = 0
            print( " ACIERTOS TIRO ANTERIOR, FALLOS PREVIOS", temp[0], temp[1])
            if temp[1]==0:
                ren,col,posx,posy,eje,cambio,bandera = genera_cambio_de_direcion(aciertos)
                if bandera == False:
                    ren,col,posx,posy,eje,cambio = genera_cambio_de_eje(aciertos) 
                
            else:
                ren,col,posx,posy,eje,cambio = genera_cambio_de_eje(aciertos)
            return (ren,col,posx,posy,eje,cambio)
        else:
            ren,col,posx,posy,eje,cambio,bandera = genera_primer_tiro_acierto2_o_mas(aciertos)
            if bandera == False:
                 ren,col,posx,posy,eje,cambio,bandera = genera_cambio_de_direcion(aciertos)
                 if bandera == False:
                      ren,col,posx,posy,eje,cambio = genera_cambio_de_eje(aciertos)        
            temp[0] = aciertos
            temp[1] = 0
            return (ren,col,posx,posy,eje,cambio)
          
def tiro_compu(mi_matriz,iniciombx,informacion_barcos_jugador):# genera un tiro random de la compu y lo dibuja
    global aciertos_compu
    global otros_aciertos
    global acierto_actual
    i = 0
    print (" ENTRO A TIRO COMPU ACIERTOS COMPU=",aciertos_compu)
    aciertos = aciertos_compu[1]
    if checa_acierto_actual(acierto_actual) ==0:
        checa_otros_aciertos_y_cambia(otros_aciertos)
        aciertos = aciertos_compu[1]
            # checa_aciertos_compu(informacion_barcos_jugador,aciertos, (aciertos+1)) != 0:               
    if aciertos == 0:
        print("A C I E R T O S  C O M P U  == 0")
        while i == 0:
            x = random.randrange(-395.0,55.0)
            y = random.randrange(-245.0,205.0)
            posx,posy,mcol,mren = localiza_tiro(x,y,iniciombx)
            i = coloca_tiro(mi_matriz,mren,mcol,posx,posy,informacion_barcos_jugador)
        temp_aciertos = aciertos
        aciertos = aciertos_compu[1]
        if aciertos == (temp_aciertos + 1):
            acierto_actual[0][0] = mren
            acierto_actual[0][1] = mcol
            acierto_actual[0][2] = posx
            acierto_actual[0][3] = posy
            casillas_aciertos[0][0] = mren
            casillas_aciertos[0][1] = mcol       
        return i
    if aciertos > 0:
        while i == 0:
            ren,col,posx,posy,eje,cambio = arbol_de_deciciones(aciertos,mi_matriz)
            temp_aciertos = aciertos_compu[1]
            if  [ren,col,posx,posy,eje,cambio] == [0,0,0,0,0,0]:
                return 9
            i = coloca_tiro(mi_matriz,ren,col,posx,posy,informacion_barcos_jugador)
        aciertos = aciertos_compu[1]
        #aciertos = checa_aciertos_compu(informacion_barcos_jugador, aciertos_compu,aciertos,(aciertos+1))
        print("ACIERTOS =",aciertos,"TEMP ACIERTOS=",temp_aciertos)
        if aciertos == (temp_aciertos + 1):
            print("EL PROGRAMA ESTA COLOCANDO EL ACIERTO EN EL ESPACIO", temp_aciertos)
            acierto_actual[temp_aciertos][0] = ren
            acierto_actual[temp_aciertos][1] = col
            acierto_actual[temp_aciertos][2] = posx
            acierto_actual[temp_aciertos][3] = posy
            acierto_actual[temp_aciertos][4] = eje
            acierto_actual[temp_aciertos][5] = cambio
            casillas_aciertos[temp_aciertos][0] = ren
            casillas_aciertos[temp_aciertos][1] = col
            valida_Hs(aciertos)
            
        return i
    
def coloca_tiro(matriz,ren,col,posx,posy,informacion_barcos):# coloca el tiro en la matriz correspondiente y lo dibuja en el tablero correspondiente 
    global aciertos_compu
    global otros_aciertos
    global informacion_barcos_jugador
    if  matriz [ren][col] == 1 or matriz [ren][col] == 2 or matriz [ren][col] == 3 or matriz [ren][col] == 4 or matriz [ren][col] == 5:
       if matriz [ren][col] == 1:
            num = 1
       elif matriz [ren][col] == 2:
           num = 2
       elif matriz [ren][col] == 3:
           num = 3
       elif matriz [ren][col] == 4:
           num = 4
       elif matriz [ren][col] == 5:
           num = 5
       if informacion_barcos == informacion_barcos_jugador :
           aciertos_compu[1]= aciertos_compu[1]+1
  
       tempi = actualiza_informacion(matriz,informacion_barcos,num)
       print("**aciertos",informacion_barcos[num-1][4],"**tamaño", informacion_barcos[num-1][2])
       if tempi == 0:
           matriz [ren][col] = "A"
           turtle.color("green")
           fill_square(posx,posy)
           return 9
       else:
           return 10 
    elif matriz [ren][col] == "T" or matriz [ren][col] == "H" or matriz [ren][col] == "A":
        print("ya tiraste ateriormente en esta casilla porfavor haz click en otra")
        return 0
    else:
        matriz [ren][col] = "T"
        turtle.color("blue")
        fill_square(posx,posy)
        return 9
               
def localiza_tiro(x,y,iniciox):
    #regresa la posicion en el tablero Mis Tiros del vertice superio izquierdo donde se dio clik y el indice correspondiente en la matriz
    difx = x - (iniciox+45)
    dify =  (inicioy-45) - y
    if y < 0:
        if y < -244:
            y = y * -1
            dify = (inicioy-90)+y
        else:
            y = y * -1
            dify = (inicioy-45)+y
    mx = difx // 45
    my = (dify // 45)
    posx = iniciox + 45 * (mx+1)
    if y < 0:
        posy=inicioy + 45 * (my+1)
    else:
        posy = inicioy - 45*(my+1)
    return(posx,posy,int(mx),int(my))       
        
def fill_square(posx,posy):
    #colorea una casilla
    turtle.penup
    turtle.home()
    turtle.setpos(posx,posy)
    turtle.pendown
    turtle.begin_fill()
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.end_fill()
    
def gana_pierde(aciertos_m,aciertos_e):
    if aciertos_e == 5 and aciertos_m == 5 or aciertos_e == 5 or aciertos_m == 5:
        turtle.penup()
        turtle.goto(-400,0)
        turtle.color("yellow")
        if aciertos_e == 5 and aciertos_m == 5:
            turtle.bgcolor("black")
            turtle.write("EMPATE!", font = (font,90, "normal"))
            wav.PlaySound(None, wav.SND_PURGE)
        elif aciertos_m == 5:
            turtle.bgcolor("black")
            wav.PlaySound(None, wav.SND_PURGE)
            turtle.write("GANASTE!!!!", font = (font,90, "normal"))
            wav.PlaySound("win.wav", wav.SND_ASYNC)
        elif aciertos_e == 5:
            turtle.bgcolor("black")
            wav.PlaySound(None, wav.SND_PURGE)
            turtle.write("PERDISTE!!!!", font = (font,90, "normal"))
            wav.PlaySound("you lost.wav", wav.SND_ASYNC)
            time.sleep(4)
            wav.PlaySound("Game Over.wav", wav.SND_ASYNC)
        turtle.onscreenclick(None)
        
        return True
    else:
        return False  
    
def mouseclick(x,y):
    #dentro de esta fucion se realizan varios procedimientos los explicare mas a detalle en cada fucion
    #en terminos generales cololoca tus barcos,colorea tus tiros y genera tiros de la compu
    global matriz_enemigo
    global barcos_colocados
    global mi_matriz
    global aciertos_m
    global aciertos_e
    global espacios_disponibles
    global informacion_barcos_jugador
    turtle.onscreenclick(None)
    salir = False
    if barcos_colocados<5: # con este if se colocan tus 5 barcos
        if x > -395.0 and x < 55.0 and y < 205.0 and y > -245.0 :#aqui se checa que esten tus barcos sean colocados en tu tablero
            if coloca_mis_barcos(x,y,mi_matriz,iniciombx,barcos_colocados,espacios_disponibles,informacion_barcos_jugador) == 1:#se considera que se ha colocado un barco solo si das click en un espacio libre
                barcos_colocados=barcos_colocados+1
                print("barcos colocados",barcos_colocados)
        else:
            print("El valor no es valido porfavor haga click en la casilla donde quiere tirar")            
    else:
        if(x > 145.0 and x < 595.0 and y < 205.0 and y > -245.0):#una vez colocados tus barcos el prorama epera a que tires en el tablero enemigo y dibuja tu tiro
            posx,posy,mcol,mren = localiza_tiro(x,y,iniciomtx)# se sacan los datos para poder colocar tu tiro en la matriz y dibujarlo
            res_ct = coloca_tiro(matriz_enemigo,mren,mcol,posx,posy,informacion_barcos_compu)
            if res_ct == 0:#se coloca tu tiro y se dibuja solo si clickeaste en una casilla donde no hayas tirado anteriormente
                pass
            elif res_ct == 10:
                aciertos_m += 1
                if tiro_compu(mi_matriz,iniciombx,informacion_barcos_jugador) == 10:#si tu tiraste en una casilla donde no hayas tirado anteriormente se genera y dibuja un tiro respuest de la computadora
                    aciertos_e += 1
                    salir=gana_pierde(aciertos_m,aciertos_e)
                else:
                    salir=gana_pierde(aciertos_m,aciertos_e)
            else:
                if tiro_compu(mi_matriz,iniciombx,informacion_barcos_jugador) == 10:#si tu tiraste en una casilla donde no hayas tirado anteriormente se genera y dibuja un tiro respuest de la computadora
                    aciertos_e += 1
                    salir=gana_pierde(aciertos_m,aciertos_e)                  
        else:
            print("El valor no es valido porfavor haga click en la casilla donde quiere tirar")
    if salir == False:
        turtle.onscreenclick(mouseclick)    


#main       
presentacion()

turtle.speed(0)
turtle.hideturtle()
turtle.pensize(2)
font_size = 30
font = "Arial"
font_color = "blue"
posix_mis_tiros = 100
posiy_mis_tiros = 250
matriz_enemigo=[]
mi_matriz=[]
iniciomtx = 100
inicioy = 250
iniciombx = -440
barcos_colocados=0
aciertos_m = 0
aciertos_e = 0
pos_ini_barco_col = 0
pos_ini_barco_ren = 0
posicion_inicial_barco = False
informacion_barcos_jugador = []
#matriz de 5 barcos
#posicion inicialren,posicion inicial col,tamaño,orientacion,aciertos,posx,posy
informacion_barcos_compu = []
#matriz de 5 barcos
#posicion inicialren,posicion inicial col,tamaño,orientacion,aciertos,posx,poy
espacios_disponibles = [0,0,0,0]#0derecha,1abajo,2izquierda,3derecha

#Matriz Mis Tiros
crea_matriz(matriz_enemigo)
crea_matriz(mi_matriz)
#inicializa una matriz con informacion relevante sobre los barcos de el jugador y la computadora
inicializa_informacion_barcos_jugador_y_compu(informacion_barcos_jugador,informacion_barcos_compu)
coloca_barcos_compu(matriz_enemigo,informacion_barcos_compu)
#arbol de deciciones
primer_tiro = True
temp = [0,0]
aciertos_compu = [0,0]#lista
acierto_actual = [ ]#matriz
# ren,col,posx,posy,eje,cambio
otros_aciertos = []# matriz
casillas_aciertos = []#matriz inicializada con V
matrices_tiros_compu =[[acierto_actual,0],[otros_aciertos,0], [casillas_aciertos,"V"]]
valores_aceptables = [0,1,2,3,4,5]
inicializa_matrices_tiros_compu(matrices_tiros_compu)

# Musica
# wav.PlaySound("music.wav", wav.SND_LOOP | wav.SND_ASYNC)

# Evento principal Click
# turtle.onscreenclick(mouseclick)



