# Dynamic Programming Python implementation of Coin 
# Change problem
def kembalian(Jenis, Uang):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    print "Pertama : Membuat array berisi 0 sebanyak nilai uang yang mau dikembalikan (",Uang, ")"
    table = [0 for k in range(Uang + 1)]
    print "Tabel awal : ",table
 
    # Base case (If given value is 0)
    if (Uang == 0):
        return 0
    else :
        table[0] = 1
        print "Mengisi nilai elemen ke 0 dengan 1 sebagai patokan"
        print "Hasil : ", table
        # Pick all coins one by one and update the table[] values
        # after the index greater than or equal to the value of the
        # picked coin
        print "===========LOOP START============"
        p = 0
        for i in range(0,m): #looping sepanjang array Kembalian
            print "Jenis uang = ",Jenis[i]
            print "Untuk menghindari iterasi terlalu banyak, iterasi selanjutnya dimulai dari elemennya yaitu ke ",Jenis[i]
            for j in range(Jenis[i], len(table)):
                p += 1
                print "Iterasi ke ", p , ", Nilai j = ",j,"\nSebelum : "
                print table
                # print table[j], i, j,j-S[i],  S
                print "Karena nilai table[j-",Jenis[i], "] adalah ",table[j - Jenis[i]], "Maka Elemen ke ",j, " dari tabel ditambah ",table[j - Jenis[i]]
                table[j] += table[j - Jenis[i]]
                print "Sesudah : "
                print table
                print "=========================="
                # print table[j], i, j,j-S[i],  S

        print "===========LOOP END============"
        # print table
        return table[Uang]
 
# Driver program to test above function
arr = [2, 3, 5]
m = len(arr)
n = 4
x = kembalian(arr, n)
print "Hasil Akhir"
print (x)
 
# This code is contributed by Afzal Ansari