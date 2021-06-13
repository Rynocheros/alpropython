"""
JEREMIAS RYAN WIJAYA/20083000140/2F
12-06-2021
PROGRAM MENAMPILKAN GOLONGAN USIA
"""
#cek golongan usia
jwbulangprog = "y"
while jwbulangprog=="y" or jwbulangprog=="Y":
    print ("================================")
    print(" CEK GOLONGAN USIA ")
    print ("================================")
    u=1
    while u>0 and u<=100:
        u = input(" Masukkan Usia = ")
        #cek batasan inputan usia 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts=("LANSIA")
            elif int(u)>=35 and int(u)<=59: sts=("DEWASA")
            elif int(u)>=18 and int(u)<=34: sts=("PEMUDA")
            elif int(u)>=15 and int(u)<=17: sts=("REMAJA")
            else:
                sts="ANAK"
            print(sts)
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break

    jwbulangprog = input(">>> Ulang Program? y/t = ")
    if jwbulangprog=="t" or jwbulangprog=="T":
        break
