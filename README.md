# Proyecto de Venta de Electrodomésticos Usados

Este proyecto es una aplicación web desarrollada con Django para la venta de electrodomésticos usados. A continuación se describen los componentes principales del proyecto.

## Estructura del Proyecto

```
electrodomesticos_usados/
├── manage.py               # Script de gestión de Django
├── electrodomesticos_usados/
│   ├── __init__.py        # Indica que este directorio es un paquete de Python
│   ├── settings.py        # Configuración del proyecto Django
│   ├── urls.py            # Rutas URL del proyecto
│   ├── asgi.py            # Configuración para el servidor ASGI
│   └── wsgi.py            # Configuración para el servidor WSGI
├── tienda/
│   ├── __init__.py        # Indica que este directorio es un paquete de Python
│   ├── admin.py           # Registro de modelos en el panel de administración
│   ├── apps.py            # Configuración de la aplicación "tienda"
│   ├── models.py          # Definición de modelos de datos
│   ├── tests.py           # Pruebas automatizadas para la aplicación
│   ├── views.py           # Lógica de negocio y manejo de modelos
│   ├── urls.py            # Rutas URL específicas de la aplicación
│   └── migrations/
│       └── __init__.py    # Paquete para almacenar migraciones de la base de datos
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Instalación

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias utilizando el archivo `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
4. Realiza las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```
5. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

## Uso

Accede a la aplicación en tu navegador web en `http://127.0.0.1:8000/`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.