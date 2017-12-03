# Dynamic Programming Python implementation of Coin 
# Change problem
def count(S, m, n):
 
    table = [0 for k in range(n+1)]
 
    table[0] = 1
    p = 0
    for i in range(0,m): #looping sepanjang array Kembalian
        for j in range(S[i],n+1): #Looping mulai dari indeks yang ditunjuk i, sampai nilai input + 1
            table[j] += table[j-S[i]]
    # print table
    return table[n]
 
# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 8
x = count(arr, m, n)
print "Hasil Akhir"
print (x)
 
# This code is contributed by Afzal Ansari