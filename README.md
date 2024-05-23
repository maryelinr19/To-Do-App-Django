# Aplicación de Lista de Tareas
Esta es una aplicación web completa de lista de tareas desarrollada utilizando Django para el backend y Django Templates para el frontend.

# Características:

Permite a los usuarios crear, visualizar, editar y eliminar tareas.

Implementa un sistema de autenticación de usuarios, donde cada usuario solo tiene acceso a sus propias tareas.

Utiliza Django Admin para administrar los modelos de datos, especialmente el modelo Task.

Implementa validaciones de datos y medidas de seguridad básicas, como la protección contra CSRF en formularios.

# Requisitos:

Python 3.x

Django 3.x o superior

# Instalación:

1.- Clona el repositorio:

git clone https://github.com/maryelinr19/To-Do-App-Django.git

2.- Navega al directorio del proyecto:

cd lista-de-tareas

3.- Crea y activa un entorno virtual:

python -m venv env
env\Scripts\activate.bat

4.- Instala las dependencias:

pip install -r requirements.txt

5.- Aplica las migraciones:

python manage.py migrate

6.- Crea un superusuario:

python manage.py createsuperuser

7.- Inicia el servidor de desarrollo:

python manage.py runserver

# Ejecución

Inicia el servidor de desarrollo:

python manage.py runserver
Accede a la aplicación en http://127.0.0.1:8000/.

Utiliza las credenciales del superusuario creado anteriormente para acceder al panel de administración en http://127.0.0.1:8000/admin/.

# Contribución
Si encuentras algún problema o tienes sugerencias para mejorar la aplicación, no dudes en abrir un issue o enviar un pull request.

# Licencia
Este proyecto está bajo la Licencia MIT.


 
