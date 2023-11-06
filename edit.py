import pandas as pd

# Función para reducir el tamaño de un archivo CSV extrayendo las primeras X filas
def reducir_csv(archivo_original, archivo_reducido, num_filas):
    """
    Lee las primeras num_filas del archivo_original y las guarda en archivo_reducido.
    
    Parámetros:
    archivo_original (str): Ruta al archivo CSV original.
    archivo_reducido (str): Ruta para guardar el nuevo archivo CSV reducido.
    num_filas (int): Número de filas a extraer del archivo original.
    """
    # Leer las primeras X filas del archivo
    df = pd.read_csv(archivo_original, nrows=num_filas)
    
    # Guardar las filas leídas en un nuevo archivo CSV
    df.to_csv(archivo_reducido, index=False)
    print(f'Archivo reducido guardado en: {archivo_reducido}')

# Ejemplo de uso
archivo_original = 'Ratings.csv'
archivo_reducido = 'ShortRatings.csv'
num_filas = 1000  # Queremos las primeras 1000 filas

reducir_csv(archivo_original, archivo_reducido, num_filas)
