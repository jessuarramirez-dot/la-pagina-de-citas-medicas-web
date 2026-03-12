
from flask import Flask, render_template, request
from models.pacientes import registrar_paciente, consultar_paciente
from models.citas import reservar_cita, consultar_cita, actualizar_cita, consultar_cita_por_id

app = Flask(__name__)

# Editar cita
@app.route("/editar_cita/<int:id>")
def editar_cita(id):
    cita = consultar_cita_por_id(id)
    return render_template("editar_cita.html", cita=cita)

# Guardar cambios de cita
@app.route("/actualizar_cita", methods=["POST"])
def actualizar_cita_view():
    id_cita = request.form["id"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    tipo_cita = request.form["tipo_cita"]
    medico = request.form["medico"]
    actualizar_cita(id_cita, fecha, hora, tipo_cita, medico)
    return render_template("resultado_cita.html", mensaje="Cita actualizada correctamente")

app = Flask(__name__)

# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Registro de paciente
@app.route("/registro")
def registro():
    return render_template("registro_paciente.html")


@app.route("/guardar_paciente", methods=["POST"])
def guardar_paciente():

    documento = request.form["documento"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    eps = request.form["eps"]

    registrar_paciente(documento, nombre, apellido, telefono, correo, eps)

    return render_template("resultado_cita.html", mensaje="Paciente registrado correctamente")


# Consultar paciente
@app.route("/consultar")
def consultar():
    return render_template("consultar.html")


@app.route("/consultar_paciente", methods=["POST"])
def consultar_pac():

    documento = request.form["documento"]

    paciente = consultar_paciente(documento)

    return render_template("resultado_consulta.html", paciente=paciente)


# Reservar cita
@app.route("/reservar")
def reservar():
    return render_template("reservar_cita.html")


@app.route("/guardar_cita", methods=["POST"])
def guardar_cita():

    documento = request.form["documento"]
    medico = request.form["medico"]
    tipo_cita = request.form["tipo_cita"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    direccion_eps = request.form["direccion_eps"]

    reservar_cita(documento, medico, tipo_cita, fecha, hora, direccion_eps)

    return render_template("resultado_cita.html", mensaje="Cita reservada correctamente")


# Consultar cita
@app.route("/consultar_cita")
def consultar_cita_view():
    return render_template("consulta_cita.html")


@app.route("/buscar_cita", methods=["POST"])
def buscar_cita():

    documento = request.form["documento"]

    cita = consultar_cita(documento)

    return render_template("resultado_cita.html", mensaje=cita)


# Páginas informativas
@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/programas")
def programas():
    return render_template("programas.html")


@app.route("/sedes")
def sedes():
    return render_template("sedes.html")

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))