from config.configuration import db, collection

# añade los datos en Mongo
def insertmensaje(tiempo, personaje, frase):
    
    dict_insert = { "date" : f"{tiempo}", 
    "speaker" : f"{personaje}", 
    "speech" : f"{frase}"
    }
    collection.insert_one(dict_insert)

    """
    Lo meto en la base de datos previo s
    """

