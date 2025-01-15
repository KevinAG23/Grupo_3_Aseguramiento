import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=SistemaVentas;'
        'UID=sa;'
        'PWD=YourStrong!Passw0rd'
    )
    return connection