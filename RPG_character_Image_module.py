
import freeGPT
from PIL import Image
from io import BytesIO
from asyncio import run

async def main():
    while True:
        try:
            # Solicitar la ruta del archivo .txt al usuario
            txt_file_path = input("Por favor, ingresa la ruta del archivo .txt que contiene el prompt: ")
            
            # Leer el contenido del archivo .txt
            with open(txt_file_path, "r") as file:
                prompt = file.read()

            resp = await getattr(freeGPT, "prodia").Generation().create(prompt) #prodia, pollinations
            Image.open(BytesIO(resp)).show()
            print(f"🤖: Imagen mostrada.")
        except Exception as e:
            print(f"🤖: {e}")

if __name__ == "__main__":
    run(main())

Con este código, el programa solicitará al usuario que ingrese la ruta del archivo .txt que contiene el prompt. Luego, leerá el contenido del archivo y generará la imagen correspondiente. Asegúrate de tener el archivo .txt con el prompt en la ruta especificada antes de ejecutar el programa.
