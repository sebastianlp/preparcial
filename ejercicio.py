# Ingreso de datos
def ingresarDatos():
    lotes = []
    creaLote = input('Crear un lote ("n" para salir):')
    while creaLote != 'n':
        lote = []
        numero = input('Ingrese un numero ("n" para salir de la carga de numeros):')
        while numero != 'n':
            lote.append(int(numero))
            numero = input('Ingrese un numero ("n" para salir de la carga de numeros):')
        lotes.append(lote)
        creaLote = input('Crear un lote ("n" para salir):')
    return lotes

def calcularPromedios(lotes):
    promedios = []
    index = 0
    for l in lotes:
        index += 1
        acum = 0
        for n in l:
            acum += int(n)
        promedios.append({'Promedio': acum/len(l), 'Lote': index})
    return promedios

def calcularPromedioMinimo(promedios):
    minTestigo = promedios[0]['Promedio']
    lote = 0
    for i, p in enumerate(promedios):
        if p['Promedio'] < minTestigo:
            minTestigo = p['Promedio']
            lote = i + 1
    return {'Promedio': minTestigo, 'Lote': lote}

def calcularValorMaximo(lotes):
    maxDato = 0
    index = 0
    for l in lotes:
        index += 1
        acum = 0
        for i, n in enumerate(l):
            if n > maxDato:
                maxDato = n
                lote = index
    return {'Maximo': maxDato, 'Lote': lote}

lotes = ingresarDatos() #comentar esta linea y descomentar la de abajo para probar sin tener que ingresar lotes manualmente
# lotes = [[1, 2, 3], [4, 2, 10], [1000, 1, 1]] descomentar esta linea y comentar la de arriba para probar sin tener que ingresar lotes manualmente
if (len(lotes)) == 0:
    print('No hay lotes creados. No hago nada.')
else:
    promedios = calcularPromedios(lotes)
    print(promedios)
    promedioMinimo = calcularPromedioMinimo(promedios)
    print(promedioMinimo)
    valorMaximo = calcularValorMaximo(lotes)
    print(valorMaximo)
