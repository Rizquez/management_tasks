# Management Tasks - Django and React + Vite

![img](images/img_2.jpg)
![img](images/img_1.jpg)

Este proyecto basado en la integracion de dos framework, es una aplicación web desarrollada para brindarle a los usuarios la posibilidad de realizar operaciones básicas sobre la gestión de tareas asi como un seguimiento sobre estas, pudiendo registrar, editar o eliminar tareas segun lo amerite.

> [!IMPORTANT]
Este proyecto es de caracter educativo y sirve para entender conceptos basicos relacionados a las REST API, asi como comenzar a realizar estudios sobre los Framework de Django, React y la aplicacion de SGBD en la integracion de una aplicaciones WEB. Se recomienda a quien vaya a usar este proyecto de estudio lease el fichero NOTE.txt ya que puede servir de ayuda.

## Tecnologías Utilizadas
1. Backend: Django.
2. Frontend: React + Vite.
3. Base de Datos: SQLite (no excluyente).

> [!NOTE]
Sera necesario la creación de una BBDD con su respectiva tabla. Se sugiere la seleccion de SQLite (aunque no es excluyente), pudiendo escoger cualquier otra BBDD relacional para el uso de este proyecto.

## Estructura del proyecto
```
├── .gitignore
├── LICENSE
├── NOTES.txt
├── README.md
├── db.sqlite3
├── manage.py
├── requirements.txt
├── tasks
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── images
│   ├── img_1.jpg
│   └── img_2.jpg
├── django_crud_api
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── client
    ├── public
    │   └── vite.svg
    ├── src
    │   ├── api
    │   │   └── tasks.api.js
    │   ├── assets
    │   │   └── react.svg
    │   ├── components
    │   │   ├── Navigation.jsx
    │   │   ├── TaskCard.jsx
    │   │   └── TasksList.jsx
    │   ├── pages
    │   │   ├── TaskFormPage.jsx
    │   │   └── TasksPage.jsx
    │   ├── App.css
    │   ├── App.jsx
    │   ├── index.css
    │   └── main.jsx
    ├── .eslintrc.cjs
    ├── .gitignore
    ├── README.md
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── postcss.config.js
    ├── tailwind.config.js
    └── vite.config.js
```

## Creacion del entorno de virtual:
Se necesitara tener instalada previamente la libreria 'virtualenv', en caso contrario se podra instalar ejecutando el siguiente comando:
```
pip install virtualenv
```
Una vez instalada, para crear un entorno de desarrollo se debe ejecutar:
```
python -m virtualenv venv
```

> [!TIP]
Se recomienda la creación de un entorno virtual para optimizar el desarrollo y la ejecución del proyecto.

## Dependencias
Este comando instala las dependencias necesarias sobre este proyecto:
```
pip install -r requirements.txt
```
Y este comando crea o actualiza el archivo txt que almacena las dependencias del proyecto:
```
pip freeze > requirements.txt  
```

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un 'fork' del repositorio, crea una rama con tus mejoras y envía un 'pull request'.

## Licencia
Este proyecto está bajo una licencia MIT. Consulta el archivo LICENSE para más detalles.
