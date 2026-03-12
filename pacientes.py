from database import conectar

def registrar_paciente(documento,nombre,apellido,telefono,correo,eps):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """INSERT INTO pacientes
    (documento,nombre,apellido,telefono,correo,eps)
    VALUES(%s,%s,%s,%s,%s,%s)"""

    valores = (documento,nombre,apellido,telefono,correo,eps)

    cursor.execute(sql,valores)

    conexion.commit()
    conexion.close()


def consultar_paciente(documento):

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    sql = "SELECT * FROM pacientes WHERE documento=%s"
    cursor.execute(sql,(documento,))

    paciente = cursor.fetchone()

    conexion.close()

    return paciente