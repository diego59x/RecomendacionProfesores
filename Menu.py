#Pablo Reyna

from neo4j import GraphDatabase
from Operaciones import *
from Defensiva import *

# Banderas para las especificaciones
BanderaPreguntas = True
test = True
grafo = {'Clase':{'Quimica 1':'Carla Beatriz Caffaro','Quimica General':'Doren Sucely Amezquita','Pensamiento':['Eugenio Antonio Aristondo','Luis Fernando Alvaro','Luis Edgar Arana'],}}

# Datos
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+\t\t   Bienvenido al test de aprendizaje                       +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
while(test):
    
    opcion = input("Ingrese la opcion: \n 1.Realizar test de aprendizaje \n 2. Calificar profesor \n 3. Eliminar profesor/clase \n 4. Agregar profesor/clase \n 5. Salir \n")
    if (opcion == "1"):
                
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t Ingrese sus datos para empezar el test\t\t           +")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        Nombre = input("+\t\tFavor ingrese su nombre: ")
        Carnet = input("+\t\tFavor ingrese su carnet: ")
        Clase = input("+\t\tFavor ingrese la clase en la que necesita ayuda: ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        while (Entero(Carnet) == False):
            print("+\t\tIngrese numeros Porfavor")
            Carnet = input("+\t\tFavor ingrese su carnet: ")
            
        print("+\t\tSe dara comienzo al test...")
    #################################################################################################################
        # test
        # Pregunta 1
        print("+\t\t¿Cuál de las siguientes actividades disfrutas más?\t\t \n+\t\t 1. Escuchar musica\t\t \n+\t\t 2. Ver peliculas \t\t\n+\t\t 3. Bailar con buena musica\t\t")
       
        pregunta1 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta1) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta1 = input("\t\t")
        while ((int(pregunta1) > 3) or (int(pregunta1) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta1 = input("\t\t")
      
        # Pregunta 2
        print("+\t\tCuando conversas con otra persona, tu \n+\t\t 1. La escuchas atentamente \n+\t\t 2. La observas \n+\t\t 3. Tiendes a tocarla")
        
        pregunta2 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta2) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta2 = input("\t\t")
        while ((int(pregunta2) > 3) or (int(pregunta2) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta2 = input("\t\t")

        # Pregunta 3
        print("+\t\t¿Que tipo de examenes se te facilitan mas? \n+\t\t 1. Examen oral \n+\t\t 2. Examen escrito \n+\t\t 3. Examen de opcion multiple")
        
        pregunta3 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta3) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta3 = input("\t\t")
        while ((int(pregunta3) > 3) or (int(pregunta3) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta3 = input("\t\t")
        
            
        # Pregunta 4
        print("+\t\t¿Como te orientas mas facilmente? \n+\t\t 1. Mediante el uso de un mapa \n+\t\t 2. Pidiendo indicaciones \n+\t\t 3. A traves de la intuicion")
        
        pregunta4 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta4) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta4 = input("\t\t")
        while ((int(pregunta4) > 3) or (int(pregunta4) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta4 = input("\t\t")
        
            
        # Pregunta 5
        print("+\t\t¿De que manera se te facilita aprender algo? \n+\t\t 1. Repitiendo en voz alta \n+\t\t 2. Escribieno varias veces \n+\t\t 3. Relacionandolo con algo divertido")
        
        pregunta5 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta5) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta5 = input("\t\t")
        while ((int(pregunta5) > 3) or (int(pregunta5) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta5 = input("\t\t")
       
            
        # Pregunta 6
        print("+\t\t¿Cuando tratas de recordar algo, ¿Como lo haces? \n+\t\t 1. A traves de imagenes \n+\t\t 2. A traves de emociones \n+\t\t 3. A traves de sonidos")
        
        pregunta6 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta6) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta6 = input("\t\t")
        while ((int(pregunta6) > 3) or (int(pregunta6) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta6 = input("\t\t")
           
            
        # Pregunta 7
        print("+\t\t¿Como se te facilia entender algo? \n+\t\t 1. Cuando te lo explican verbalmente \n+\t\t 2. Cuando utilizan medios visuales \n+\t\t 3. Cuando se realiza a traves de alguna actividad")
        
        pregunta7 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta7) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta7 = input("\t\t")
        while ((int(pregunta7) > 3) or (int(pregunta7) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta7 = input("\t\t")
                
        # Pregunta 8
        print("+\t\t¿Qué es lo que más disfrutas de una habitación? \n+\t\t 1. Que sea silenciosa \n+\t\t 2. Que sea confortable \n+\t\t 3. Que esté limpia y ordenada,")
        
        pregunta8 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta8) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta8 = input("\t\t")
        while ((int(pregunta8) > 3) or (int(pregunta8) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta8 = input("\t\t")        
                
        # Pregunta 9
        print("+\t\tSi te ofrecieran uno de los siguientes empleos ¿cuál elegirías? \n+\t\t 1. Director de una estación de radio \n+\t\t 2. Director de un club deportivo \n+\t\t 3. Director de una revista")
        
        pregunta9 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta9) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta9 = input("\t\t")
        while ((int(pregunta9) > 3) or (int(pregunta9) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta9 = input("\t\t")
                
        # Pregunta 10
        print("+\t\t¿De qué manera te formas una opinión de otras personas? \n+\t\t 1. Por la sinceridad en su voz \n+\t\t 2. Por la forma de estrecharte la mano \n+\t\t 3. Por su aspecto")
        
        pregunta10 = input("\t\t")
        # Ciclos para verificar si lo ingresado es correcto, un numero y si existe entre las opciones
        while (Entero(pregunta10) == False):
            print("+\t\tIngrese numeros Porfavor")
            pregunta10 = input("\t\t")
        while ((int(pregunta10) > 3) or (int(pregunta10) < 1 )):
            print("+\t\tIngrese una opcion valida")
            pregunta10 = input("\t\t")
             
                
        # se mandan las preguntas al contador donde las segmenta y luego las recibe la grafica para mostrar su desempeño final
        #GraficaAprendisaje(Contador(pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7))
        # Se manda la lista de las respuestas segmentadas y los datos del usuario para mostrar un mensaje final
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(Reporte(Nombre, Clase, Carnet, Contador(pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9 , pregunta10)))
        #print("+\t\tUsted se puede avocar con los profesores: ", ProfesorDesignado(Listado,Contador(pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7),Clase), "\n+")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    elif (opcion == "2"):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t ¿Que profesor desea calificar?")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        profesor = input("\t\t")
        print("+\t\t Ingresa la calificacion")
        calificacion = input("\t\t")
        while (Entero(calificacion) == False):
            print("+\t\tIngrese numeros Porfavor")
            calificacion = input("\t\t")
        
    elif (opcion == "3"):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t ¿Desea eliminar un \n 1. Profesor \n 2. Clase?")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # Verificar si esta y luego alv jajaja
        opcion = input("\t\t")
        
        while ((int(opcion) > 2) or (int(opcion) < 1 )):
            print("+\t\tIngrese una opcion valida")
            opcion = input("\t\t")
        if(opcion == "1"):
            profesor = input("\t\t Ingresa el nombre del profesor:\n")
        elif(opcion == "2"):
            clase = input("\t\t Ingresa el nombre del curso:\n")
        
    elif (opcion == "4"):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t ¿Desea eliminar un \n 1. Profesor \n 2. Clase?")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # Verificar si no esta y luego que se venga papi jajaja
        opcion = input("\t\t")
        
        
        while ((int(opcion) > 2) or (int(opcion) < 1 )):
            print("+\t\tIngrese una opcion valida")
            opcion = input("\t\t")
        if(opcion == "1"):
            profesor = input("\t\t Ingresa el nombre del profesor:\n")
        elif(opcion == "2"):
            clase = input("\t\t Ingresa el nombre del curso:\n")
        
        
    elif (opcion == "5"):
        test = False
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t Esperemos te haya servido, suerte en tu proximo semestre!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+\t\t Opcion no valida")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
              
          
          
          
          
          




    