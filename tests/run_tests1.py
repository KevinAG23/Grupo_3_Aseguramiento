# from behave.__main__ import main as behave_main

# if __name__ == "__main__":
#     behave_main("tests/features")



from behave.__main__ import main as behave_main
import os

if __name__ == "__main__":
    # Ruta de los features y del archivo JSON de salida
    features_path = "tests/features1"
    report_file = "report1.json"

    # Ejecutar behave con opciones para generar el reporte JSON
    status = behave_main(f"{features_path} --format json --outfile {report_file}")

    # Verificar si el archivo de reporte fue generado
    if os.path.exists(report_file):
        print(f"El reporte JSON se ha generado correctamente en: {report_file}")
    else:
        print("Hubo un problema al generar el reporte JSON.")

    # Retornar el estado de salida de las pruebas
    exit(status)
