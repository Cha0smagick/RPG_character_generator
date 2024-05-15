import streamlit as st
import textwrap
import google.generativeai as genai
import random
import os
import time
import base64

# Listas de nombres, apellidos, profesiones, etc.
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

tipos_crianza_masculinos = ["Maestro en las Artes Arcanas", "Sabio del Bosque", "Comandante de la Orden", "Maestro de las Tempestades", "Explorador Legendario", "Rey de las Bestias", "Alquimista Famoso", "Vidente de las Estrellas", "Bardo del Reino", "Ingeniero Maestro", "Maestro Asesino", "Maestro de la Espada", "Anciano del Templo", "Guardián de las Runas", "Sabio del Bosque", "Caballero de la Justicia", "Inquisidor Valiente", "Nigromante Poderoso", "Sacerdote de la Luz"]
tipos_crianza_femeninos = ["Maestra en las Artes Arcanas", "Sabia del Bosque", "Comandante de la Orden", "Maestra de las Tempestades", "Exploradora Legendaria", "Reina de las Bestias", "Alquimista Famosa", "Vidente de las Estrellas", "Bardo del Reino", "Ingeniera Maestra", "Maestra Asesina", "Maestra de la Espada", "Anciana del Templo", "Guardiana de las Runas", "Sabia del Bosque", "Caballera de la Justicia", "Inquisidora Valiente", "Nigromante Poderosa", "Sacerdotisa de la Luz"]
tipos_crianza_neutros = ["Maestre en las Artes Arcanas", "Sabie del Bosque", "Comandante de la Orden", "Maestre de las Tempestades", "Exploradore Legendario", "Monarque de las Bestias", "Alquimiste Famose", "Vidente de las Estrellas", "Bardo del Reino", "Ingeniere Maestre", "Maestre Asesine", "Maestre de la Espada", "Anciane del Templo", "Guardiane de las Runas", "Sabie del Bosque", "Caballere de la Justicia", "Inquisidore Valiente", "Nigromante Poderose", "Sacerdote de la Luz"]

# Function to display formatted Markdown text
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Configurar la API key de Gemini (reemplazar con tu clave de API de Gemini)
genai.configure(api_key='your_google_API_key')

# Streamlit app
def main():
    st.set_page_config(page_title="Generador de Personajes de Fantasía con Gemini", page_icon="👹")
    st.title("Generador de Personajes de Fantasía con Gemini")

    # Función para generar un nombre aleatorio
    def generar_nombre():
        genero = random.choice(["masculino", "femenino", "neutro"])
        if genero == "masculino":
            return random.choice(nombres_masculinos)
        elif genero == "femenino":
            return random.choice(nombres_femeninos)
        else:
            return random.choice(nombres_neutros)

    # Función para generar un apellido aleatorio
    def generar_apellido():
        return random.choice(apellidos_epicos)

    # Función para generar una profesión aleatoria
    def generar_profesion():
        return random.choice(profesiones_fantasticas)

    # Función para generar un lugar mágico aleatorio
    def generar_lugar_magico():
        genero = random.choice(["masculino", "femenino", "neutro"])
        if genero == "masculino":
            return random.choice(lugares_magicos_masculinos)
        elif genero == "femenino":
            return random.choice(lugares_magicos_femeninos)
        else:
            return random.choice(lugares_magicos_neutros)

    # Función para generar un trasfondo de infancia aleatorio
    def generar_transfondo_infancia():
        genero = random.choice(["masculino", "femenino", "neutro"])
        if genero == "masculino":
            return random.choice(transfondos_infancia_masculinos)
        elif genero == "femenino":
            return random.choice(transfondos_infancia_femeninos)
        else:
            return random.choice(transfondos_infancia_neutros)

    # Función para generar un tipo de crianza aleatorio
    def generar_tipo_crianza():
        genero = random.choice(["masculino", "femenino", "neutro"])
        if genero == "masculino":
            return random.choice(tipos_crianza_masculinos)
        elif genero == "femenino":
            return random.choice(tipos_crianza_femeninos)
        else:
            return random.choice(tipos_crianza_neutros)

    # Función para obtener una respuesta del modelo Gemini
    def obtener_respuesta(prompt, chat):
        response = chat.send_message(prompt, stream=True)
        return response

    # Función para generar la historia adicional de un personaje
    def generar_historia_adicional(nombre, profesion, lugar_magico, transfondo_infancia, tipo_crianza):
        prompt = f"Escribe una historia sobre {nombre}, el {profesion}, nacido en {lugar_magico}, quien tuvo un pasado como {transfondo_infancia} y fue criado por un {tipo_crianza}."
        response = obtener_respuesta(prompt, chat)
        historia_adicional = ""
        for chunk in response:
            historia_adicional += chunk.text
        return historia_adicional

    # Inicializar la sesión de chat con Gemini
    select_model = "gemini-pro"
    chat = genai.GenerativeModel(select_model).start_chat(history=[])

    # Función para generar la historia completa de un personaje
    def generar_historia_personaje():
        nombre = generar_nombre()
        apellido = generar_apellido()
        profesion = generar_profesion()
        lugar_magico = generar_lugar_magico()
        transfondo_infancia = generar_transfondo_infancia()
        tipo_crianza = generar_tipo_crianza()

        historia = f"Nombre: {nombre} {apellido}\n"
        historia += f"Profesión: {profesion}\n"
        historia += f"Lugar Mágico de Origen: {lugar_magico}\n"
        historia += f"Transfondo de la Infancia: {transfondo_infancia}\n"
        historia += f"Tipo de Crianza: {tipo_crianza}\n"

        historia_adicional = generar_historia_adicional(nombre, profesion, lugar_magico, transfondo_infancia, tipo_crianza)

        historia += f"Historia Adicional:\n{historia_adicional}\n"

        return historia

    # Streamlit UI
    st.sidebar.title("Configuración de Gemini")
    st.sidebar.write("Selecciona el modelo de Gemini:")
    select_model = st.sidebar.selectbox("Modelo", ["gemini-pro"])

    # Botón para generar un nuevo personaje
    if st.button("Generar Personaje"):
        with st.spinner("Generando Personaje..."):
            historia = generar_historia_personaje()
        st.write(historia)

    # Función para descargar la historia generada como archivo de texto
    def descargar_archivo(historia, filename):
        b64 = base64.b64encode(historia.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Descargar {filename}</a>'
        return href

    # Botón para descargar la historia generada
    if "historia" in locals():
        st.markdown(descargar_archivo(historia, "personaje_de_fantasia.txt"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
