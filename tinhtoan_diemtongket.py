filename =input("Enter the file name: ")
try:
    handle = open(filename)
except:
    print("File name not found: ", filename)
    exit()
    

lst = []
lst1 = []
bangdiemchuan = dict()
monhoc = list()

def tinhdiem_trungbinh(path):
    for line in handle:
        line = line.rstrip()
        if line.startswith("Ma HS"):
            tenmuc = line.split(",")
            monhoc = tenmuc[1:]
        if not line.startswith("Ma HS"):
            diem = line.split(";")
            mahs = diem[0]
            ma_hs = mahs.split(",").pop(0)
            lst1.append(ma_hs)
            montunhien = diem[1:5]
            monxahoi = diem[5:]
        
            toan = ((montunhien[0]).split(","))
            ly = ((montunhien[1]).split(","))
            hoa = ((montunhien[2]).split(","))
            sinh = ((montunhien[3]).split(","))
            van = ((monxahoi[0]).split(","))
            anh = ((monxahoi[1]).split(","))
            su = ((monxahoi[2]).split(","))
            dia = ((monxahoi[3]).split(","))

            tbtoan = float(toan[0])*0.05 + float(toan[1])*0.1 + float(toan[2])*0.15 + float(toan[3])*0.7
            tbly = float(ly[0])*0.05 + float(ly[1])*0.1 + float(ly[2])*0.15 + float(ly[3])*0.7
            tbhoa = float(hoa[0])*0.05 + float(hoa[1])*0.1 + float(hoa[2])*0.15 + float(toan[3])*0.7
            tbsinh = float(sinh[0])*0.05 + float(sinh[1])*0.1 + float(sinh[2])*0.15 + float(sinh[3])*0.7
            tbvan = float(van[0])*0.05 + float(van[1])*0.1 + float(van[2])*0.1 + float(van[3])*0.15 + float(van[4])*0.6
            tbanh = float(anh[0])*0.05 + float(anh[1])*0.1 + float(anh[2])*0.1 + float(anh[3])*0.15 + float(anh[4])*0.6
            tbsu = float(su[0])*0.05 + float(su[1])*0.1 + float(su[2])*0.1 + float(su[3])*0.15 + float(su[4])*0.6
            tbdia = float(dia[0])*0.05 + float(dia[1])*0.1 + float(dia[2])*0.1 + float(dia[3])*0.15 + float(dia[4])*0.6
        
            t = round(tbtoan, 2)
            v = round(tbvan, 2)
            h = round(tbhoa, 2)
            sinh = round(tbsinh, 2)
            l = round(tbly, 2)
            a = round(tbanh, 2)
            su = round(tbsu, 2)
            d = round(tbdia, 2)
            tong = t, l, h, sinh, v, a, su, d
            bangdiem = dict(zip(monhoc, tong))
            
            lst.append(bangdiem)
            #bangdiemchuan = dict(zip(ma_hs, lst))
            bangdiemchuan[ma_hs] = bangdiem
    print(bangdiemchuan)
           

dest = "Diem_trungbinh.txt"
def luudiem_trungbinh(dest, bangdiemchuan):
    with open(dest, 'w', encoding = "utf-8") as f:
        f.write('Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Đia \n')
        #print(bangdiemchuan)
        for x, y in bangdiemchuan.items():
            monhoc = [' Toan', ' Ly', ' Hoa', ' Sinh', ' Van', ' Anh', ' Su', ' Dia']
            diemtrungbinh = list()
            diemtrungbinh.append(x)
            for y in monhoc:
                diemtrungbinh.append(bangdiemchuan[x][y])
            #print(diemtrungbinh)
            f.write(';'.join(map(str, diemtrungbinh)) + '\n')
        
        
             
def main():
    path = 'diem_chitiet.txt'
    dest = 'Diem_trungbinh.txt'
    tinhdiem_trungbinh(path)
    #print(bangdiemchuan)
    luudiem_trungbinh(dest, bangdiemchuan)
    print('Bai 1: OK')

main()