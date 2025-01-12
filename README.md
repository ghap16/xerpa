# GetXerpa Test

Este es un proyecto desarrollado con Django. A continuación, se describen los pasos para instalar y correr el proyecto localmente.

## Requisitos

Antes de empezar, asegúrate de tener lo siguiente instalado en tu máquina:

- [Python](https://www.python.org/downloads/) (recomendado: 3.11.5)
- [Pip](https://pip.pypa.io/en/stable/) (gestor de paquetes de Python)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (opcional, pero recomendado para gestionar entornos virtuales)
- [Git](https://git-scm.com/) (para clonar el repositorio)

## Instalación

Sigue los siguientes pasos para instalar el proyecto y ejecutarlo localmente:

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/ghap16/xerpa.git
cd xerpa

```

### 2. Crear un entorno virtual (opcional pero recomendado)

Es recomendable crear un entorno virtual para evitar conflictos con otras dependencias de Python que puedas tener instaladas en tu sistema. Si no tienes `virtualenv` instalado, puedes instalarlo con el siguiente comando:

```bash
pip install virtualenv
```

Ahora, crea un entorno virtual:

```bash
python -m venv env
```

Activa el entorno virtual:

-   En Windows:
    
    ```bash
    .\env\Scripts\activate
    ```
    
-   En macOS/Linux:
    
    ```bash
    source env/bin/activate
    ```
    

### 3. Instalar dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias para el proyecto usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Enviroment

Dentro del directorio, existe un archivo llamado `env_example`, hay que renombrar el archivo como `.env` y definir las variables si es necesario:


### 5. Configurar la base de datos

Para este proyecto se utilizo SQLite, solo asegúrate de que el archivo de la base de datos exista.

Si necesitas realizar migraciones a la base de datos, corre el siguiente comando:

```bash
python manage.py migrate
```

### 6. Crear un superusuario (opcional)

Si necesitas acceder al panel de administración de Django, puedes crear un superusuario con el siguiente comando:

```bash
python manage.py createsuperuser

```

Se te pedirá que ingreses un nombre de usuario, correo electrónico y una contraseña.

### 7. Correr el servidor de desarrollo

Una vez que hayas completado los pasos anteriores, ya puedes correr el servidor de desarrollo localmente:

```bash
python manage.py runserver
```

Esto iniciará el servidor en `http://127.0.0.1:8000/` (puedes cambiar el puerto si lo deseas).

### 8. Acceder al proyecto

Abre tu navegador y visita la URL `http://127.0.0.1:8000/` para ver el proyecto en funcionamiento. Si configuraste un superusuario, puedes acceder a la interfaz de administración en `http://127.0.0.1:8000/admin/`.

### 9. Swagger

Abre tu navegador y visita la URL `http://127.0.0.1:8000/api/swagger/` para ver la documentación en swagger

### 10. Test

Para correr los test ejecute el siguiente comando
 ```bash
    python manage.py test
```

### 10. Development

Cuando se trabaja en modo de desarrollo puede instalar opcional algunas librerias extra, principalmente para formatting
 ```bash
    pip install -r requirements_dev.txt
```
