def consultar_cita_por_id(id_cita):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM citas WHERE id=%s"
    cursor.execute(sql, (id_cita,))
    cita = cursor.fetchone()
    conexion.close()
    return cita
def actualizar_cita(id_cita, fecha, hora, tipo_cita, medico):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
    UPDATE citas
    SET fecha=%s, hora=%s, tipo_cita=%s, medico=%s
    WHERE id=%s
    """
    valores = (fecha, hora, tipo_cita, medico, id_cita)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()
from database import conectar

def reservar_cita(documento,medico,tipo_cita,fecha,hora,direccion_eps):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """INSERT INTO citas
    (documento,medico,tipo_cita,fecha,hora,direccion_eps)
    VALUES(%s,%s,%s,%s,%s,%s)"""

    valores = (documento,medico,tipo_cita,fecha,hora,direccion_eps)

    cursor.execute(sql,valores)

    conexion.commit()
    conexion.close()

def consultar_cita(documento):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM citas WHERE documento=%s"
    cursor.execute(sql, (documento,))
    cita = cursor.fetchone()
    conexion.close()
    return cita