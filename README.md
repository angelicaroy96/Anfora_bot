# Anfora_bot
Bot en consola desarrollado en Python y con MongoDB para guardar información relevante las respuestas que el usuario ingrese.

### Pre-requisitos 📋
crear entorno virtual en anaconda o con virtualenv con la versión 3.7 de python.

#### Anaconda 
```bash
conda create -n myenv python=3.4
```
#### Virtualenv
```bash
python -m venv tutorial-env
```

### Instalación  🔧
Activar entorno virtual.
#### Anaconda
```bash
activate myenv
```

#### Virtualenv 
El archivo se encuentra dentro de la carpeta Scrpits 
```bash
activate.bat
```
Ejecutar el siguiente comando para instalar las librerias despues de activar el entorno virtual.
```bash
pip install -r requirements.txt
```

### Despligue del programa 📦
Entrar a la ruta /bot_anfora ejecutar el comando 
```bash
python main.py
```
A continuación se inicara la ejecucción del programa.
![image](https://user-images.githubusercontent.com/59720195/137990213-3813110b-e147-4050-b2cd-906242129a41.png)

Abrir Mongo Compass para verifcar si se guardaron los datos introducidos.
![image](https://user-images.githubusercontent.com/59720195/137990967-3d3f35d9-6d93-4b32-9042-d55b6eaac0c4.png)

Como se puede observar los datos han sigo guardados con exito.
