from config.configuration import db, collection

def mensajepersonaje(nombre):
    """
    Hago una query a la base de datos para sacar las frases de una persona
    """
    query = {"speaker": f"{nombre}"}
    frases = list(collection.find(query,{"_id":0, "date":0}))
    return frases 