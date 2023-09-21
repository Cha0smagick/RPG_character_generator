import random
import os
from gpt4free import you
import time
import codecs

nombres_masculinos = ["Aldric", "Bryce", "Cedric", "Darius", "Edric", "Felix", "Gavin", "Hadrian", "Ivan", "Jareth", "Kael", "Liam", "Malcolm", "Nolan", "Owen", "Percival", "Quentin", "Roland", "Sebastian", "Tristan", "Ulric", "Valerian", "Wesley", "Xavier", "Yorick", "Zephyr"]
nombres_femeninos = ["Astrid", "Brienne", "Carys", "Dahlia", "Elara", "Fiona", "Gwendolyn", "Helena", "Iris", "Jasmine", "Keira", "Luna", "Morgana", "Nadia", "Ophelia", "Penelope", "Quinn", "Rowan", "Seraphina", "Thalia", "Ursula", "Violet", "Willow", "Xena", "Yara", "Zara"]
nombres_neutros = ["Avery", "Bailey", "Charlie", "Dakota", "Emery", "Finley", "Harper", "Indigo", "Jordan", "Kai", "Logan", "Morgan", "Nico", "Peyton", "Quinn", "Riley", "Sawyer", "Taylor", "Vivian", "Wyatt", "Xan", "Yael", "Zion"]

apellidos_epicos = ["Fireforge", "Ironhide", "Bloodaxe", "Stormborn", "Frosthammer", "Shadowbane", "Nightwalker", "Ravenshadow", "Dreadheart", "Soulreaper", "Skullcrusher", "Deathwhisper", "Silversong", "Starfyre", "Moonshadow", "Dragonslayer", "Stormrider", "Battlehammer", "Blackthorn", "Steelclaw"]

profesiones_fantasticas = ["Mago Arcano", "Guardián del Bosque", "Caballero de la Orden Sagrada", "Hechicera del Viento", "Explorador de las Tierras Salvajes", "Cazador de Bestias", "Alquimista de los Elementos", "Oráculo de la Profecía", "Bardo de las Melodías Épicas", "Ingeniero de las Máquinas Mágicas", "Asesino de las Sombras", "Maestro de la Espada Llameante", "Monje del Templo Perdido", "Druida de la Luna", "Guardián de las Runas Antiguas", "Bruja de los Bosques Encantados", "Paladín de la Justicia Divina", "Inquisidor de las Tinieblas", "Nigromante de los Muertos Vivientes", "Sacerdotisa de la Luz"]

profesiones_cotidianas = ["Panadero de Panes Mágicos", "Carpintero de Naves Celestiales", "Mercader de Objetos Encantados", "Cazador de Recompensas", "Agricultora de Plantas Gigantes", "Minero de Gemas Preciosas", "Artesana de Armaduras Legendarias", "Cocinero de Platos Épicos", "Pescador de Criaturas Marinas", "Cartógrafo de Tierras Desconocidas", "Bailarina del Fuego", "Arquitecto de Ciudades Flotantes", "Sanador de Heridas Milagrosas", "Herrero de Espadas Legendarias", "Domador de Bestias Fantásticas", "Guardia Real del Reino", "Ingeniera de Inventos Increíbles", "Científica de Pociones Misteriosas", "Contadora de Historias Legendarias", "Guardabosques de la Naturaleza"]

lugares_magicos_masculinos = ["Valle de la Luna", "Montañas de Dragón", "Ciudad de las Estrellas", "Bosque Encantado", "Isla de los Mares Celestiales", "Reino de la Niebla", "Abismo de la Oscuridad", "Desierto de los Milagros", "Lago de los Sueños", "Cueva de los Secretos"]
lugares_magicos_femeninos = ["Valle de la Aurora", "Montañas de la Serpiente", "Ciudad de las Flores", "Bosque de Cristal", "Isla de las Lunas Plateadas", "Reino de los Sueños Perdidos", "Abismo de la Llama Eterna", "Desierto de las Maravillas", "Lago de los Deseos", "Cueva de las Maravillas"]
lugares_magicos_neutros = ["Valle de las Maravillas", "Montañas de la Espada", "Ciudad de los Susurros", "Bosque de las Sombras", "Isla de los Secretos Olvidados", "Reino de los Sueños Prohibidos", "Abismo de los Recuerdos Perdidos", "Desierto de los Misterios", "Lago de la Eternidad", "Cueva de los Encantamientos"]

transfondos_infancia_masculinos = ["Huérfano", "Aprendiz de Mago", "Guardián de los Bosques", "Noble Exiliado", "Ladrón de las Calles", "Hijo del Herrero", "Náufrago en una Isla Desierta", "Cazador de Bestias Salvajes", "Criado por Lobos", "Rescatado por un Dragón"]
transfondos_infancia_femeninos = ["Huérfana", "Aprendiza de Hechicera", "Guardiana de los Bosques", "Noble Exiliada", "Ladrona de las Calles", "Hija del Herrero", "Náufraga en una Isla Desierta", "Cazadora de Bestias Salvajes", "Criada por Lobos", "Rescatada por un Dragón"]
transfondos_infancia_neutros = ["Huérfane", "Aprendize de Maga", "Guardiane de los Bosques", "Noble Exiliade", "Ladrone de las Calles", "Hije del Herrero", "Náufrage en una Isla Desierta", "Cazadore de Bestias Salvajes", "Criad@ por Lobos", "Rescatad@ por un Dragón"]

tipos_crianza_masculinos = ["Crianza Rigurosa", "Crianza en un Monasterio", "Crianza en un Circo Ambulante", "Crianza en la Nobleza", "Crianza en la Naturaleza", "Crianza en las Calles", "Crianza por una Hechicera", "Crianza por Gigantes", "Crianza por Enanos", "Crianza por Elfos"]
tipos_crianza_femeninos = ["Crianza Rigurosa", "Crianza en un Monasterio", "Crianza en un Circo Ambulante", "Crianza en la Nobleza", "Crianza en la Naturaleza", "Crianza en las Calles", "Crianza por un Hechicero", "Crianza por Gigantes", "Crianza por Enanos", "Crianza por Elfos"]
tipos_crianza_neutros = ["Crianza Rigurosa", "Crianza en un Monasterio", "Crianza en un Circo Ambulante", "Crianza en la Nobleza", "Crianza en la Naturaleza", "Crianza en las Calles", "Crianza por un Hechicero", "Crianza por Gigantes", "Crianza por Enanos", "Crianza por Elfos"]

tipos_voluntad_masculinos = ["Voluntad de Acero", "Voluntad Indomable", "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Trueno", "Voluntad de Agua", "Voluntad de Luz", "Voluntad de Oscuridad"]
tipos_voluntad_femeninos = ["Voluntad de Acero", "Voluntad Indomable", "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Trueno", "Voluntad de Agua", "Voluntad de Luz", "Voluntad de Oscuridad"]
tipos_voluntad_neutros = ["Voluntad de Acero", "Voluntad Indomable", "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Trueno", "Voluntad de Agua", "Voluntad de Luz", "Voluntad de Oscuridad"]

propositos_vida_masculinos = ["Proteger a los Débiles", "Buscar la Verdad Absoluta", "Vengar una Afrenta Pasada", "Descubrir un Artefacto Perdido", "Dominar las Artes Arcanas", "Erradicar el Mal del Mundo", "Restaurar un Reino Caído", "Revelar los Secretos del Universo", "Forjar una Espada Legendaria", "Crear una Nueva Orden de Caballeros"]
propositos_vida_femeninos = ["Proteger a los Débiles", "Buscar la Verdad Absoluta", "Vengar una Afrenta Pasada", "Descubrir un Artefacto Perdido", "Dominar las Artes Arcanas", "Erradicar el Mal del Mundo", "Restaurar un Reino Caído", "Revelar los Secretos del Universo", "Forjar una Espada Legendaria", "Crear una Nueva Orden de Caballeras"]
propositos_vida_neutros = ["Proteger a los Débiles", "Buscar la Verdad Absoluta", "Vengar una Afrenta Pasada", "Descubrir un Artefacto Perdido", "Dominar las Artes Arcanas", "Erradicar el Mal del Mundo", "Restaurar un Reino Caído", "Revelar los Secretos del Universo", "Forjar una Espada Legendaria", "Crear una Nueva Orden de Caballeres"]

def tirada_dado(numero_caras):
    return random.randint(1, numero_caras)

def generar_stats():
    stats = []
    for _ in range(6):
        total = tirada_dado(20)
        stats.append(total)
    return stats

def generar_nombre_sexo():
    nombre = random.choice(nombres_masculinos + nombres_femeninos + nombres_neutros)
    sexo = ""
    if nombre in nombres_masculinos:
        sexo = "Masculino"
    elif nombre in nombres_femeninos:
        sexo = "Femenino"
    else:
        sexo = "???"
    return nombre, sexo

def generar_apellido():
    return random.choice(apellidos_epicos)

def generar_profesion():
    profesiones = profesiones_fantasticas + profesiones_cotidianas
    return random.choice(profesiones)

def generar_lugar_magico(sexo):
    if sexo == "Masculino":
        return random.choice(lugares_magicos_masculinos)
    elif sexo == "Femenino":
        return random.choice(lugares_magicos_femeninos)
    else:
        return random.choice(lugares_magicos_neutros)

def generar_transfondo_infancia(sexo):
    if sexo == "Masculino":
        return random.choice(transfondos_infancia_masculinos)
    elif sexo == "Femenino":
        return random.choice(transfondos_infancia_femeninos)
    else:
        return random.choice(transfondos_infancia_neutros)

def generar_tipo_crianza(sexo):
    if sexo == "Masculino":
        return random.choice(tipos_crianza_masculinos)
    elif sexo == "Femenino":
        return random.choice(tipos_crianza_femeninos)
    else:
        return random.choice(tipos_crianza_neutros)

def generar_tipo_voluntad(sexo):
    if sexo == "Masculino":
        return random.choice(tipos_voluntad_masculinos)
    elif sexo == "Femenino":
        return random.choice(tipos_voluntad_femeninos)
    else:
        return random.choice(tipos_voluntad_neutros)

def generar_proposito_vida(sexo):
    if sexo == "Masculino":
        return random.choice(propositos_vida_masculinos)
    elif sexo == "Femenino":
        return random.choice(propositos_vida_femeninos)
    else:
        return random.choice(propositos_vida_neutros)

def generar_historia_lugar(lugar):
    inicio_historia = random.choice(["Nació", "Creció", "Fue criado", "Fue destinado"]) + " en"
    medio_historia = random.choice(["los", "las", "un"]) + " " + lugar
    final_historia = random.choice(["y luchó contra", "enfrentándose a", "descubriendo", "explorando"]) + " " + random.choice(["peligrosos enemigos", "oscuros secretos", "poderosas criaturas mágicas"])
    return inicio_historia + " " + medio_historia + ", " + final_historia + "."

def generar_historia_profesion(profesion):
    inicio_historia = random.choice(["Dominó", "Desafió", "Sirvió", "Exploró"]) + " como"
    medio_historia = random.choice(["los", "las", "un"]) + " " + profesion
    final_historia = random.choice(["ganando renombre", "salvando vidas", "forjando alianzas", "superando desafíos"]) + " " + random.choice(["épicos", "legendarios", "inolvidables", "mágicos"])
    return inicio_historia + " " + medio_historia + ", " + final_historia + "."

def generar_historia_apellido(apellido):
    inicio_historia = random.choice(["Su apellido", "La historia de su familia", "El linaje de los"]) + " " + apellido
    final_historia = random.choice(["está lleno de", "ha estado marcado por", "es conocido por"]) + " " + random.choice(["heroicas hazañas", "antiguas leyendas", "poderosos guerreros", "destinos trágicos"])
    return inicio_historia + " " + final_historia + "."

# Generar y mostrar el nombre, apellido y sexo del personaje
nombre_personaje, sexo_personaje = generar_nombre_sexo()
apellido_personaje = generar_apellido()


# Generar y mostrar la profesión del personaje
profesion_personaje = generar_profesion()

# Generar y mostrar el trasfondo épico del personaje
lugar_magico = generar_lugar_magico(sexo_personaje)
transfondo_infancia = generar_transfondo_infancia(sexo_personaje)
tipo_crianza = generar_tipo_crianza(sexo_personaje)
tipo_voluntad = generar_tipo_voluntad(sexo_personaje)
proposito_vida = generar_proposito_vida(sexo_personaje)


# Generar y mostrar los stats del personaje
stats_personaje = generar_stats()

def escribir_info_en_archivo(nombre, apellido, sexo, profesion, lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida, stats):
    with open("personaje.txt", "w") as archivo:
        archivo.write(f"Nombre del personaje: {nombre} ")
        archivo.write(f"Apellido del personaje: {apellido} ")
        archivo.write(f"Sexo del personaje: {sexo} ")
        archivo.write(f"Profesión del personaje: {profesion} ")
        archivo.write(f"{nombre} {apellido}, {generar_historia_lugar(lugar_magico)} {generar_historia_apellido(apellido)} ")
        archivo.write(f"Desde una tierna infancia fue {transfondo_infancia} y recibió una {tipo_crianza} que moldeó su carácter. ")
        archivo.write(f"Posee experiencia porque el {generar_historia_profesion(profesion)} y ha jurado {proposito_vida}. ")
        archivo.write("Stats del personaje: ")
        nombres_stats = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
        for nombre, valor in zip(nombres_stats, stats):
            archivo.write(f"{nombre}: {valor} ")

# Generar y mostrar el nombre, apellido y sexo del personaje
nombre_personaje, sexo_personaje = generar_nombre_sexo()
apellido_personaje = generar_apellido()

# Generar y mostrar la profesión del personaje
profesion_personaje = generar_profesion()

# Generar y mostrar el trasfondo épico del personaje
lugar_magico = generar_lugar_magico(sexo_personaje)
transfondo_infancia = generar_transfondo_infancia(sexo_personaje)
tipo_crianza = generar_tipo_crianza(sexo_personaje)
tipo_voluntad = generar_tipo_voluntad(sexo_personaje)
proposito_vida = generar_proposito_vida(sexo_personaje)

# Generar y mostrar los stats del personaje
stats_personaje = generar_stats()

# Llamar a la función para escribir la información en el archivo
escribir_info_en_archivo(nombre_personaje, apellido_personaje, sexo_personaje, profesion_personaje, lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida, stats_personaje)

print("Información del personaje guardada en 'personaje.txt'")

# Función para obtener una respuesta sin "Unable to fetch the response, Please try again."
def obtener_respuesta(prompt, chat):
    while True:
        response = you.Completion.create(
            prompt=prompt,
            chat=chat
        )
        text = response.text.strip()
        if text != "Unable to fetch the response, Please try again.":
            return text

        time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente

# Inicializar el chat vacío
chat = []

# Pedir al usuario la ruta del archivo .txt
archivo_txt = os.path.join(os.getcwd(), "personaje.txt")

try:
    with open(archivo_txt, "r", encoding="utf-8") as archivo_entrada:
        contenido = archivo_entrada.read()
except FileNotFoundError:
    print("El archivo especificado no se encontró.")
    exit()

# Agregar el contenido del archivo al chat
chat.append({"question": contenido, "answer": ""})

# Filtrar el contenido eliminando las líneas del entrevistador
contenido_filtrado = "\n".join([linea for linea in contenido.splitlines() if not linea.strip().startswith("Entrevistador:")])

# Obtener respuesta del modelo
respuesta_bot = obtener_respuesta("actúa como un maestro diseñador de personajes de fantasia con maestría en estudios de escritura y generación de lore y backgrounds de personajes. A continuación voy a darte la información de un personaje. necesito que me devulevas la hoja de personaje con todas las características imputadas, pero también necesito que a partir de la información imputada le inventes un background épico muy extenso y detallado con nombres propios fantasticos inventados y asignados para personas y lugares y objetos determinantes para el personaje. tambien inventa y describe caratcerísticas unicas del personaje, asi como habilidades natas con base en sus atributos, fortalezas, fobias, etica y moral, alineacion moral, traumas, personalidad y propósito en la vida, con nombres propios de personajes,lugares y crituras relevantes. Debes añadir ese background a la hoja de personaje como si fuese su pasado personalizado muy extenso y detallado. recuerda que es un juego de rol de fantasía así que puedes inventar cuanto quieras, basado en multiples juegos de rol y eso incluye nombres, lugares, fechas, epocas, tecnologia, magia y lore propio del personaje. Extiende la historia del personaje lo que más puedas con todos los detalles personalizados posibles que puedas añadir. devuélveme una hoja de personaje lo más completa y jugable posible con todas las características solicitadas legibles y con numeros que puedan ser mesurables para cada habilidad, fobia y trauma en una escala apropiada y estandard para todos los stats. tambien debe sinventar una serie de hechizos relacionados a la clase del personaje, teniendo en cuenta que si el personaje esta relacionado con la magia debe tener mas hechizos y si no, debe tener menos relacionados con su propio lore y atributos y características unicas\n\n" + contenido_filtrado, chat)

# Imprimir la respuesta formateada en la consola
respuesta_bot_legible = codecs.decode(respuesta_bot, 'unicode_escape')
print("Bot:", respuesta_bot_legible)

# Guardar la respuesta en un archivo de salida con el formato adecuado
with codecs.open("personaje_con_background.txt", "w", "utf-8") as archivo_respuestas:
    archivo_respuestas.write(respuesta_bot_legible)

print("Hoja de personaje con background guardada en 'personaje_con_background.txt'")
