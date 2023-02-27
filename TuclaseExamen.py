
class TuclaseExamen(): 
    
    '''
    define propiedades de clase 
    para utilizarlas en el metodo principla
    '''
    
    def arithmetic_arranger(lista, argumento = False):
        tamanoLista = len(lista)   
        primerosNumeros = [a.split()[0] for a in lista]
        operadores = [operador.split()[1] for operador in lista]
        segundosNumeros = [b.split()[2] for b in lista]
        longitudPrimerosNumeros = [len(str(longitud)) for longitud in primerosNumeros]
        longitudSegundosNumeros = [len(str(longitud)) for longitud in segundosNumeros]

        if (tamanoLista > 5):
            return "Error: Too many problems."
        
        def contarPrimerosDigitos():
            for digitos in longitudPrimerosNumeros:
                if digitos > 4:
                    return True
                
        def contarSegundosDigitos():
            for digitos in longitudSegundosNumeros:
                if digitos > 4:
                    return True
                        
        digitosPrimerosNumeros = contarPrimerosDigitos()
        digitosSegundosNumeros = contarSegundosDigitos()

        for problema in lista:
            # Verificar que si se encuentra un caracter que no es numerico a los primeros numeros que seran operando
            if not all([i.isnumeric() for i in primerosNumeros]):
                return 'Error: Numbers must only contain digits.'
            
            # Verificar que si se encuentra un caracter que no es numerico a los segundos numeros que seran operando
            elif not all([i.isnumeric() for i in segundosNumeros]):
                return 'Error: Numbers must only contain digits.'

            elif ('/' in problema):
                return "Error: Operator must be '+' or '-'."
                            
            elif ('*' in problema):
                return "Error: Operator must be '+' or '-'."

            elif (digitosPrimerosNumeros == True or digitosSegundosNumeros == True):
                return 'Error: Numbers cannot be more than four digits.'
            
            else:
                # Se guardaran al restar la-longitud de los primeros operadores menos la de los segundos operadores
                diferencias = []

                # Se agregan la cantidad de espacios que habra a la izquierda del primer operando
                diferencias2 = []

                # Se agregan la cantidad de espacios que habra a la izquierda del segundo operando
                diferencias3 = []

                # Lineas que contendran los operandos de manera horizontal
                primerLinea = []
                segundaLinea = []
                terceraLinea = []
                cuartaLinea = []
                resultados = []
                longitudLineasResultado = []
                espaciosCuartaLinea = []

                for problema in lista:
                    resultados.append(eval(problema))

                for elementos1, elementos2 in zip(longitudPrimerosNumeros, longitudSegundosNumeros):
                    diferencias.append(elementos1 - elementos2)

                for i in range(len(diferencias)):
                    if (diferencias[i] < 0):
                        diferencias2.insert(i, (abs(diferencias[i]) + 2))
                        diferencias3.insert(i, 1)
                    
                    elif (diferencias[i] == 0):
                        diferencias2.insert(i, 2)
                        diferencias3.insert(i, 1)

                    else:
                        diferencias2.insert(i, 2)
                        diferencias3.insert(i, ((diferencias[i]) + 1))

                longitudResultados = [len(str(longitud)) for longitud in resultados]
                
                for longitud1, longitud2 in zip(longitudPrimerosNumeros, diferencias2):
                    longitudLineasResultado.append(longitud1 + longitud2)

                for longitud1, longitud2 in zip(longitudLineasResultado, longitudResultados):
                    espaciosCuartaLinea.append(longitud1 - longitud2)

                for i in range(len(diferencias)):
                    primerLinea.insert(i, ((' ' * diferencias2[i]) + str(primerosNumeros[i]) + (' ' * 4)))
                    segundaLinea.insert(i, (operadores[i] + (' ' * diferencias3[i]) + str(segundosNumeros[i]) + (' ' * 4)))
                    terceraLinea.insert(i, (('-' * diferencias3[i]) + ('-' * longitudSegundosNumeros[i]) + '-' + (' ' * 4)))
                    cuartaLinea.insert(i, (' ' * espaciosCuartaLinea[i] + str(resultados[i]) + (' ' * 4)))

                primerLinea[(len(primerosNumeros)) - 1] = primerLinea[(len(primerosNumeros)) - 1].rstrip()
                segundaLinea[(len(segundosNumeros)) - 1] = segundaLinea[(len(segundosNumeros)) - 1].rstrip()
                terceraLinea[(len(diferencias3)) - 1] = terceraLinea[(len(diferencias3)) - 1].rstrip()
                cuartaLinea[(len(resultados)) - 1] = cuartaLinea[(len(resultados)) - 1].rstrip()

                # Lineas que muestran los problemas aritmeticos                
                resultadoPrimeraLinea = "".join(primerLinea)
                resultadoSegundaLinea = "".join(segundaLinea)
                resultadosTerceraLinea = "".join(terceraLinea)
                resultadosCuartaLinea = "".join(cuartaLinea)

                if (argumento == False):
                    arranged_problems = resultadoPrimeraLinea + '\n' + resultadoSegundaLinea + '\n' + resultadosTerceraLinea
                    return arranged_problems
                
                else:
                    arranged_problems = resultadoPrimeraLinea + '\n' + resultadoSegundaLinea + '\n' + resultadosTerceraLinea + '\n' + resultadosCuartaLinea
                    return arranged_problems
                