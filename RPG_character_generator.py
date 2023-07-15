import random

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
    historia = ""
    if lugar in lugares_magicos_masculinos:
        historia = "Exploró los profundos valles de la Luna, descubriendo los secretos ocultos de antiguas razas."
    elif lugar in lugares_magicos_femeninos:
        historia = "Recorrió los bosques de cristal en busca de la verdad y la sabiduría ancestral de las lunas plateadas."
    else:
        historia = "Se aventuró en el misterioso Valle de las Maravillas, enfrentando peligros y desentrañando enigmas."
    return historia

def generar_historia_profesion(profesion):
    historia = ""
    if profesion in profesiones_fantasticas:
        historia = "Dominó los elementos y desató poderosos hechizos para proteger a los indefensos y mantener el equilibrio en el mundo."
    elif profesion in profesiones_cotidianas:
        historia = "Construyó una reputación como el mejor artesano de armaduras legendarias, forjando protección impenetrable para los valientes guerreros."
    return historia

def generar_historia_apellido(apellido):
    historia = f"El apellido {apellido} resonaba en los corazones de aquellos que conocían su legado épico, evocando historias de heroísmo y valentía."
    return historia

def imprimir_stats(stats):
    nombres_stats = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
    for nombre, valor in zip(nombres_stats, stats):
        print(f"{nombre}: {valor}")

def imprimir_trasfondo_epico(personaje, lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida):
    historia_lugar = generar_historia_lugar(lugar_magico)
    historia_profesion = generar_historia_profesion(profesion_personaje)
    historia_apellido = generar_historia_apellido(apellido_personaje)

    if personaje[1] == "Masculino":
        print(f"\n{personaje[0]}, el valiente {personaje[1]}, nació en {lugar_magico}. {historia_lugar} Desde una tierna infancia, fue {transfondo_infancia} y recibió una {tipo_crianza} que moldeó su carácter. Posee una voluntad de {tipo_voluntad} y ha jurado {proposito_vida}. {historia_profesion} {historia_apellido}")
    elif personaje[1] == "Femenino":
        print(f"\n{personaje[0]}, la intrépida {personaje[1]}, nació en {lugar_magico}. {historia_lugar} Desde una tierna infancia, fue {transfondo_infancia} y recibió una {tipo_crianza} que moldeó su carácter. Posee una voluntad de {tipo_voluntad} y ha jurado {proposito_vida}. {historia_profesion} {historia_apellido}")
    else:
        print(f"\n{personaje[0]}, el misterioso {personaje[1]}, nació en {lugar_magico}. {historia_lugar} Desde una tierna infancia, fue {transfondo_infancia} y recibió una {tipo_crianza} que moldeó su carácter. Posee una voluntad de {tipo_voluntad} y ha jurado {proposito_vida}. {historia_profesion} {historia_apellido}")

# Generar y mostrar el nombre, apellido y sexo del personaje
nombre_personaje, sexo_personaje = generar_nombre_sexo()
apellido_personaje = generar_apellido()

print("Nombre del personaje:", nombre_personaje)
print("Apellido del personaje:", apellido_personaje)
print("Sexo del personaje:", sexo_personaje)

# Generar y mostrar la profesión del personaje
profesion_personaje = generar_profesion()
print("Profesión del personaje:", profesion_personaje)

# Generar y mostrar el trasfondo épico del personaje
lugar_magico = generar_lugar_magico(sexo_personaje)
transfondo_infancia = generar_transfondo_infancia(sexo_personaje)
tipo_crianza = generar_tipo_crianza(sexo_personaje)
tipo_voluntad = generar_tipo_voluntad(sexo_personaje)
proposito_vida = generar_proposito_vida(sexo_personaje)

imprimir_trasfondo_epico((nombre_personaje, sexo_personaje), lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida)

# Generar y mostrar los stats del personaje
stats_personaje = generar_stats()
print("\nStats del personaje:")
imprimir_stats(stats_personaje)

