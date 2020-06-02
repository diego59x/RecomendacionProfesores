# Pablo Reyna 10% del trabajo
# Cesar vinicio 20% del trabajo
# Diego Alvaarez 70% del trabajo
from neo4j import GraphDatabase

def inicio():
    db = GraphDatabase.driver("bolt://localhost:7687", auth = ("neo4j","1234"), encrypted = False)
    return db
def close(db):
    db.close()
    
  
def mostrarProfesores(db):
    profesores = []
    nombre = "Professor"
    session = db.session()
    ql = "MATCH (x:%s) RETURN x"%nombre
    nodos = session.run(ql)
    nodos = list(nodos)
    
    try:
        for profesor in nodos:
            profesores.append(dict(dict(profesor)['x'])['name'])
    except:
        for profesor in nodos:
            profesores.append(dict(dict(profesor)['x'])['nombre'])
    return profesores
def borrar(db,profesor,clase,aprendizaje):
    session = db.session()
    eliminarClase = """MATCH (a:Profesor), (b:Clase)
    WHERE a.nombre = '%s' AND b.name = '%s' 
    DELETE a, b """%(profesor, clase)
    
    eliminarAprendizaje = """MATCH (a:Profesor), (b:Aprendizaje)
    WHERE a.nombre = '%s' AND b.name = '%s' 
    DELETE a, b """%(profesor, aprendizaje)
    
    session.run(eliminarClase)
    session.run(eliminarAprendizaje)

def crear(db,profesor,clase,aprendizaje):
    session = db.session()
    Create_1 = """Create(%s:Profesor {nombre:"%s"})
    CREATE (%s:Clase {nombre: %s})
    CREATE (%s)-[:TeacherFor]->(%s)
    CREATE (%s:Aprendizaje {nombre: %s})
    CREATE (%s)-[:TeachingType]->(%s)
    """%(profesor,profesor,clase,clase, profesor, clase, aprendizaje, aprendizaje, profesor, aprendizaje)
    
    Clase = """MATCH (a:Profesor), (b:Clase)
    WHERE a.nombre = '%s' AND b.name = '%s'
    CREATE (a)-[:TeacherFor]->(b)

    """%(profesor,clase)
     
    Clase1 = """MATCH (a:Profesor), (b:Aprendizaje)
    WHERE a.nombre = '%s' AND b.name = '%s'
    CREATE (a)-[:TeachingType]->(b)

    """%(profesor,aprendizaje)
    session.run(Clase)
    session.run(Clase1)
 
# Contadores de preguntas
def Contador(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    # Se crea una lista con las respuestas del usuario y se convierten a enteros
    respuestas = [int(num1), int(num2), int(num3), int(num4), int(num5), int(num6), int(num7), int(num8), int(num9), int(num10)]
    # Contadores de preguntas
    contadorV = 0
    contadorA = 0
    contadorC = 0
    # Se recorre la lista de respuestas y dependiendo de lo que ha respondido se hace el conteo
    # de respuestas, si es "Visual", "Auditivo" o "Cinestesico"
    for i in range(len(respuestas)):
        if (respuestas[i] == 1):
            contadorV += 1
        elif (respuestas[i] == 2):
            contadorA += 1
        elif (respuestas[i] == 3):
            contadorC += 1
            
    lista = [contadorV, contadorA, contadorC]
    return lista
# Se muestra un reporte de lo que ha ingresado el usuario con su aprendisaje
def Reporte(nom, clase, carnet, respuestas):
    
    if ((respuestas[0]>respuestas[1]) and (respuestas[0]>respuestas[2])):
        tipo = "Visual"
    elif ((respuestas[1]>respuestas[0]) and (respuestas[1]>respuestas[2])):
        tipo = "Auditivo"
    elif ((respuestas[2]>respuestas[0]) and (respuestas[2]>respuestas[1])):
        tipo = "Cinestesico"
    else:
        tipo = "Hubo un problema, no se pudo calcular :/"
    datos = []
    datos.append("+\t\tNombre: " + nom + "\n+\t\tClase en la que necesita ayuda: " + clase + "\n+\t\tCarnet: " + carnet + "\n+\t\tSu tipo de aprendisje es: " + tipo)
    datos.append(tipo)
    return datos


def recomendacion(db, tt, cu):
    session = db.session()
    for record in session.run(" MATCH (n:Professor)-[k:TeacherFor]->(c:Course) "
                         " MATCH (p:Professor {name: n.name})-[r:TeachingType]-(t:TeachingType) "
                         " WHERE t.name = $variabletipoaprendizaje AND c.name = $variablenombrecurso"
                         " RETURN r, p,t "
                         " ORDER BY r.rating DESC ", variabletipoaprendizaje=tt, variablenombrecurso = cu  ):
        print(record["r, p,t "])

    




