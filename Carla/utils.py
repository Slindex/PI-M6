import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def verificar_tipo_datos(df):
    '''
    Verifica el tipo de dato contenido en cada columna de un dataframe.
    Tiene como parámetro el dataframe a evaluar y devuelve un resumen de el/los tipos de datos, 
    porcentaje de nulos y no nulos y cantidad de nulos por cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "nulos_%": [], "nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict["nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def boxplot(df, columna):
    '''
    Realiza un boxplot sencillo para una columna determinada.
    '''
    plt.figure(figsize=(15, 2))
    sns.boxplot(data=df, x=df[columna])
    plt.title(f'Boxplot de la columna {columna}')
    plt.show()

def histplot(df, columna, bins=None):
    '''
    Realiza un histplot sencillo para una columna determinada.
    '''
    plt.figure(figsize=(5, 3))
    if bins is None:
        sns.histplot(data=df, x=df[columna])
    else:
        sns.histplot(data=df, x=df[columna], bins=bins)
    plt.title(f'Boxplot de la columna {columna}')
    plt.xticks(range(min(df[columna]), max(df[columna]) + 1, 1))

    plt.show()

def countplot(df, columna):
    '''
    Realiza un countplot sencillo para una columna determinada.
    '''
    plt.figure(figsize=(14, 3))

    sns.countplot(data=df, y=df[columna])

    plt.title(f'Countplot de la columna {columna}')

    # Ajusta los espacios entre subplots y muestra
    plt.tight_layout()
    plt.show()
    
def pairplot(df, hue):
    sns.pairplot(df, hue=hue, diag_kind="hist", palette=['red', 'green'])
    plt.show()

def tabla_contingencias(df, var_objetivo):
    '''
    Muestra la relación de variables categóricas de un dataframe en relación a una variable objetivo
    '''
    df_categ = df.select_dtypes(exclude=['int', 'float'])
    columnas_to_compare = [col for col in df_categ.columns if col != var_objetivo]

    # Crea y muestra tablas de contingencia y mapas de calor para cada variable categórica
    for columna in columnas_to_compare:
        contingency_table = pd.crosstab(index=df_categ[columna], columns=df_categ[var_objetivo])
        plt.figure(figsize=(5, 4))
        sns.heatmap(contingency_table, annot=True, cmap='YlGnBu', fmt='d')
        plt.title(f'Mapa de Calor de Contingencia - {columna} vs {var_objetivo}')
        plt.show()

def bigote_max(columna):
    '''
    Calcula el valor del bigote máximo y la cantidad de valores que se encuentran como valores atípicos.
    '''
    # Cuartiles
    q1 = columna.describe()[4]
    q3 = columna.describe()[6]

    # Valor del vigote
    bigote_max = round(q3 + 1.5*(q3 - q1), 2)
    print('El bigote superior se ubica en:', bigote_max)

    # Cantidad de atípicos
    print('Hay', (columna > bigote_max).sum(), 'valores atípicos.')
    
def valor_mas_frecuente(df, columna):
    '''
    Calcula el valore mas frecuente en una columna, su cantidad y porcentaje respecto del total.
    '''
    # Frecuencias
    moda = df[columna].mode()[0]
    # Cantidad de la mayor frecuencia
    cantidad = (df[columna] == moda).sum()
    # Total de registros
    total = df[columna].count()
    # Porcentaje de la mayor frecuencia
    porcentaje = round(cantidad/total * 100,2)
    print(f'Valor mas frecuente es {moda}, con una cantidad de {cantidad} y representa el {porcentaje}%.')
    
def resumen_categoricas(df, columna):
    '''
    Resume una columna categóricas de un dataframe indicando la cantidad por categoría y su porcentaje.
    '''
    porcentajes = round(((df[columna].value_counts() / len(df)) * 100), 2)
    cantidades = df[columna].value_counts()

    resultados_df = pd.DataFrame({
        'Porcentaje': porcentajes,
        'Cantidad': cantidades
    })

    # Imprime el DataFrame resultante
    print(resultados_df)

def resumen_binarias(df):
    '''
    Resume las variables binarias de un dataframe indicando la cantidad y porcentaje de cada una.
    '''
    datos_resumen = []
    for columna in df.columns:
        valores_unicos = df[columna].unique()
        if "SI" in valores_unicos and "NO" in valores_unicos:
            porcentaje_si = round((df[columna] == "SI").sum() / len(df) * 100,2)
            total_si = (df[columna] == "SI").sum()
            porcentaje_no = round(100 - porcentaje_si, 2)
            total_no = (df[columna] == "NO").sum()
            datos_resumen.append({
                'Columna': columna,
                'Porcentaje de Si': porcentaje_si,
                'Cantidad de Si': total_si,
                'Porcentaje de No': porcentaje_no,
                'Cantidad de No': total_no
            })

    # Se crea un DataFrame de resumen
    df_resumen = pd.DataFrame(datos_resumen)
    return df_resumen

