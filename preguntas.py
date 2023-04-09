"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    a = data.shape[0]
    return a

    return


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    a = data.shape[1]
    return a


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """

    data = pd.read_csv('tbl0.tsv', sep='\t')
    a = data.groupby(by="_c1")["_c0"].count()
    return a


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    b = data.groupby(by="_c1")["_c2"].mean()
    return b


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    b = data.groupby(by="_c1")["_c2"].max()
    return b




def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    data = pd.read_csv('tbl1.tsv', sep='\t')
    d = sorted(list(set(data['_c4'].str.upper())))
    return d


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    e = (data.groupby(by="_c1")["_c2"].sum())
    return e 


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    data = pd.read_csv('tbl0.tsv', sep='\t')
    data1 = data.assign(suma = data['_c0'] + data['_c2'])
    return data1

def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """

    data = pd.read_csv('tbl0.tsv', sep='\t')

    fecha = data["_c3"]
    ini = 0 #posición inicial de la subcadena
    fin = 4 #posición final de la subcadena (excluida)
    anho =[] 
    for row in fecha:
        anho.append(row[ini:fin])

    data1 = data.assign(year = pd.DataFrame(anho, columns = ['year']))

    return data1


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    data = pd.read_csv('tbl0.tsv', sep='\t')
    data.sort_values(by=['_c1','_c2'],inplace=True)
    data._c2=data._c2.astype(str)
    tb=data.groupby(['_c1'])['_c2'].apply(':'.join).reset_index()
    tb.set_index('_c1',inplace=True)
    return tb


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    data = pd.read_csv('tbl1.tsv', sep='\t')
    dfaux = data.groupby('_c0')['_c4'].apply(list)
    df1 = pd.DataFrame()
    df1['_c0'] = dfaux.keys()
    df1['_c4'] = [elem for elem in dfaux]
    df1['_c4'] = [','.join(str(v) for v in sorted(elem)) for elem in df1['_c4']]
    
    return df1


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """

    df = pd.read_csv('tbl2.tsv', sep='\t', header=0)
    df['_c5'] = df["_c5a"] + ":" + df["_c5b"].map(str)
    serie = df.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(map(str, x))))
    df2 = pd.DataFrame(serie)
    df2.reset_index(inplace=True)
    return df2


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    df1 = pd.read_csv('tbl0.tsv', sep='\t', header=0)
    df2 = pd.read_csv('tbl2.tsv', sep='\t', header=0)

    df3 = pd.merge(df1, df2, on='_c0')
    df4 = df3.groupby('_c1')['_c5b'].sum()
    return df4
