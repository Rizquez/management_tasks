# Management Tasks / Django CRUD + Bootstrap - (V.2)
Este proyecto es una aplicacion web desarrollada con Django y Bootstrap para practicar las operaciones `CRUD` (Crear, Leer, Actualizar, Eliminar) con autenticacion de usuario. Permite gestionar tareas dentro de un sistema que requiere que los usuarios inicien sesion para acceder a sus funcionalidades.

> [!NOTE]
> Esta segunda version del proyecto es refactorizada con la intencion de aplicar conceptos nuevos aprendidos sobre el framework de `Django`.

## Tecnologias Utilizadas
- **Django**: Framework de desarrollo web de alto nivel que fomenta el desarrollo rapido y el diseño limpio y pragmatico.
- **Bootstrap**: Framework de CSS para desarrollar componentes y diseños responsivos de forma rapida y eficiente.
- **SQLite**: Base de datos utilizada para el almacenamiento de datos (configurable a otras bases de datos).

## Estructura del proyecto
Descripcion de como esta organizado el proyecto:
```
├── djangocrud
│   ├── asgi.py 
│   ├── settings.py 
│   ├── urls.py 
│   └── wsgi.py 
├── tasks
│   ├── migrations/...
│   ├── templates/...
│   ├── admin.py 
│   ├── app.py 
│   ├── forms.py 
│   ├── models.py
│   ├── test.py 
│   └── views.py
├── .gitignore
├── LICENSE
├── README.md
├── db.sqlite3
├── manage.py
└── requierments.txt
```

## Creacion del entorno de virtual
Se necesitara tener instalada previamente la libreria `virtualenv`, en caso contrario se podra instalar ejecutando el siguiente comando:
```
pip install virtualenv
```
Una vez instalada, para crear un entorno de desarrollo se debe ejecutar:
```
python -m virtualenv venv
```
Y para activar el entorno virtual se debe ejecutar el comando:
```
venv\Scripts\activate
```

> [!TIP]
> Se recomienda la creacion de un entorno virtual para optimizar el desarrollo y la ejecucion del proyecto.

## Dependencias
Las dependencias de este proyecto se encuentran en el fichero `requirements.txt`, las cuales se instalan mediante la ejecucion del siguiente comando:
```
pip install -r requirements.txt
```

## Recursos adicionales
* [Django docs](https://docs.djangoproject.com/en/5.1/)
* [Bootstrap docs](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un `fork` del repositorio, crea una rama con tus mejoras y envia un `pull request`.

## Licencia
Este proyecto esta bajo una licencia `MIT`. Consulta el archivo `LICENSE` para mas detalles.
