def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini #anggap ini yang terkecil
    for i in range(dariSini + 1, sampaiSini): #cari di sisa list
        if A[i] < A[posisiYangTerkecil]: #kalau menemukan yang lebih kecil,
            posisiYangTerkecil = i #anggapan dirubah
    return posisiYangTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1): #lakukan operasi gelembung sebanyak n-1
        for j in range(n-i-1): #dorong elemen terbesar ke ujung kanan
            if A[j] > A[j + 1]: #jika di kiri lebih besar dari di kanannya,
                swap(A, j, j+1) #tukar posisi elemen ke j dengan ke j+1

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexkecil = cariPosisiYangTerkecil (A, i, n)
        if indexkecil != i :
            swap(A, i, indexkecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos -1]: #Cari posisi yang tepat
            A[pos] = A[pos -1] #dan geser ke kanan terus
            pos = pos -1 #nilai - nilai yang lebih besar
        A[pos] = nilai #pada posisi ini ditempatkan nilai elemet ke i.
