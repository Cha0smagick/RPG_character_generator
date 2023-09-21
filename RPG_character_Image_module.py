async def main():
    try:
        # Solicitar la ruta del archivo .txt al usuario
        txt_file_path = input("Por favor, ingresa la ruta del archivo .txt que contiene el prompt: ")

        # Leer el contenido del archivo .txt
        with open(txt_file_path, "r") as file:
            prompt = file.read()

        output_folder = os.path.dirname(os.path.abspath(txt_file_path))  # Obtiene la carpeta del archivo .txt

        for i in range(5):
            resp = await getattr(freeGPT, "prodia").Generation().create(prompt) #prodia, pollinations
            image = Image.open(BytesIO(resp))
            image.show()
            
            # Guardar la imagen en la carpeta de salida con un nombre único
            image.save(os.path.join(output_folder, f"imagen_{i}.png"))
            
            print(f"🤖: Imagen {i + 1} mostrada y guardada en la carpeta de salida.")

    except Exception as e:
        print(f"🤖: {e}")

if __name__ == "__main__":
    run(main())
