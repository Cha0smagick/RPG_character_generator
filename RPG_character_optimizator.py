import time
import codecs
from gpt4free import you

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
archivo_txt = input("Por favor, ingresa la ruta del archivo .txt: ")

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
