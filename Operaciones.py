#Pablo Reyna

from neo4j import GraphDatabase

def inicio():
    driver = GraphDatabase.driver(uri ="bolt://localhost:7687", auth = ("neo4j","123456"), encrypted = False)
    
def close():
    driver.close()
    
def mostrar():
    session = driver.session()
    ql = "MATCH teachingTypes=()-[:teachingTypes]-() RETURN(teachingTypes)"
    nodos = session.run(ql)
    for nodos in nodos:
        print(nodos)
        
def mostrarProfesores():
    session = driver.session()
    ql = "MATCH teacherfor=()-[:TeacherFor]-() RETURN(teacherfor)"
    nodos = session.run(ql)
    for nodos in nodos:
        print(nodos)
        
def create_person(driver, name):
    with driver.session() as session:
        return session.run("CREATE (a:Person {name:$name}) "
                           "RETURN id(a)", name=name).single().value()


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
    datos = "+\t\tNombre: " + nom + "\n+\t\tClase en la que necesita ayuda: " + clase + "\n+\t\tCarnet: " + carnet + "\n+\t\tSu tipo de aprendisje es: " + tipo + " los profesores a los que se puede avocar son Amalia, Aristondo"
    return datos

def ProfesorDesignado(profesores, aprendisaje, clase):
    
    if ((aprendisaje[0]>aprendisaje[1]) and (aprendisaje[0]>aprendisaje[2])):
        tipo = "Visual"
    elif ((aprendisaje[1]>aprendisaje[0]) and (aprendisaje[1]>aprendisaje[2])):
        tipo = "Auditivo"
    elif ((aprendisaje[2]>aprendisaje[0]) and (aprendisaje[2]>aprendisaje[1])):
        tipo = "Cinestesico"
    else:
        tipo = "Hubo un problema, no se pudo calcular :/"

    nombres = ""
    tipoAprendisaje = 2
    for coma in profesores:
        if tipo == coma[2] and clase == coma[1]:
            nombres += coma[0] + ", "
    
    return nombres
def recomendacion(tx, tt, cu):
    for record in tx.run(" MATCH (n:Professor)-[k:TeacherFor]->(c:Course) "
                         " MATCH (p:Professor {name: n.name})-[r:TeachingType]-(t:TeachingType) "
                         " WHERE t.name = {variabletipoaprendizaje} AND c.name ={variablenombrecurso}"
                         " RETURN r, p,t "
                         " ORDER BY r.rating DESC ", variabletipoaprendizaje=tt, variablenombrecurso = cu  ):
        print(record["r, p,t "])

    
    




