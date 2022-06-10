import numpy as np
import math as m
import time
from pathlib import Path
from sys import exit
import tracemalloc
import os
from datetime import datetime
import random
import heapq
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# functions


def menu():
    while True:
        print("Escolha o tipo de ordenação:")
        print("[1] Bubble Sort")
        print("[2] Heapsort")
        print("[3] Criar arquivo base - aleatório x ordenado")
        
        print('[0] Sair')
        a = int(input('Digite uma das quatro opções: '))
        if a == 1:
            ordenacao(1)
        elif a == 2:
            ordenacao(2)
        elif a == 3:
            criaArray()
        elif a == 0:
            print('exit')
            exit()
        else:
            print('Opção inválida, voltando ao menu.')
            return menu()


def bubbleSort(array): #tempo O(n^2)
    n = len(array)-1
    for i in range(n):
        for j in range(0, n-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                continue
    return array

#--------------------------------------------------------------------------#
#ORDENAÇÂO SQRT SORT
def ordena_lista(output): 
    cont = 0
    for sublista in output:
        cont += 1
        bubbleSort(sublista)
        
def maior_valor_lista(output):
     return list(el[-1] for el in output)

def maior_indice_lista(output):
     b = [len(sublist)-1 for sublist in output]
     return b


def ordena_lista_heap(output): 
    for sublista in range(len(output)):
       heapq._heapify_max(output[sublista])

def nested_remove(L, x):
    if x in L:
        L.remove(x)
    else:
        for element in L:
            if type(element) is list:
                nested_remove(element, x)

def valores_maximos(output,indice):
    count = 0
    c = []
    for i in indice:
        if i<0:
            c.append(-1)
        else:
            c.append(output[count][i])
        count+=1
    return c

def sqrt_sort_bubble(b):
    n= m.floor(m.sqrt(len(b)))
    output=list([b[i:i + n] for i in range(0, len(b), n)])
    final = []
    ordena_lista(output)
    indice = []
    valores_maximo = []
    indice = maior_indice_lista(output) #indice dos ultimos valores da sublista
    final = [0 for x in b]
    n2 = len(b)-1
    for i in range(len(b)):
        valores_maximo = valores_maximos(output, indice) 
        max_indice = valores_maximo.index(max(valores_maximo))
        final[n2] = valores_maximo[max_indice]  #adiciona a lista solução
        indice[max_indice] = indice[max_indice] - 1
        n2-=1
    return final

def sqrt_sort_heap(b): 
    n= m.floor(m.sqrt(len(b)))
    output=list([b[i:i + n] for i in range(0, len(b), n)])
    ordena_lista_heap(output)
    indice = 0
    valor_maximo = 0
    final = []
    final = [0 for x in b]
    n=0
    n2 = len(b)-1
    for i in range(len(b)):
        for j in range(len(output)):
            if not output[j]:
            # if len(output[j])
                continue
            elif(valor_maximo < output[j][0]):
                valor_maximo = output[j][0]
                indice = j
        if not output[indice]:
        # if len(output[indice])==0:
            continue
        heapq._heappop_max(output[indice])
        final[n2] = valor_maximo
        valor_maximo = 0
        n2-=1
    return final
    
#-------------------------------------------------------------------------#

def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        leftArray = array[:r]
        rightArray = array[r:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1
    return array


def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)





def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapSort(array):
    n = len(array)
    for i in range(n, -1, -1):
        max_heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, i, 0)
    return array


def criaArray():
    print('Gerando Array...')
    for i in (10**j for j in range(1, 8)):
        x = (random.sample(range(10000000), 10000000))
    np.savetxt('valores.txt', x, delimiter='\t', fmt='%i')
    array = []
    for i in range(int(10000000)):
        array.append(i)
    inv_array = array[::-1]
    np.savetxt('valores_crescentes.txt', array, delimiter='\t', fmt='%i')
    np.savetxt('valores_decrescentes.txt',
               inv_array, delimiter='\t', fmt='%i')
    print('Completo.\n')
    return 'Completo'


def ordenacao(a):
    try:
        Path('valores.txt').resolve(strict=True)
    except IOError:
        cls()
        print('\n---------------------------------\n\tArquivo base não existe\n---------------------------------')
    else:
        f = open('saida_final_final.txt', 'a')
        potencia = 9  # na verdade é a quantidade de digitos
        x = np.loadtxt('valores.txt').astype(int)
        tracemalloc.start()
        tracemalloc.stop()
        if a == 1:
            f.write('Tipo: BubbleSort - Aleatório\n')
            for i in (10**j for j in range(1, potencia-1)):
                c = x[:i]
                b = c.tolist()
                print('Tamanho:', len(b),'inicio:',datetime.now())
                start = time.time()
                tracemalloc.start()
                sqrt_sort_bubble(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.write('Tipo: BubbleSort - Crescente\n')
            for i in (10**j for j in range(1, potencia-1)):
                c = x[:i]
                b = c.tolist()
                print('Tamanho:', len(b),'inicio:',datetime.now())
                start = time.time()
                tracemalloc.start()
                sqrt_sort_bubble(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.write('Tipo: BubbleSort - Decrescente\n')
            # mesmo caso do bubble aleatório, porém pior.
            for i in (10**j for j in range(1, potencia-1)):
                c = x[:i]
                b = c.tolist()
                print('Tamanho:', len(b),'inicio:',datetime.now())
                start = time.time()
                tracemalloc.start()
                sqrt_sort_bubble(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.close()
        x = np.loadtxt('valores.txt').astype(int)
        
        if a == 2:
            f.write('Tipo: HeapSort - Aleatório\n')
            for i in (10**j for j in range(1, potencia)):
                c = x[:i]
                b = c.tolist()
                print('Tipo: HeapSort - Aleatório\nTamanho:', len(b),'inicio:',datetime.now())
                start = time.time()
                tracemalloc.start()
                sqrt_sort_heap(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                #print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.write('Tipo: HeapSort - Crescente\n')
            for i in (10**j for j in range(1, potencia)):
                c = x[:i]
                b = c.tolist()
                print('Tipo: HeapSort - Crescente\nTamanho:', len(b))
                start = time.time()
                tracemalloc.start()
                sqrt_sort_heap(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                #print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.write('Tipo: HeapSort - Decrescente\n')
            for i in (10**j for j in range(1, potencia)):
                c = x[:i]
                b = c.tolist()
                print('Tipo: HeapSort - Decrescente\nTamanho:', len(b),'inicio:',datetime.now())
                start = time.time()
                tracemalloc.start()
                sqrt_sort_heap(b)
                end = time.time()
                current, peak = tracemalloc.get_traced_memory()
                #print("Uso atual de memória atual:	{:.6f}MB; Maior foi:{:.6f}MB".format((current / 10**6), (peak / 10**6)))
                f.write("Uso atual de memória atual:	{:.6f}\tMB;\tMaior foi:\t{:.6f}\tMB\n".format(
                    (current / 10**6), (peak / 10**6)))
                tracemalloc.stop()
                print("Tempo de execução:	{:.16e}s.".format((end-start)))
                print('----------------------------------------')
                f.write('Tamanho do array:\t{:d}\tTempo gasto:\t{:.16f}\ts\n'.format(
                    i, (end-start)))
            f.close()
        x = np.loadtxt('valores.txt').astype(int)
        