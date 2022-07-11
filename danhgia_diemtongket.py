xeploai = dict()   
def xeploai_hocsinh(handle):    
    for line in handle:
        line = line.rstrip()
        dtb_chuan = 0
        loai = str()
        if line.startswith("Ma HS"):
            tenmuc = line.split(",")
            monhoc = tenmuc[1:]
            continue
            #print(tenmuc)
        if not line.startswith("Ma HS"):
            diemtb = line.split(";")
            #print(diemtb)
            mahs = diemtb[0]
            diem_tb = diemtb[1:]
            mon_xahoi = float(float(diemtb[2]) + float(diemtb[3]) + float(diemtb[4]) + float(diemtb[7]) + float(diemtb[8]))
            mon_tunhien = float((float(diemtb[1]) + float(diemtb[5]) + float(diemtb[6]))*2)
            dtb_chuan = (mon_xahoi + mon_tunhien) /11
            dtb_chuan = round(dtb_chuan, 2)
            #print(diem_tb)
            diem_tb.sort()
            #print(diem_tb)
            #print(dtb_chuan)
        if dtb_chuan > 9:
            if float(diem_tb[0]) > 8:
                loai = "xuat sac"
            elif float(diem_tb[0]) > 6.5:
                loai = "gioi"
            elif float(diem_tb[0]) > 5:
                loai = "kha"
            elif float(diem_tb[0]) > 4.5:
                loai = "tb kha"
            else:
                loai = "trung binh"
        elif dtb_chuan > 8:
            if float(diem_tb[0]) > 6.5:
                loai = "gioi"
            elif float(diem_tb[0]) > 5:
                loai = "kha"
            elif float(diem_tb[0]) > 4.5:
                loai = "tb kha"
            else:
                loai = "trung binh"
        elif dtb_chuan > 6.5:           
            if float(diem_tb[0]) > 5:
                loai = "kha"
            elif float(diem_tb[0]) > 4.5:
                loai = "tb kha"
            else:
                loai = "trung binh"
        elif dtb_chuan > 6:           
            if float(diem_tb[0]) > 4.5:
                loai = "tb kha"
            else:
                loai = "trung binh"
        else:
            loai = "trung binh"
        
        xeploai[mahs] = loai
    return xeploai
    
        

xeploaib = dict()
def xeploai_thidaihoc_hocsinh(handle):
    for data in handle:
        data = data.rstrip()        
        loaib = str()
        
        if data.startswith("Ma HS"):
            tenmucb = data.split(",")
            monhocb = tenmucb[1:]
           
            continue
            #print(tenmuc)
        if not data.startswith("Ma HS"):
            
            diemtbmon = data.split(";")
            #print(diemtb)
            mahsb = diemtbmon[0]
            diem_tb_mon = diemtbmon[1:]
            dtb_toan = float(diem_tb_mon[0])
            dtb_ly = float(diem_tb_mon[1])
            dtb_hoa =float(diem_tb_mon[2])
            dtb_sinh = float(diem_tb_mon[3])
            dtb_van = float(diem_tb_mon[4])
            dtb_anh = float(diem_tb_mon[5])
            dtb_su = float(diem_tb_mon[6])
            dtb_dia = float(diem_tb_mon[7])
            
            khoiA = dtb_toan + dtb_ly + dtb_hoa
            khoiA1 = dtb_toan + dtb_ly + dtb_anh
            khoiB = dtb_toan + dtb_hoa + dtb_sinh
            khoiC = dtb_van + dtb_su + dtb_dia
            khoiD = dtb_toan + dtb_van + dtb_anh*2
            
            A = round(khoiA, 2)
            A1 = round(khoiA1, 2)
            B = round(khoiB, 2)
            C = round(khoiC, 2)
            D = round(khoiD, 2)
            
            
            diemTB_khoi = list()
            diemTB_khoi.append(A)
            diemTB_khoi.append(A1)
            diemTB_khoi.append(B)
            diemTB_khoi.append(C)
            diemTB_khoi.append(D)
            #print(diemTB_khoi)
            diemTB_xeploai = list()
            for i in diemTB_khoi:
                if i >= 24 :
                    diemTB_xeploai.append("1") 
                elif  i >= 18:
                    diemTB_xeploai.append("2")
                elif  i >= 12:
                    diemTB_xeploai.append("3")
                else:
                    diemTB_xeploai.append("4")           
            #print(diemTB_xeploai)                   
            xeploaib[mahsb] = diemTB_xeploai
    return xeploaib
            
def main():
    
    filename =input("Enter the file name: ")
    try:
        handle = open(filename, "r", encoding="utf8")
        lines = handle.readlines()
        #print(handle.readlines())
        xeploai = xeploai_hocsinh(lines)
        diemtheokhoi = xeploai_thidaihoc_hocsinh(lines)
        print(xeploai)
        print(diemtheokhoi)
    except:
        print("File name not found: ", filename)
        exit()
    # ghi ra file moi
    with open("danhgia_hocsinh.txt", 'w') as f:
        first_line = 'Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D\n'
        f.write(first_line)
        for x, y in xeploai.items():
            # Tao new_line từ việc cắt ghép xeploai_TBchuan với xeploai_khoithi
            line = x + ";" + y + ";" + ";".join(diemtheokhoi[x])
            
            f.write(line + '\n')

    print('Bai 2: OK')
main()