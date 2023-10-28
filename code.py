import math as mt
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

def calcular_moda (Type):
    frecuencia = {}
    for valores in Type:
        if valores in frecuencia:
            frecuencia[valores] += 1
        else:
            frecuencia[valores] = 1

    moda = []
    max_frecuencia = max(frecuencia.values())
    for valor, freq in frecuencia.items():
        if freq == max_frecuencia:
            moda.append(valores)
    return moda

def var(RV, prom):
    rsl = 0
    for v in RV:
        a = (v - prom)**2
        rsl += a
    return rsl/len(RV)


def mediana (vals):
    """
    Calcula la mediana de los datos de una lista de números.

    Parámetros
    ----------
    vals: lista
    » Lista con números.
    lista = lista
    » Lista de datos ordenados.
    largo = float
    » Cantidad de datos en la lista.

    Retorna
    ---------
    mediana: float
    » Calcula la mediana de los datos.
    """

    lista = sorted(vals)
    largo = len(vals)

    if largo % 2 == 1:
        mediana = lista[largo // 2]
    else:
        centro1 = lista[largo // 2 - 1]
        centro2 = lista[largo // 2]
        mediana = (centro1 + centro2) / 2

    return mediana



def promedio(RV):
    """
    """
    return sum(RV) / len(RV)
    resultado = promedio(RV)
    print(resultado)

def mediana(RV):
    """
    """
    n = len(RV)

    if n % 2 != 0:
        return RV[n // 2]
    else:
        mid1 = RV[(n - 1) // 2]
        mid2 = RV[n // 2]
        return (mid1 + mid2) / 2

        result = mediana(RV)
        print(result)

def perce(RV):
    """
    """
    am = len(RV)

    if am % 4 == 0:
        p25 = (RV[am // 4 - 1] + RV[am // 4]) / 2
        p75 = (RV[3 * am // 4 - 1] + RV[3 * am // 4]) / 2
    else:
        p25 = RV[(am + 1) // 4 - 1]
        p75 = RV[3 * (am + 1) // 4 - 1]

    print(p25)
    print(p75)

def rango(vrad1):
    rango = max(vrad1) - min(vrad1)
    return rango


def mediana (vrad1):
    """
    Calcula la mediana de los datos de una lista de números.

    Parámetros
    ----------
    vals: lista
    » Lista con números.
    lista = lista
    » Lista de datos ordenados.
    largo = float
    » Cantidad de datos en la lista.

    Retorna
    ---------
    mediana: float
    » Calcula la mediana de los datos.
    """

    lista = sorted(vrad1)
    largo = len(vrad1)

    if largo % 2 == 1:
        mediana = lista[largo // 2]
    else:
        centro1 = lista[largo // 2 - 1]
        centro2 = lista[largo // 2]
        mediana = (centro1 + centro2) / 2

    return mediana

def varianza (vrad1):
    """
    Calcula la varianza.

    Parámetros
    ----------
    vals: lista
    » Lista con números de la cual se calculará la varianza.

    Retorna
    ---------
    Var: float
    » Valor de punto flotante donde se muestra la varianza.

    Variables
    ----------
    suma: variable
    » sumatoria de la resta entre un valor y la suma de todos los datos, dividido
    en la cantidad de datos y todo esto elevado al cuadrado.
    """
    suma = sum((x - (sum(vrad1) / len(vrad1)))**2 for x in vrad1)
    var = suma/len(vrad1)
    return var

def desviacion (vrad1):
    """
    Calcula la desviación estándar de los datos.

    Parámetros
    ----------
    vals: lista
    » Lista con números.

    Retorna
    ---------
    desv: float
    » La raíz de la varianza.
    """
    desv = sqrt(varianza(vrad1))
    return desv

archivo = open("cumulo_de_Virgo.dat", "r")
for _ in range(1):
    archivo.readline()

Type = []
Size = []
radial_velocities = []
for lin in archivo:
    palabras = lin.split()

    if len(palabras) >= 9:
        tipo = palabras[6]
        tamaño = palabras[8]
        rv = palabras[9]
        Type.append(tipo)
        Size.append(tamaño)
        radial_velocities.append(rv)
archivo.close()

mmd = calcular_moda(Type)
strm = str(mmd)
print(f"La moda del tipo de galaxias en el cúmulo de Virgo es: {strm[2:4]}")

# ------------- #

tipos = list(set(Type))
conteo = [Type.count(tipo) for tipo in tipos]

plt.figure(figsize=(10, 6))

# Gráfico de barras de frecuencia absoluta
plt.bar(tipos, conteo)

# Configuración del gráfico
plt.title("Tipos de galaxias")
plt.xlabel("Tipo de Galaxia")
plt.ylabel("Frecuencia")
plt.xticks(rotation = 33)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()

# Calcular el porcentaje
total = sum(conteo)
porcentaje = [(count / total) * 100 for count in conteo]

plt.figure(figsize=(10, 6))  # Ajusta las dimensiones del gráfico

# Gráfico de barras de porcentaje
plt.bar(tipos, porcentaje)

# Configuración del gráfico
plt.title("Tipos de galaxias")
plt.xlabel("Tipo de Galaxia")
plt.ylabel("Porcentaje (%)")
plt.xticks(rotation = 33)  # Rotar las etiquetas del eje X para mayor legibilidad
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar marcas en el eje vertical

# Mostrar el gráfico
plt.show()

# ----------- #

# Calcular frecuencia absoluta y tipos de galaxias
tipos = list(set(Type))
conteo = [Type.count(tipo) for tipo in tipos]

fig = plt.figure(figsize=(7, 18))
ax1 = fig.add_subplot(111)

ax1.pie(conteo, labels=tipos)
plt.title("Distintos tipos de Galaxias")

plt.show()

# --------- #

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

cdv = 'cumulo_de_Virgo.dat'
RV = []
with open(cdv, "r", encoding="utf-8") as archv:
    for l in range(4):
        archv.readline()

    for lin in archv:
        cudevi = lin.split()
        RV.append(float(cudevi[9]))

n = len(RV)
for i in range(n):
    for j in range(0, n - i - 1):
        if RV[j] > RV[j + 1]:
            RV[j], RV[j + 1] = RV[j + 1], RV[j]

n = len(RV)
c1 = n // 4
c3 = 3 * n // 4
q1 = (RV[c1] + RV[c1 - 1]) / 2
q3 = (RV[c3] + RV[c3 - 1]) / 2
iqr = q3 - q1

fre_dia = 2 * iqr * (n ** (-1/3))


prom = sum(RV) / len(RV)
med = RV[n // 2]


varianza = var(RV, prom)
st_d = (varianza)**1/2

#Crear el histograma
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 2900)

bin_range = range(0, 2900, int(fre_dia))
ax.hist(RV, bins=int(fre_dia), color="orange", alpha=0.5)

# Dibujar líneas y agregar texto para las estadísticas
ax.axvline(prom, color='black', linestyle='solid', linewidth=3)
ax.text(prom + 10, min(ax.hist(RV, bins=50)[0], default=1),\
        f'Promedio = {int(prom)} km/s', color='black')

ax.axvline(med, color='red', linestyle='dashed', linewidth=3)
ax.text(med + 50, max(ax.hist(RV, bins=50)[0], default=1),\
        f'Mediana = {int(med)} km/s', color='red')

# Agregar estadísticas debajo del gráfico
ax.text(1600, 5, f'STD = {int(st_d)} km/s', color='red')
ax.axvline(prom - st_d, color='green', linestyle='dotted', linewidth=3)
ax.axvline(prom + st_d, color='green', linestyle='dotted', linewidth=3)
ax.text(1600, 10, f'RI = {int(iqr)} km/s', color='blue')
ax.axvline(q1, color='blue', linestyle='dotted', linewidth=3)
ax.axvline(q3, color='blue', linestyle='dotted', linewidth=3)

# Configuración del gráfico
ax.set_xlabel(r"V$_{helio}$ (km/s)", fontsize=10)
ax.set_ylabel("N", fontsize=10)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

plt.show()

# ------------ #

# Nueva versión
omc = 'omegaCen.dat'

ORV = []
K = []
M_H = []

with open(omc, "r", encoding="utf-8") as archv:

    for l in range(1):
        archv.readline()

    for lin in archv:

        k = lin.split()[7]
        vh = lin.split()[8]
        mh = lin.split()[9]

        if k != '""' and k != 'nan':
            K.append(float(k))

        if vh != '""' and vh != 'nan':
            ORV.append(float(vh))

        if mh != '""' and mh != 'nan':
            M_H.append(float(mh))

ORV.sort()

def promedio(ORV):
    """
    """
    return sum(ORV)/len(ORV)

resultado = promedio(ORV)
print(f'Promedio: {resultado:.2f}')

def mediana(ORV):
    """
    """
    n = len(ORV)


    if n % 2 != 0:
        return ORV[n // 2]
    else:
        mid1 = ORV[(n - 1) // 2]
        mid2 = ORV[n // 2]
        return (mid1 + mid2) / 2

result = mediana(ORV)
print(f'Mediana: {result:.2f}')

def perce(ORV):
    """
    """
    am = len(ORV)

    if am % 4 == 0:
        p25 = (ORV[am // 4 - 1] + ORV[am // 4]) / 2
        p75 = (ORV[3 * am // 4 - 1] + ORV[3 * am // 4]) / 2
    else:
        p25 = ORV[(am + 1) // 4 - 1]
        p75 = ORV[3 * (am + 1) // 4 - 1]

    print(f'Primer cuartil: {p25:.2f}')
    print(f'Tercer cuartil: {p75:.2f}')

perce(ORV)

# -------------- #

def rango(ORV):
    rango = max(ORV) - min(ORV)
    return rango

ran = rango(ORV)
print("El rango de los datos es: ", ran)
print("El dato maximo es: ", max(ORV))
print("El dato minimo es: ", min(ORV))

def varianza(ORV):
    suma = sum((x - (sum(ORV) / len(ORV)))**2 for x in ORV)
    varianza = suma/len(ORV)
    return varianza

vari = varianza(ORV)
var = round(vari, 1)
print("La varianza de los datos es: ", var)

def desviacion(ORV):
    desviacion = (var)**1/2
    return desviacion

devn = desviacion(ORV)
dev = round(devn, 1)
print("La desviacion estandar de los datos es: ", dev)

#Nuevas varianzas
varian = med - devn
varia = round(varian, 1)
print("La nueva varianza es: ", varia)

varian2 = med + devn
varia2 = round(varian2, 1)
print("La nueva varianza es: ", varia2)

#Definir los valores mínimos y máximos
val_min = -150
val_max = 350

#Definir el tamaño de los bines
bin_size = 10

#Crear una lista de bines usando bucles
bins = []
cu_bin = val_min

while cu_bin <= val_max:
    bins.append(cu_bin)
    cu_bin += bin_size

#Crear el histograma
fig2 = plt.figure(figsize = (4.0, 3.0), tight_layout=True)
ax2 = fig2.add_subplot(111)

#Crear el gráfico de barras
ax2.set_xlim(-150, 350)
ax2.hist(ORV, bins=range(-150,350,10), color="red", alpha=0.5)
ax2.set_xlabel(r"V${rad}$ (km/h)", fontsize=13)
ax2.set_ylabel("N",fontsize=13)
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))

#Definimos el histograma
fig = plt.figure(figsize = (4.0, 3.0), tight_layout=True)
ax1 = fig.add_subplot(111)

#Crear el gráfico de barras
ax1.set_xlim(-150, 350)
ax1.hist(ORV, bins=range(-150,350,10), color="blue", alpha=0.7)
ax1.set_xlabel(r"V${rad}$ (km/h)", fontsize=13)
ax1.set_ylabel("N",fontsize=13)
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))

# --------------------- #

def Promedio(x):
    """
    Calcula el promedio (media aritmética) de una lista de datos.

    Args:
    - x (list): Una lista de datos numéricos.

    Returns:
    - float: El valor del promedio.

    El promedio se calcula como la suma de todos los datos dividida por el número de datos en la lista.
    """

    n = len(x)  # Obtiene la longitud de la lista de datos.
    suma = 0

    # Itera a través de los datos en la lista.
    for h in x:
        suma = suma + h  # Acumula la suma de todos los datos.

    prom = (suma / n)  # Calcula el promedio como la suma dividida por el número de datos.

    return prom  # Devuelve el valor del promedio (media aritmética).
def mediana(m):
    """
    Calcula la mediana de una lista de datos.

    Args:
    - m (list): Una lista de datos numéricos.

    Returns:
    - float: El valor de la mediana.

    La mediana se calcula de la siguiente manera:
    1. Se ordena la lista de datos en orden ascendente.
    2. Si la lista tiene un número impar de elementos, la mediana es el valor en el centro.
    3. Si la lista tiene un número par de elementos, la mediana es el promedio de los dos valores en el centro.
    """

    m.sort()  # Ordena la lista de datos en orden ascendente.

    if len(m) % 2 == 0:  # Comprueba si la lista tiene un número par de elementos.
        c = int(len(m) / 2) - 1
        j = m[c]  # Obtiene el valor en el centro (izquierda).
        h = m[c + 1]  # Obtiene el valor en el centro (derecha).
        med = (h - j) / 2  # Calcula la mediana como el promedio de los valores en el centro.

        if med == 0:  # Si la mediana calculada es 0, se toma el valor 'j' como mediana.
            med = j
    else:
        n = (len(m) - 1) / 2
        f = n + 1
        med = m[int(f - 1)]  # Calcula la mediana como el valor en el centro en caso de un número impar de elementos.

        if med == 0:  # Si la mediana calculada es 0, se toma el valor 'n' como mediana.
            med = n

    return med  # Devuelve el valor de la mediana.


archivo = open("omegaCen.dat", "r")
#for _ in range(1): #Nos saltamos la primera línea que no contiene información necesaria.
archivo.readline()

K = [] #brillo aparente
VHELIO_AVG = [] #velocidad radial
M_H = [] #metalicidad
for lin in archivo:
    palabras = lin.split()
    palabra = []

 #Verificamos la longitud de palabras para separar correctamente.
    if len(palabras) >= 14:
        try:
            a = float(palabras[7])

        except ValueError:
                a = 0
        try:
            b = float(palabras[8])

        except ValueError:
                b = 0
        try:c = float(palabras[13])

        except ValueError:
                c = 0
        brillo = a
        velradial = b
        meta = c
        K.append(brillo)
        VHELIO_AVG.append(velradial)
        M_H.append(meta)
archivo.close()

metal = []
for n in M_H:
    if n <=-0.7:
        metal.append(n)
velo = []
veloz = []
VEloz = []
Veloz = []

for n in VHELIO_AVG:
    if M_H[VHELIO_AVG.index(n)] in metal:
        velo.append(n)
for n in velo:
    d = str(n)
    veloz.append(d)
for n in veloz:
    t = n[n.index("."):]
    r = t[:2]
    g = n[0:n.index(".")] + r
    VEloz.append(g)
for n in VEloz:
    d = float(n)
    Veloz.append(d)
ene, bins, patches = plt.hist(Veloz, bins=range(185,300,3))
cuentas =list(ene)
list(bins)
#print(cuentas.index(max(cuentas)))
d = bins[15] - bins[16]
b = d/2
max(cuentas)
o = str(Promedio(Veloz))
m = mediana(Veloz)
g = o[:5]

fig = plt.figure(figsize = (6, 5),\
tight_layout=True)
ax1 = fig.add_subplot(111)
# Crear el gráfico de barras
ax1.set_xlim(185, 300)
ax1.hist(Veloz, bins=range(185,300,3),\
color="gray", alpha=0.7)
bins=range(185,300,3)
ax1.set_xlabel(r"V$_{Radial}$ (km/s)", fontsize=13)
ax1.set_ylabel("N",fontsize=13)
ax1.axvline(231.5, color = 'red', linestyle = 'dotted', linewidth=1.5)
ax1.axvline(231.7, color = 'blue', linestyle = 'dotted', linewidth=1.5)
ax1.axvline(233.1, color = 'green', linestyle = 'dotted', linewidth=1.5)
ax1.text(233.5, 214, f'Moda = {b}km/s', color='red')
ax1.text(233.5, 205, f'Promedio = {g}km/s', color='blue')
ax1.text(233.5, 195, f'Mediana = {m}km/s', color='green')
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
plt.show()

# ------------------------ #

import matplotlib.pyplot as plt
import math
n = len(K)
for i in range(n):
    for j in range(0, n - i - 1):
        if K[j] > K[j + 1]:
            K[j], K[j + 1] = K[j + 1], K[j]

# Regla de Sturges
n_sturges = int(1 + 3.322 * math.log10(len(K)))

# Regla de Scott
num = (max(K) - min(K))
div = 3.5 * (max(K) - min(K)) / (len(K) ** (1/3))
n_scott = int(num / div)

# Regla de Freeman & Diaconis
q1 = sorted(K)[int(len(K) * 0.25)]
q3 = sorted(K)[int(len(K) * 0.75)]
iqr = q3 - q1
n_fd = int((max(K) - min(K)) / (2 * iqr / (len(K) ** (1/3))))

# Asegurarse de que el número de bins sea al menos 1
n_sturges = max(n_sturges, 1)
n_scott = max(n_scott, 1)
n_fd = max(n_fd, 1)

# Crear los histogramas con los estilos "step" y etiquetarlos
plt.hist(K, bins=n_sturges, color='blue', label='Sturges', histtype='step')
plt.hist(K, bins=n_scott, color='green', label='Scott', histtype='step')
plt.hist(K, bins=n_fd, color='red', label='Freeman & Diaconis', histtype='step')

# Ajustar el rango Y del gráfico
plt.ylim(-20, 590)  # Ajusta los valores según tus preferencias

# Graficar un área sombreada para resaltar el rango intercuartílico
plt.fill_betweenx([0, 100], q1, q3, color='yellow', alpha=0.5, label='IQR')

# Agregar marcas menores en los ejes X e Y
plt.minorticks_on()
plt.grid(which='major', color='black', linestyle='-', linewidth=0.5)
plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)

# Agregar leyenda en la esquina superior izquierda
plt.legend(loc='upper left')

# Etiquetas y título
plt.xlabel('Magnitudes K')
plt.ylabel('Frecuencia')
plt.title('Histogramas de Magnitudes K')

# Mostrar el gráfico
plt.show()
