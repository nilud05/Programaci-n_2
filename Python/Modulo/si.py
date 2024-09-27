import psycopg2

try:
    conectar = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = 'danitzha010912',
            host = 'localhost',
            port = '5432'
        )
    print("Conectado a PostgresSQL")
    cur = conectar.cursor()  #hasta aqui es para conectar la base de datos
    cur.execute("select * from usuarios") 
    for id, nombre, estrato, venta, mes in cur.fetchall():
                print(id,nombre, estrato, venta, mes) #esto es para consultar lo que yo deseo

    cur.close()

except Exception as e:
    print("Error de conexion a PostgreSQL", e)
    if conectar is not None:
        conectar.close()