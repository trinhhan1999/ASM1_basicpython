# ASM1_basicpython
lst = []
n = int(input())

for i in range(n):
    lst.append(int(input()))
    
def dodaicanh_tamgiac(xx1, xx2 ,yy1, yy2):
    return math.sqrt( (xx1 - xx2)**2 +  (yy1 - yy2)**2 )

Ax, Ay, Bx, By, Cx, Cy = lst
#Độ dài của 3 cạnh tam giác
a = AB = dodaicanh_tamgiac(Ax, Bx, Ay, By)
c = BC = dodaicanh_tamgiac(Bx, Cx, By, Cy)
b = AC = dodaicanh_tamgiac(Cx, Ax, Cy, Ay)
AB = round(AB, 2)
AC = round(AC, 2)
BC = round(BC, 2)
#Kiểm tra xem ABC có tạo thành tam giác hay không
def kiemtra_tamgiac():
    if BC + AB != AC or  AC + AB != BC or AC + BC != AB:
        print("ABC là tam giác")
    else:
        print("ABC không là tam giác")
        

#Tính độ dài và góc tam giác

def goccanh_tamgiac(a1, b1, c1):
    G = degrees(acos((a1**2 + b1**2 - c1**2)/(2*a1*c1)))
    return G

gocA = goccanh_tamgiac(a, b, c)
gocA =  round(gocA, 2)
gocB = goccanh_tamgiac(a, c, b)
gocB = round(gocB, 2)
gocC = 180 - gocA - gocB
gocC = round(gocC, 2)


#Kiểm tra loại tam giác
def xet_tamgiac():
    if BC + AB != AC and  AC + AB != BC and AC + BC != AB:
       #Kiem tra tam giac vuong can va vuong
       if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            if a == b or a == c or b == c:
                print("ABC la tam giac vuong can")
            else:
                print("ABC la tam giac vuong")
       #Kiem tra tam giac deu
       elif a==b and b==c:
           print("ABC là tam giac deu")
       #Kiem tra tam giac can
       elif a==b or a==c or b==c:
           print("ABC la tam giac can")
       #Kiem tra tam giac tu deu va tu
       elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
            if a == b or a == c or b == c:
                print("ABC la tam giac tu deu")
            else:
                print("ABC la tam gai tu")
       #Cac truong hop con lai la tam giac nhon
       else:
           print("ABC la tam giac binh thuong")
    else:
        print("khong phai la tam giac")
        


# Tính chu vi và diện tích tam giác
def dientich_tamgiac():
    if BC + AB != AC and  AC + AB != BC and AC + BC != AB:
        print("True")
        #Tính chu vi
        cv = a + b + c
        cv = round(cv, 2)
        
        #Tính diện tích tam giác
        p = cv/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        s = round(s, 2)
    else:
        print("False")

# Tính đương cao của tam giác
cv = a + b + c #chu vi tam giac
cv = round(cv, 2)
p = cv/2 #nua chu vi tam giac
s = math.sqrt(p*(p-a)*(p-b)*(p-c)) #dien tich tam giac
s = round(s, 2)
def duongcao_tamgiac(x):
    trungtuyen = (2*(s/x))
    return trungtuyen

ha = duongcao_tamgiac(c)#Đường cao từ góc A
ha = round(ha, 2)
hb = duongcao_tamgiac(b)#Đường cao từ góc B
hb = round(hb, 2)
hc = duongcao_tamgiac(a)#Đường cao từ góc C
hc = round(hc, 2)

           
#Tính độ dài trung tuyến tam giác
def trungtuyen_tamgiac(x1, x2, x3):
    m = sqrt((2*(x1*x1+x2*x2)-x3*x3)/4)        
    return m

ma = trungtuyen_tamgiac(b, c, a)#Trung tuyến tại góc A
tta = (2*ma)/3
tta = round(tta, 2)#Độ dài trung tuyến tại đỉnh A tới trọng tâm
mb = trungtuyen_tamgiac(a, c, b)#Trung tuyến tại góc B
ttb = (2*mb)/3
ttb = round(ttb, 2)#Độ dài trung tuyến tại đỉnh B tới trọng tâm
mc = trungtuyen_tamgiac(a, b, c)#Trung tuyến tại góc C
ttc = (2*mc)/3
ttc = round(ttc, 2)#Độ dài trung tuyến tại đỉnh C tới trọng tâm
           

def giaima_tamgiac():
    kiemtra_tamgiac()
    print("Chieu dai canh AB: ",AB)
    print("Chieu dai canh AC: ",AC)
    print("Chieu dai canh BC: ",BC)
    print("Goc A: ", gocA)
    print("Goc B: ", gocB)
    print("Goc C: ", gocC)
    xet_tamgiac()
    print("Chu vi = ", cv)
    print("Diện tích = ", s)
    print("Do dai duong cao tu dinh A: ",ha )
    print("Do dai duong cao tu dinh B: ",hb )
    print("Do dai duong cao tu dinh C: ",hc )
    print("Khoang cach den trong tam tu dinh A: ",tta)
    print("Khoang cach den trong tam tu dinh B: ",ttb)
    print("Khoang cach den trong tam tu dinh C: ",ttc)
    
giaima_tamgiac()
