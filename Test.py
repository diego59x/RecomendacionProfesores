from neo4j import GraphDatabase


driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"), encrypted = False)

def recomendacion(tx, tt, cu):
    for record in tx.run(" MATCH (n:Professor)-[k:TeacherFor]->(c:Course) "
                         " MATCH (p:Professor {name: n.name})-[r:TeachingType]-(t:TeachingType) "
                         " WHERE t.name = {variabletipoaprendizaje} AND c.name ={variablenombrecurso}"
                         " RETURN r, p,t "
                         " ORDER BY r.rating DESC ", variabletipoaprendizaje=tt, variablenombrecurso = cu  ):
        print(record["r, p,t "])

with driver.session() as session:
    session.read_transaction(recomendacion, "visual", "PENSAMIENTO CUANTITATIVO")

driver.close()
