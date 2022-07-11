from bs4 import BeautifulSoup
import requests as req
import json
import urllib.request as ur
from os.path import exists


# Lấy dữ liệu từ file XML    
resp = req.get('https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7')
soup = BeautifulSoup(resp.text, 'lxml')

thue = [] 
for tag in soup.find_all('tax'):
    try:
        a = tag.min.text
    except AttributeError:
        pass
        
    try: 
        b = tag.max.text
    except AttributeError:
        pass
        
    try: 
        c = tag.value.text
    except AttributeError:
        pass
        
    thue_theoluong = a, b, c
    thue.append(thue_theoluong)        

# Lấy dữ liệu từ file JSON
json_url = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'
data = ur.urlopen(json_url).read().decode('utf-8')
json_obj = json.loads(data)

phat = []
for i in range(len(json_obj)):
    try:
        x = f'{json_obj[i]["min"]}'
    except KeyError:
        pass
        
    try:
        y = f'{json_obj[i]["max"]}'        
    except KeyError:
        y = None
        pass
        
    try:
        z = f'{json_obj[i]["value"]}'
    except KeyError:
        pass
        
    late_date = x, y, z
    phat.append(late_date)
    
list_employee = [] # khởi tạo 1 danh sách nhân viên
list_manager = [] # khởi tạo 1 danh sách quản lý
list_department = [] # khởi tạo 1 danh sách bộ phận

# khởi tạo lớp nhân viên
class Employee:
    def __init__(self, id, name, salary, day, iddepartment, performance, bonus, late, level):
        self.id = id
        self.name = name
        self.salary_base = salary
        self.working_days = day
        self.iddepartment = iddepartment
        self.working_performance = performance
        self.bonus = bonus
        self.late_comming_days = late
        self.luong_thucnhan = 0
        self.chucvu = level

    #Hàm tính lương nhân viên
    def tinh_luong(self):
        luong = float((self.salary_base * self.working_days) * self.working_performance) #Thu nhập chưa thưởng
        print(luong)
        # Tính tiền thuế nhân viên phải đóng
        thue_cannop = 0
        for m in thue: # dựa vào thue được lấy ra từ dữ liệu của file XML ở trên
            if (int(m[0])*(10**6)) < luong:
                if m[1] is not None: #trong file XML không có giá trị của nhãn max
                    if luong <= (int(m[1])*(10**6)):                
                        thue_cannop = luong*int(m[2])*0.01
                else:
                    thue_cannop = luong*int(m[2])*0.01
        print(thue_cannop)           
        # Tính lương phạt
        for n in phat: # dựa vào phat được lấy ra từ dữ liệu của file JSON
            if int(n[0]) < self.late_comming_days:
                if n[1] is not None: # trong file JSON không có giá trị của nhãn max
                    if self.late_comming_days <= int(n[1]):                
                        tienphat_dimuon = self.late_comming_days*int(n[2])
                else:
                    tienphat_dimuon = self.working_performance*int(n[2])
        
        # Khởi tạo thưởng bộ phận cho tường người
        bonus_salary = 0    
        for department in list_department:
            if department.id == self.iddepartment:
                bonus_salary = department.bonus_salary
                
        # Biểu thức tính lương của nhân viên         
        self.total_luong = float(luong + self.bonus + bonus_salary - tienphat_dimuon) #lương đã thêm thưởng và phạt
        self.total_luong_chuathue = float(self.total_luong * 0.895) #lương chưa tính thuế, đóng bảo hiểm 10.5%
        self.luong_thucnhan = float(self.total_luong_chuathue - thue_cannop) #lương đã tính thuế
        print("tinh luong Employee")
        return self.luong_thucnhan

# khởi tạo lớp quản lý
class Manager(Employee):
    def _init_(self, id, name, salary, day, iddepartment, performance, bonus, late, level):
        Employee.__init__(self, id, name, salary, day, iddepartment, performance, bonus, late, level)
        
    def tinh_luong(self):
        luong = float((self.salary_base * self.working_days) * self.working_performance) #Thu nhập chưa thưởng
        print(luong)
        # Tính tiền thuế nhân viên phải đóng
        for m in thue:
            if (int(m[0])*(10**6)) < luong:
                if m[1] is not None:
                    if luong <= (int(m[1])*(10**6)):                
                        thue_cannop = luong*int(m[2])*0.01
                else:
                    thue_cannop = luong*int(m[2])*0.01
                
                
        # Tính lương phạt
        for n in phat:
            if int(n[0]) < self.late_comming_days:
                if n[1] is not None:
                    if self.late_comming_days <= int(n[1]):                
                        tienphat_dimuon = self.late_comming_days*int(n[2])
                else:
                    tienphat_dimuon = self.late_comming_days*int(n[2])

        bonus_salary = 0    
        for department in list_department:
            if department.id == self.iddepartment:
                bonus_salary = department.bonus_salary
                
        self.total_luong = float(luong + self.bonus + (bonus_salary*1.1) - tienphat_dimuon) #lương đã thêm thưởng và phạt
        self.total_luong_chuathue = float(self.total_luong * 0.895) #lương chưa tính thuế, đóng bảo hiểm 10.5%
        self.luong_thucnhan = float(self.total_luong_chuathue - thue_cannop) #lương đã tính thuế
        print("tinh luong manager")
        return self.luong_thucnhan    
        
# khơi tạo Lớp bộ phận
class Department:
    def __init__(self, id, bonus_salary):
        self.id = id
        self.bonus_salary = bonus_salary


def docfilejson():
    # Mở file JSON 
    file_exists = exists("Employee.json")
    if file_exists == False:
        return 
    f = open('Employee.json')
      
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
  
    # Iterating through the json
    # list
    for employee in data['Employee']:
        if employee["Level"].lower() == "ql":
            new_employee = Manager(employee["ID"], employee["Name"], employee["salary"], employee["working_days"], employee["ID_department"], employee["Performance"], employee["Bonus"], employee["late_working_date"], employee["Level"])
        else:
            new_employee = Employee(employee["ID"], employee["Name"], employee["salary"], employee["working_days"], employee["ID_department"], employee["Performance"], employee["Bonus"], employee["late_working_date"], employee["Level"])
        list_employee.append(new_employee)
        
    for department in data["Department"]:
        new_department = Department(department["ID"], department["bonus_salary"])
        list_department.append(new_department)
        
    f.close()   
    
def luuvaofilejson():
    list_employees = []
    dict_data = dict()
    list_departments = []
    
    for employee in list_employee:
        dict_employee = dict()
        dict_employee = {"salary": employee.salary_base,"Name": employee.name,"Level": employee.chucvu,"working_days": employee.working_days,"Performance": employee.working_performance,"late_working_date": employee.late_comming_days,"ID_department": employee.iddepartment,"ID": employee.id,"Bonus": employee.bonus} 
        list_employees.append(dict_employee)
    dict_data["Employee"] = list_employees
    
    for department in list_department:
        dict_department = dict()
        dict_department = {"ID": department.id, "bonus_salary": department.bonus_salary}
        list_departments.append(dict_department)
    dict_data["Department"] = list_departments
    
    with open('Employee.json', 'w', encoding='utf-8') as f:
        json.dump(dict_data, f, ensure_ascii = False, indent=4)

# Hàm hiển thị danh sách nhân viên        
def list_Employee():
    for employee in list_employee:
        print("----")
        print("Mã số: ", employee.id)
        print("Mã bộ phận: ", employee.iddepartment)
        print("Chức vụ: ", employee.chucvu)
        print("Họ và tên: ", employee.name)
        print("Hệ số lương: ", employee.salary_base)
        print("Số ngày làm việc: ", employee.working_days, "(ngày)")
        print("Hệ số hiệu quả: ", employee.working_performance)
        print("Thưởng: ", employee.bonus, "(VND")
        print("Số ngày đi muộn: ", employee.late_comming_days, "ngày")
        print("----")

# Hàm hiển thị danh sách bộ phận
def list_Department():
    for department in list_department:
        print("----")
        print("Mã bộ phận: ", department.id)
        print("Thưởng bộ phận: ", department.bonus_salary, "(VND)")
        print("----")

# Hàm thêm nhâ viên
def addnew_Employee():
    print("----")
    print("Thêm nhân viên mới ...")
    while True:
        Id = input("Nhập mã số: ")
        # kiểm tra không được bỏ trống thông tin với ID nhân viên
        if Id == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
            
        count = 0
        for employee in list_employee:
        # Checking if Employee with given Id
        # Already Exist or Not   
            if employee.id == Id:
                print("Mã nhân viên đã tồn tại\nThử lại\n")
                break
            else:
                count += 1
        if count == len(list_employee):
            break 
            
            
    while True:
        # kiểm tra không được bỏ trống thông tin với mã bộ phận
        mabophan = input("Nhập mã bộ phận: ")
        if mabophan == "":
            print("Bạn không được bỏ trống thông tin này")
        else:
            break
            
    count_department = 0
    for department in list_department:
        # Kiểm tra xem mã bộ phần đã có hay chưa
        if department.id == mabophan:
            break
        else:
            count_department += 1
      
    if count_department == len(list_department):
        print("Mã bộ phận chưa tồn tại, tạo mới ...")
        while True:
            thuong_bophan = input("Nhập thưởng bộ phận: ")
            # kiểm tra không được bỏ trống thông tin với thưởng bộ phận
            if thuong_bophan == "":
                print("Bạn không được bỏ trống thông tin này")
                continue
            # Kiểm tra nhập vào là số dương, không được nhập số âm
            if int(thuong_bophan) > 0:
                new_department = Department(mabophan, int(thuong_bophan))
                list_department.append(new_department)
                print("Đã tạo bộ phận mới ...")
                break
            else:
                print("Bạn phải nhập một số dương")
        
    while True:
        Chucvu = input("Nhập chức vụ (NV / QL): ")
        if Chucvu == "":
            print("Bạn không được bỏ trống thông tin này")
        else:
            break
            
    while True:    
        Name = input("Nhập họ và tên: ")
        if Name == "":
            print("Bạn không được bỏ trống thông tin này")
        else:
            break
            
    while True:        
        salary = input("Nhập hệ số lương: ")
        if salary == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        if int(salary) > 0:
            break
        else:
            print("Bạn phải nhập một số dương")
            
    while True:
        working_days = input("Nhập số ngày làm việc: ")
        if working_days == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        if int(working_days) > 0:
            break
        else:
            print("Bạn phải nhập một số dương")
            
    while True:
        performance = input("Nhập hệ số hiệu quả: ")
        if performance == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        if float(performance) > 0:
            break
        else:
            print("Bạn phải nhập một số dương")
            
    while True:        
        bonus = input("Nhập thưởng: ")
        if bonus == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        if int(bonus) > 0:
            break
        else:
            print("Bạn phải nhập một số dương")
            
    while True:
        late_working_days = input("Nhập số ngày đi muộn: ")
        if late_working_days == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        if int(late_working_days) > 0:
            break
        else:
            print("Bạn phải nhập một số dương")
            
    print("Đã thêm nhân viên mới ...")
    print("----")
    
    # Kiểm tra chức vụ là nhân viên hay quản lý
    if Chucvu.lower() == "ql":
        new_employee = Manager(Id, Name, int(salary), int(working_days), mabophan, float(performance), int(bonus), int(late_working_days), Chucvu)
        print("add manager")
    else:
        new_employee = Employee(Id, Name, int(salary), int(working_days), mabophan, float(performance), int(bonus), int(late_working_days), Chucvu)
        print("add employ")
        
    list_employee.append(new_employee)
    
# Hàm xóa nhân viên    
def remove_EmployeeswithID():
    print("----")
    while True:
        xoa_id = input("Nhập mã nhân viên muốn xóa: ")
        if xoa_id == "":
            print("Bạn không được bỏ trống thông tin này")
            continue
        count = 0 
        for employee in list_employee:
            if xoa_id == employee.id:
                list_employee.remove(employee)
                print("Đã xóa thành công")
                return
            else:
                count += 1
                
        if count == len(list_employee):
            print("Mã nhân viên không tồn tại")
            return
    print("----")

# Hàm xóa bộ phận
def remove_DepartmentwithID():
    print("----")
    while True:
        xoa_id = input("Nhập mã bộ phận muốn xóa: ")
        if xoa_id == "":
            continue
        for employee in list_employee:
            if employee.iddepartment == xoa_id:
                print("Bạn không thể xóa bộ phận đang có nhân viên")
                return 
            
        count = 0 
        for department in list_department:
            if xoa_id == department.id:
                list_department.remove(department)
                print("Đã xóa thành công")
                return
            else:
                count += 1
        if count == len(list_department):
            print("Mã bộ phận không tồn tại")    
            return
    print("----")

# Hàm hiển thị bảng lương
def tabale_salary():
    for employee in list_employee:
        print("----")
        print("Mã số: ", employee.id)    
        print("Thu nhập thực nhận: ", employee.tinh_luong())        
        print("----")

# Hàm hiển thị các lựa chọn        
def menu():
    print("1. Hiển thị danh sách nhân viên.")
    print("2. Hiển thị danh sách bộ phận.")
    print("3. Thêm nhân viên mới.")
    print("4. Xóa nhân viên theo ID.")
    print("5. Xóa bộ phân theo ID")
    print("6. Hiển thị bảng lương.")
    print("7. Thoát.")

    # Taking choice from user
    ch = int(input("Mời bạn nhập chức năng mong muốn: "))
    if ch == 1:
        list_Employee()
        
    elif ch == 2:
        list_Department()

    elif ch == 3:
        addnew_Employee()

    elif ch == 4:
        remove_EmployeeswithID()

    elif ch == 5:
        remove_DepartmentwithID()

    elif ch == 6:
        tabale_salary()

    elif ch == 7:
        luuvaofilejson()
        exit(0)
        return
    else:
        print("Invalid Choice")
    
    menu()

    
docfilejson()
menu()

