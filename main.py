# Hangman game

# Libraries

import random, sys, os, time
from getpass import getpass

# Graphics

scaffold='''
 +---+
     |
     |
     |
     |
     |
=========
'''

hangmanpics=[
'''
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

bigtitle={'en':"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""", 'es':"""
             _                             _       
     /\   | |                           | |      
    /  \  | |__   ___  _ __ ___ __ _  __| | ___  
   / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
  / ____ \| | | | (_) | | | (_| (_| | (_| | (_) |
 /_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ 
     
"""}

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

youLooseASCI={"es":'''

██████╗░███████╗██████╗░██████╗░██╗░██████╗████████╗███████╗██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝██║
██████╔╝█████╗░░██████╔╝██║░░██║██║╚█████╗░░░░██║░░░█████╗░░██║
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝
██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝░░░██║░░░███████╗██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝
''', "en":"""

██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝██║
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░██║
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝
"""}

youWinASCI={'es':'''

░██████╗░░█████╗░███╗░░██╗░█████╗░░██████╗████████╗███████╗██╗
██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║
██║░░██╗░███████║██╔██╗██║███████║╚█████╗░░░░██║░░░█████╗░░██║
██║░░╚██╗██╔══██║██║╚████║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝
╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝░░░██║░░░███████╗██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝
''','en':'''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═╝
'''
}

# Global variables

errorCounter=0
remaining=7
underscoreCount=0
counter=0
guessedCount=0
chosenWord=''
wordLetters=[]
guessed=[]
listofWords=()
lan=''
txt={}
words={}

# Words

enE=('Also Aged Back Ball Bend Come Card Chat Cook Each Ever Four Feel Fine Gone Have Hear Jump Life Main More Open Pull Able Away Bank Base Bell Came Coat Cash Cool Evil Face Five Fell Fish Gold Hair Into Kick Like Move Nose Only Sell Acid Baby Been Busy Bird Calm City Crow Dark Even Fact Fair Fire Game Girl Here Iron Kill Love Meet Near Push Sale ').lower().split()

enM=('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ').lower().split()

enH=('Connecticutian Jackasseries Impedimenta Tergiversation     Polyphiloprogenitive Embourgeoisement Xenotransplantation Myrmecophilous Omphaloskepsis Trichotillomania Psychotomimetic Consanguineous Pulchritudinous Sesquipedalian Onomatopoeia Worcestershire').lower().split()

esE=('De La Que El En Y A Los Se Del Las Un Por Con No Una Su Para Es Al Lo Como Más O Pero Sus Le Ha Me Si Sin Sobre Este Ya Entre Cuando Todo Esta Ser Son Dos También Fue Había Era Muy Años Hasta Desde Está Mi Porque Qué Sólo Han Yo Hay Vez Puede Todos Así Nos Ni Parte Tiene Él Uno Donde Bien Tiempo Mismo Ese Ahora Cada E Vida Otro Después Te Otros Aunque Esa Eso Hace Otra Gobierno Tan Durante Siempre Día Tanto Ella Tres Sí Dijo Sido Gran País Según Menos Año Antes Estado Contra Sino Forma Caso Nada Hacer General Estaba Poco Estos Presidente Mayor Ante Unos Les Algo Hacia Casa Ellos Ayer Hecho Primera Mucho Mientras Además Quien Momento Millones Esto España Hombre Están Pues Hoy Lugar Madrid Nacional Trabajo Otras Mejor Nuevo Decir Algunos Entonces Todas Días Debe Política Cómo Casi Toda Tal Luego Pasado Primer Medio Va Estas Sea Tenía Nunca Poder Aquí Ver Veces Embargo Partido Personas Grupo Cuenta Pueden Tienen Misma Nueva Cual Fueron Mujer Frente José Tras Cosas Fin Ciudad He Social Manera Tener Sistema Será Historia Muchos Juan Tipo Cuatro Dentro Nuestro Punto Dice Ello Cualquier Noche Aún Agua Parece Haber Situación Fuera Bajo Grandes Nuestra Ejemplo Acuerdo Habían Usted Estados Hizo Nadie Países Horas Posible Tarde Ley Importante Guerra Desarrollo Proceso Realidad Sentido Lado Mí Tu Cambio Allí Mano Eran Estar San Número Sociedad Unas Centro Padre Gente Final Relación Cuerpo Obra Incluso Través Último Madre Mis Modo Problema Cinco Carlos Hombres Información Ojos Muerte Nombre Algunas Público Mujeres Siglo Todavía Meses Mañana Esos Nosotros Hora Muchas Pueblo Alguna Dar Problema Don Da Tú Derecho Verdad María Unidos Podría Sería Junto Cabeza Aquel Luis Cuanto Tierra Equipo Segundo Director Dicho Cierto Casos Manos Nivel Podía Familia Largo Partir Falta Llegar Propio Ministro Cosa Primero Seguridad Hemos Mal Trata Algún Tuvo Respecto Semana Varios Real Sé Voz Paso Señor Mil Quienes Proyecto Mercado Mayoría Luz Claro Iba Éste Pesetas Orden Español Buena Quiere Aquella Programa Palabras Internacional Van Esas Segunda Empresa Puesto Ahí Propia M Libro Igual Político Persona Últimos Ellas Total Creo Tengo Dios C Española Condiciones México Fuerza Solo Único Acción Amor Policía Puerta Pesar Zona Sabe Calle Interior Tampoco Música Ningún Vista Campo Buen Hubiera Saber Obras Razón Ex Niños Presencia Tema Dinero Comisión Antonio Servicio Hijo Última Ciento Estoy Hablar Dio Minutos Producción Camino Seis Quién Fondo Dirección Papel Demás Barcelona Idea Especial Diferentes Dado Base Capital Ambos Europa Libertad Relaciones Espacio Medios Ir Actual Población Empresas Estudio Salud Servicios Haya Principio Siendo Cultura Anterior Alto Media Mediante Primeros Arte Paz Sector Imagen Medida Deben Datos Consejo Personal Interés Julio Grupos Miembros Ninguna Existe Cara Edad Etc. Movimiento Visto Llegó Puntos Actividad Bueno Uso Niño Difícil Joven Futuro Aquellos Mes Pronto Soy Hacía Nuevos Nuestros Estaban Posibilidad Sigue Cerca Resultados Educación Atención González Capacidad Efecto Necesario Valor Aire Investigación Siguiente Figura Central Comunidad Necesidad Serie Organización Nuevas Calidad').lower().split()

esM = ('ablandar aborigen abreviar acarrear acogedor adjetivo adjuntar afrontar agrícola alcayata almohada aminorar aparecer apreciar arbitrar atenazar atrevido aventura avestruz bailarín baluarte baratija barbacoa bebedizo bendecir blancura bofetada bombilla bordillo braguero cabestro cafetera calcular califato callejón calzador camarero capturar carruaje carrusel cartilla cartucho castillo catarata celebrar cellisca cerilla chistera circuito circular codorniz cofradía colgante colonial comparar comparsa concebir conceder concepto consulta contrato converso convicto convulso correcto corredor creación creativo creencia culminar cultural dactilar decisión degradar degustar delgadez deprimir desacato desatino descoser descuido desguace deshacer destacar destapar destello devuelto dictamen diminuto diputado disolver dolorido dualidad duradero efectuar elevador embeleso empalmar emplazar encantar encestar endémico enfático ensalada entender envuelto erupción escalope escombro espinoso espumoso esquimal estatura estofado estudiar eventual evocador exaltado explorar expulsar extracto fabricar fabuloso fanático fandango favorito fechoría fecundar femenino festejar flaqueza florista folletín fonética forajido frondoso gabinete galápago garbanzo generoso genética grabador graduado guisante guitarra habanero hechizar herético holgazán homónimo hospital humildad ilustrar imaginar imprenta impulsar incienso incierto inculpar indultar inocente insignia insuflar insumiso intentar invasión isotermo jabalina jacobino jilguero justicia juventud labranza ladrillo lanosta lanzador lastimar licencia liquidez luchador magnolia maletero mamífero maniobra medieval mercader merendar misterio molestar molinero moraleja nebulosa nervioso obelisco octaedro olfatear ondulado opositor original orquídea pabellón palomita paraguas pasajero pastoril percutor perdurar perezoso perfecto pergeñar pistacho pleitear poltrona populoso portería precepto préstamo probable probador producto profesor provocar puñetazo purgante raspador reactivo reavivar recortar reiterar renegado reproche repuesto reservar revolcar rupestre sacudida seductor segmento sencillo sensible servicio simetría sobornar sorpresa subsuelo suciedad sufragio sustento taburete tangente terminar tornillo torrente traducir travesía vainilla variedad ventisca vocativo vorágine').lower().split()

esH = ('Otorrinolaringólogo Idiosincrasia Desoxirribonucleico Paralelepípedo Ovovivíparo Caleidoscopio Electroencefalografista Hipopotomonstrosesquipedaliofobia Supercalifragilísticoespialidoso Pneumonoultramicroscopicsilicovolcanoconiosis parangaricutirimicuaro').lower().split()

es={'easy':esE, 'medium':esM,'hard':esH}
en={'easy':enE, 'medium':enM,'hard':enH}
words={'en':en, 'es':es}

# Subroutines
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

def txts(key):
  global lan
  if lan=='en':
    print(txt['en'][key])
  elif lan=='es':
    print(txt['es'][key])
  else:
    print("Unsupported language / Lenuaje no soportado")

def wSel(diff):
  global listOfWords
  global chosenWord
  if diff==1:
    listOfWords=words[lan]['easy']
    chosenWord=random.choice(listOfWords)
  elif diff==2:
    listOfWords=words[lan]['medium']
    chosenWord=random.choice(listOfWords)
  elif diff==3:
    listOfWords=words[lan]['hard']
    chosenWord=random.choice(listOfWords)
  else:
    print(" ")
    chosenWord=getpass()
    txts('wordlen')

def check():
    global counter
    global guessedCount
    global errorCounter
    global remaining
    # if counter==0 or errorCounter==0:
    #   print(f"{c('purple')}{littleTitle[lan]}")
    #   print(f"{c('purple')}{scaffold}")
    print()
    for i in range(len(guessed)):
      print(guessed[i], sep="", end="")
    print()
    txts('input')
    userLetter=input().lower()
    os.system("clear")
    print()
    if userLetter not in wordLetters:
      remaining-=1
      print(f"{c('red')}{littleTitle[lan]}")
      print(hangmanpics[errorCounter])
      errorCounter+=1
      txts('error')
      if errorCounter==1:
        txts('error1')
      elif errorCounter==2:
        txts('error2')
      elif errorCounter==3:
        txts('error3')
      elif errorCounter==4:
        txts('error4')
      elif errorCounter==5:
        txts('error5')
      elif errorCounter==6:
        txts('error6')
      elif errorCounter==7:
        txts('error7')
        print(youLooseASCI[lan])
        print(f"{txts('word')} {chosenWord}")
    else:
      if errorCounter==0 or counter==0:
        print(f"{c('green')}{littleTitle[lan]}")
        print(f"{c('green')}{scaffold}")
      else:
        print(f"{c('green')}{littleTitle[lan]}")
        print(f"{c('green')}{hangmanpics[errorCounter]}")
      for letter in wordLetters:
        indexLetter=wordLetters.index(letter)
        if userLetter==wordLetters[counter]:
          guessed[counter]=userLetter
          counter+=1
          guessedCount+=1
          if guessedCount==chosenWordLen:
            print(youWinASCI[lan])
            print()
            print(f"The word is: {chosenWord}")
        else:
          counter+=1
      counter=0

# Text dictionaries

en={
  'lanSel':'You chosed english', 
  'difficulty':'Choose the difficulty:\n\n1. Easy\n2. Medium\n3. Hard\n4. Write a word of your choice\n\n ', 
  'unsupported':'Unsupported',
  'error':'The letter is not in the word!',
  'error1':'One more step on the scaffold!',
  'error2':'The neck is not for the rope!',
  'error3':'Do you really want to rescue it? It seems that you want to hang it',
  'error4':'With one foot on the other side!',
  'error5':'Half a lenth of a hanged man',
  'error6':'Good! Now you have one foot in the afterlife!',
  'error7':'Hangman has died ☠',
  'wordinput':"Write the word you want to use and press enter (You won't be able to see it):\n",
  'input':'Type in a letter...\n\n',
  'repeat':'Play again? Press "y" for yes or any other key to exit...',
  'exit':'Bay! Hangman awaits for you 😔',
  'word':'The word was: '
}

es={
  'lanSel':'Elegiste español', 
  'difficulty':'Elige la dificultad:\n\n1. Fácil\n2. Medio\n3. Difícil\n4. escribe una palabra de tu elección\n\n', 
  'unsupported':'No soportado',
  'error':'¡La letra no está en la palabra!',
  'error1':'¡Un paso más en el cadalso!',
  'error2':'¡El cuello no es pa la soga!',
  'error3':'¿en verdad quieres salvarlo? Pareciera que lo quieres colgar',
  'error4':'¡Con un pie en el otro lado!',
  'error5':'A medio cuerpo de un ahorcado',
  'error6':'¡Bien! ¡Ahora tienes un pie en el más allá!',
  'error7':'El Ahorcado ha muerto ☠',
  'wordinput':'Escribe la palabra que quieres usar y presiona enter (No podrás verla):\n',
  'wordlen':f"Número de letras en la palabra ingresada: {len(chosenWord)}",
  'input':'escribe una letra...\n\n',
  'repeat':'¿Jugar de nuevo? Presiona "S" para Sí o cualquier otra tecla para salir...',
  'exit':'!Adiós! El Ahorcado espera por ti 😔',
  'word':'La palabra era: '
}

txt={'en':en, 'es':es}

# Language selection
while True:
  lan=int(input("""Choose language  / Elige lenuaje:

1. English
2. Español

""").lower())
  if lan==1 or lan=='english' or lan=='English' or lan=='1.English' or lan=='1. English':
    lan="en"
    break
  elif lan==2 or lan=='español' or lan=='Español' or lan=='2.Español' or lan=='2. Español':
    lan="es"
    break
  else:
    print('Not available. Try again... / No disponible, prueba de nuevo')
    continue
txts('lanSel')
while True:
  os.system("clear")
  print(f"{c('purple')}{bigtitle[lan]}")  
  txts('difficulty')
  difficulty=int(input(""))
  wSel(difficulty)
  os.system("clear")
  for letter in littleTitle[lan]:
    sys.stdout.write(letter)
    time.sleep(.005)
  print(f"{c('purple')}{hangmanpics[errorCounter]}")
  chosenWordLen=len(chosenWord)
  for letter in range(chosenWordLen):
    guessed.append("_")
  for letter in chosenWord:
    wordLetters.append(letter)
  while remaining>0:
    if guessedCount==chosenWordLen:
      break
    check()
  txts('repeat')
  print()
  again=input()
  if again=='y' or again=='Y' or again=='S' or again=='s':
    continue
  else:
    sys.exit(txts('exit'))