import subprocess

comandos = [
    "python -m venv env",
    ".\\env\\Scripts\\activate",
    "python -m pip install -r FIFAclone/requirements.txt",
    "npm install",
    "python .\FIFAclone\manage.py collectstatic"
]

for comando in comandos:
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    if resultado.returncode == 0:
        print("La ejecución del comando fue exitosa.")
        print("Salida del comando:")
        print(resultado.stdout)
    else:
        print("Hubo un error al ejecutar el comando.")
        print("Error:", resultado.stderr)
