import random
import pymongo
import seriesjuegos

# aqui hay que editar la conexion a la bd para que funcione con tu bd


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["uf4"]
# conexion con colecciones
col_juegos = mydb["videojuegos"]
col_series = mydb["series"]

col_juegos.delete_many({})
col_series.delete_many({})

# añadimos juegos y series a la db
mylist = [{"titulo": "Nier", "horas_estimadas": 10, "entregado": False,
           "genero": "openworld", "companya": "platinum games"},

          {"titulo": "Minecraft", "horas_estimadas": 10, "entregado": False,
           "genero": "survival", "companya": "microsoft"},

          {"titulo": "Lol", "horas_estimadas": 10, "entregado": False,
           "genero": "moba", "companya": "riot games"},

          {"titulo": "Doom", "horas_estimadas": 10, "entregado": False,
           "genero": "action", "companya": "bethesda"},

          {"titulo": "hades", "horas_estimadas": 10, "entregado": False,
           "genero": "roguelike", "companya": "supergiant games"}]

col_juegos.insert_many(mylist)

mylsit = [{"titulo": "Skins", "numero_temporadas": 3, "entregado": False,
           "genero": "drama", "creador": "no se"},

          {"titulo": "brooklin99", "numero_temporadas": 3, "entregado": False,
           "genero": "comedia", "creador": "Fremulon"},

          {"titulo": "juego de tronos", "numero_temporadas": 3, "entregado": False,
           "genero": "drama", "creador": "hbo"},

          {"titulo": "stranger things", "numero_temporadas": 3, "entregado": False,
           "genero": "misterio", "creador": "Entertainment Monkey Massacre"},

          {"titulo": "modern family", "numero_temporadas": 3, "entregado": False,
           "genero": "comedia", "creador": "Lloyd-Levitan Productions"}]

col_series.insert_many(mylsit)

# bajamos los datos de la bd y los guardamos
videojuegos = []
series = []
print("Descargando los videojuegos de la bd...")
for x in col_juegos.find():
    obj = seriesjuegos.Videojuego(x["titulo"], x["genero"], x["companya"])
    videojuegos.append(obj)
print("Descargando las series de la bd...")
for x in col_series.find():
    obj = seriesjuegos.Serie(x["titulo"], x["genero"], x["creador"])
    series.append(obj)
print("")
print("Descarga finalizada.")
print("")


print("*********PRUEBA ENTREGAR**********")
# entregar series/videojuegos
for x in videojuegos:

    num = random.randint(1, 2)
    if num == 1:
        print("Videojuego " + str(x.get_titulo) + " ha sido entregado")
        x.entregar()

for x in series:
    num = random.randint(1, 2)
    if num == 1:
        print("Serie " + str(x.get_titulo) + " ha sido entregado")
        x.entregar()

print("")
# contamos cuantos son entregados y los devolvemos
print("*****PRUEBA CONTAR ENTREGADOS****")
cont_serie = 0
cont_juego = 0
for x in videojuegos:

    if x.isEntregado():
        cont_juego += 1
        x.devolver()

for x in series:

    if x.isEntregado():
        cont_serie += 1
        x.devolver()

print(str(cont_juego) + " videojuegos entregados")
print(str(cont_serie) + " series entregadas")
print("")

# mostrar juego/serie con mas horas
print("***PRUEBA MAS HORAS***")
jocdum = videojuegos[1]
seriedum = series[1]
for i in videojuegos:

    if i.horas_estimadas > jocdum.horas_estimadas:
        jocdum = i

for i in series:

    if i.numero_temp > seriedum.numero_temp:
        seriedum = i
print("Juego con mas horas:")
print(jocdum)
print("")
print("Serie con mas horas:")
print(seriedum)

