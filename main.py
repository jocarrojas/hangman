# Hangman game

import random, sys
from getpass import getpass
# Color change subroutine
def c(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color=="green":
    return ("\033[32m")
  elif color=="purple":
    return ("\033[35m")
  elif color=="pink":
    return ("\033[38;5;206m")

listOfWordsEng = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

listOfWordsSpaE = ('De La Que El En Y A Los Se Del Las Un Por Con No Una Su Para Es Al Lo Como Más O Pero Sus Le Ha Me Si Sin Sobre Este Ya Entre Cuando Todo Esta Ser Son Dos También Fue Había Era Muy Años Hasta Desde Está Mi Porque Qué Sólo Han Yo Hay Vez Puede Todos Así Nos Ni Parte Tiene Él Uno Donde Bien Tiempo Mismo Ese Ahora Cada E Vida Otro Después Te Otros Aunque Esa Eso Hace Otra Gobierno Tan Durante Siempre Día Tanto Ella Tres Sí Dijo Sido Gran País Según Menos Año Antes Estado Contra Sino Forma Caso Nada Hacer General Estaba Poco Estos Presidente Mayor Ante Unos Les Algo Hacia Casa Ellos Ayer Hecho Primera Mucho Mientras Además Quien Momento Millones Esto España Hombre Están Pues Hoy Lugar Madrid Nacional Trabajo Otras Mejor Nuevo Decir Algunos Entonces Todas Días Debe Política Cómo Casi Toda Tal Luego Pasado Primer Medio Va Estas Sea Tenía Nunca Poder Aquí Ver Veces Embargo Partido Personas Grupo Cuenta Pueden Tienen Misma Nueva Cual Fueron Mujer Frente José Tras Cosas Fin Ciudad He Social Manera Tener Sistema Será Historia Muchos Juan Tipo Cuatro Dentro Nuestro Punto Dice Ello Cualquier Noche Aún Agua Parece Haber Situación Fuera Bajo Grandes Nuestra Ejemplo Acuerdo Habían Usted Estados Hizo Nadie Países Horas Posible Tarde Ley Importante Guerra Desarrollo Proceso Realidad Sentido Lado Mí Tu Cambio Allí Mano Eran Estar San Número Sociedad Unas Centro Padre Gente Final Relación Cuerpo Obra Incluso Través Último Madre Mis Modo Problema Cinco Carlos Hombres Información Ojos Muerte Nombre Algunas Público Mujeres Siglo Todavía Meses Mañana Esos Nosotros Hora Muchas Pueblo Alguna Dar Problema Don Da Tú Derecho Verdad María Unidos Podría Sería Junto Cabeza Aquel Luis Cuanto Tierra Equipo Segundo Director Dicho Cierto Casos Manos Nivel Podía Familia Largo Partir Falta Llegar Propio Ministro Cosa Primero Seguridad Hemos Mal Trata Algún Tuvo Respecto Semana Varios Real Sé Voz Paso Señor Mil Quienes Proyecto Mercado Mayoría Luz Claro Iba Éste Pesetas Orden Español Buena Quiere Aquella Programa Palabras Internacional Van Esas Segunda Empresa Puesto Ahí Propia M Libro Igual Político Persona Últimos Ellas Total Creo Tengo Dios C Española Condiciones México Fuerza Solo Único Acción Amor Policía Puerta Pesar Zona Sabe Calle Interior Tampoco Música Ningún Vista Campo Buen Hubiera Saber Obras Razón Ex Niños Presencia Tema Dinero Comisión Antonio Servicio Hijo Última Ciento Estoy Hablar Dio Minutos Producción Camino Seis Quién Fondo Dirección Papel Demás Barcelona Idea Especial Diferentes Dado Base Capital Ambos Europa Libertad Relaciones Espacio Medios Ir Actual Población Empresas Estudio Salud Servicios Haya Principio Siendo Cultura Anterior Alto Media Mediante Primeros Arte Paz Sector Imagen Medida Deben Datos Consejo Personal Interés Julio Grupos Miembros Ninguna Existe Cara Edad Etc. Movimiento Visto Llegó Puntos Actividad Bueno Uso Niño Difícil Joven Futuro Aquellos Mes Pronto Soy Hacía Nuevos Nuestros Estaban Posibilidad Sigue Cerca Resultados Educación Atención González Capacidad Efecto Necesario Valor Aire Investigación Siguiente Figura Central Comunidad Necesidad Serie Organización Nuevas Calidad')

listOfWordsSpaM = ('ablandar aborigen abreviar acarrear acogedor adjetivo adjuntar afrontar agrícola alcayata almohada aminorar aparecer apreciar arbitrar atenazar atrevido aventura avestruz bailarín baluarte baratija barbacoa bebedizo bendecir blancura bofetada bombilla bordillo braguero cabestro cafetera calcular califato callejón calzador camarero capturar carruaje carrusel cartilla cartucho castillo catarata celebrar cellisca cerilla chistera circuito circular codorniz cofradía colgante colonial comparar comparsa concebir conceder concepto consulta contrato converso convicto convulso correcto corredor creación creativo creencia culminar cultural dactilar decisión degradar degustar delgadez deprimir desacato desatino descoser descuido desguace deshacer destacar destapar destello devuelto dictamen diminuto diputado disolver dolorido dualidad duradero efectuar elevador embeleso empalmar emplazar encantar encestar endémico enfático ensalada entender envuelto erupción escalope escombro espinoso espumoso esquimal estatura estofado estudiar eventual evocador exaltado explorar expulsar extracto fabricar fabuloso fanático fandango favorito fechoría fecundar femenino festejar flaqueza florista folletín fonética forajido frondoso gabinete galápago garbanzo generoso genética grabador graduado guisante guitarra habanero hechizar herético holgazán homónimo hospital humildad ilustrar imaginar imprenta impulsar incienso incierto inculpar indultar inocente insignia insuflar insumiso intentar invasión isotermo jabalina jacobino jilguero justicia juventud labranza ladrillo langosta lanzador lastimar licencia liquidez luchador magnolia maletero mamífero maniobra medieval mercader merendar misterio molestar molinero moraleja nebulosa nervioso obelisco octaedro olfatear ondulado opositor original orquídea pabellón palomita paraguas pasajero pastoril percutor perdurar perezoso perfecto pergeñar pistacho pleitear poltrona populoso portería precepto préstamo probable probador producto profesor provocar puñetazo purgante raspador reactivo reavivar recortar reiterar renegado reproche repuesto reservar revolcar rupestre sacudida seductor segmento sencillo sensible servicio simetría sobornar sorpresa subsuelo suciedad sufragio sustento taburete tangente terminar tornillo torrente traducir travesía vainilla variedad ventisca vocativo vorágine')

listOfWordsSpaH = ('Otorrinolaringólogo Idiosincrasia Desoxirribonucleico Paralelepípedo Ovovivíparo Caleidoscopio Electroencefalografista Hipopotomonstrosesquipedaliofobia Supercalifragilísticoespialidoso Pneumonoultramicroscopicsilicovolcanoconiosis parangaricutirimicuaro')

listofWords=()
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

littleTitle={"es":"""

█████████████████████████████████████████████
██▀▄─██─█─█─▄▄─█▄─▄▄▀█─▄▄▄─██▀▄─██▄─▄▄▀█─▄▄─█
██─▀─██─▄─█─██─██─▄─▄█─███▀██─▀─███─██─█─██─█
▀▄▄▀▄▄▀▄▀▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀
""", "en":"""

███████████████████████▀███████████████████████
█─█─██▀▄─██▄─▀█▄─▄█─▄▄▄▄█▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█
█─▄─██─▀─███─█▄▀─██─██▄─██─█▄█─███─▀─███─█▄▀─██
▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀
"""}

lostMessage={"es":"""

██████╗░███████╗██████╗░██████╗░██╗░██████╗████████╗███████╗██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝██║
██████╔╝█████╗░░██████╔╝██║░░██║██║╚█████╗░░░░██║░░░█████╗░░██║
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝
██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝░░░██║░░░███████╗██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝
""", "en":"""

██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝██║
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝
"""}

lang=int(input("""Choose language / Elige lenguaje:

1. English / Inglés
2. Spanish / Español

Write the number/Escribe el número... 
"""))

if lang==1:
  print("You have choosen english...") 
  print(f"""{c("pink")}
   _                                             
  | |                                            
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/     
  """)

  listOfWords=listOfWordsEng
  def wordSelection():
    wordChosen=random.choice(listOfWords)

  wordSelection()
  wordChosenList=[]
  guessed=[]
  wordChosenLen=len(wordChosen)
  errorCounter=0
  remaining=7
  underscoreCount=0
  counter=0
  guessedCount=0
  
  for letter in range(wordChosenLen):
    guessed.append("_")
  
  for letter in wordChosen:
    wordChosenList.append(letter)
  
  def check():
    global counter
    global guessedCount
    global errorCounter
    print()
    for i in range(len(guessed)):
      print(f"{c('pink')}{guessed[i]}", sep="", end="")
    print()
    userLetter=input(f"{c('white')}\nType in a letter...\n\n")
    print()
    if userLetter not in wordChosenList:
      print(f"{c('red')}{hangmanpics[errorCounter]}")
      errorCounter+=1
      if errorCounter==7:
        print("Hangman died!")
        sys.exit("Game finished!")
    else:
      for letter in wordChosenList:
        indexLetter=wordChosenList.index(letter)
        if userLetter==wordChosenList[counter]:
          guessed[counter]=userLetter
          counter+=1
          guessedCount+=1
          if guessedCount==wordChosenLen:
            print("You won!")
            print(f"The word is: {wordChosen}")
            sys.exit("Game finished!")
        else:
          counter+=1
      counter=0
  
  while remaining>0:
    remaining-=1
    check()
elif lang==2:
  print("Has elegido español...")
  titleSpa="""
             _                             _       
     /\   | |                           | |      
    /  \  | |__   ___  _ __ ___ __ _  __| | ___  
   / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
  / ____ \| | | | (_) | | | (_| (_| | (_| | (_) |
 /_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ 
                                          
  """
  print(f"""{c("pink")}{titleSpa}""")  
  difficulty=int(input("Elige la dificultad:\n\n1. Fácil\n2.Medio\n3.Difícil\n4.Elegir palabra manualmente\n\n)")
  if difficulty==1:
    listOfWords=listOfWordsSpaE
  elif difficulty==2:
    listofWords=listOfWordsSpaM
  elif difficulty==3:
    listOfWords=listOfWordsSpaH
  else:
    print("Escribe la palabra que quieres usar. Escríbela con cuidado, no podrás verla :")
    wordChosen=getpass()
    print(f"Número de letras en la palabra ingresada: {len(wordChosen)}")

                       
  wordSelection()
  wordChosenList=[]
  guessed=[]
  wordChosenLen=len(wordChosen)
  errorCounter=0
  remaining=7
  underscoreCount=0
  counter=0
  guessedCount=0
  
  for letter in range(wordChosenLen):
    guessed.append("_")
  
  for letter in wordChosen:
    wordChosenList.append(letter)
  
  def check():
    global counter
    global guessedCount
    global errorCounter
    print()
    for i in range(len(guessed)):
      print(f"{c('pink')}{guessed[i]}", sep="", end="")
    print()
    userLetter=input(f"{c('white')}\nType in a letter...\n\n")
    print()
    if userLetter not in wordChosenList:
      print(f"{c('red')}{hangmanpics[errorCounter]}")
      errorCounter+=1
      if errorCounter==7:
        print("Hangman died!")
        sys.exit("Game finished!")
    else:
      for letter in wordChosenList:
        indexLetter=wordChosenList.index(letter)
        if userLetter==wordChosenList[counter]:
          guessed[counter]=userLetter
          counter+=1
          guessedCount+=1
          if guessedCount==wordChosenLen:
            print("You won!")
            print(f"The word is: {wordChosen}")
            sys.exit("Game finished!")
        else:
          counter+=1
      counter=0
  
  while remaining>0:
    remaining-=1
    check()
else:
  print("""
  Not supported/No soportado
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
  
  """)