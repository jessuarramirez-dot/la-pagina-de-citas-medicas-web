# Sistema de Gestión de Citas EPS

**eps_citas_app**

## Descripción

Este proyecto es una aplicación web desarrollada en Python utilizando Flask, orientada a la gestión de citas médicas en una entidad tipo EPS. Permite registrar pacientes, programar citas, consultar información y administrar datos de manera organizada.

El sistema incluye una interfaz web dinámica basada en plantillas HTML, así como una estructura modular para el manejo de base de datos y lógica del negocio.

---

## Características principales

* Registro de pacientes
* Programación de citas médicas
* Consulta de citas registradas
* Edición de citas existentes
* Interfaz web con navegación estructurada
* Arquitectura modular (modelos, base de datos, vistas)

---

## Tecnologías utilizadas

* Python
* Flask
* HTML5
* CSS3
* Jinja2 (plantillas)
* SQLite / Base de datos (según configuración)

---

## Estructura del proyecto

```
eps_citas_app/
│
├── app.py                 # Archivo principal (Flask)
├── database.py            # Conexión a base de datos
├── confi.py               # Configuración general
├── requirements.txt       # Dependencias
│
├── models/                # Modelos de datos
│   ├── pacientes.py
│   └── citas.py
│
├── templates/             # Vistas HTML
│   ├── index.html
│   ├── registro_paciente.html
│   ├── reservar_cita.html
│   ├── consulta_cita.html
│   └── ...
│
├── static/                # Archivos estáticos
│   ├── css/
│   └── img/
│
└── Procfile               # Configuración para despliegue
```

---

## Requisitos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

* Python 3.8 o superior
* pip (gestor de paquetes)

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

2. Acceder al proyecto:

```bash
cd eps_citas_app
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar el archivo principal:

```bash
python app.py
```

Luego abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## Uso del sistema

1. Acceder a la página principal
2. Registrar un paciente
3. Programar una cita médica
4. Consultar o editar citas existentes
5. Navegar entre las diferentes secciones del sistema

---

## Configuración de base de datos

La conexión se encuentra definida en:

```
database.py
```

Dependiendo de la configuración, se puede utilizar SQLite u otro motor de base de datos.

---

## Problemas comunes

* **La aplicación no inicia:**
  Verificar que Python esté instalado correctamente

* **Error de dependencias:**
  Ejecutar nuevamente `pip install -r requirements.txt`

* **No carga la página:**
  Asegurarse de ejecutar `app.py`

---

## Mejoras futuras

* Implementación de autenticación de usuarios
* Integración con base de datos más robusta (MySQL/PostgreSQL)
* Validaciones avanzadas en formularios
* Panel administrativo
* Despliegue en la nube

---

## Autor

Jessuar Ramírez

---

## Licencia

Proyecto desarrollado con fines académicos.
