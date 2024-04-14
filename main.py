from SubscriptionManager import SubscriptionManager
from Subscriber import Subscriber
manager = SubscriptionManager()
while True:
    print("1: Thêm người đăng ký mới")
    print("2: Chỉnh sửa thông tin đăng ký")
    print("3: Xóa đăng ký")
    print("4: Xem danh sách người đăng ký theo loại hộ")
    print("5: Xem dữ liệu thô trong tệp")
    print("0: Thoát chương trình")
    choice = input("Nhập một số (0 để thoát): ")
    if choice == '0':
        print("Thoát chương trình!")
        break
    elif choice == '1':
        while True:
            SoDKy = input("Nhập mã đăng ký: ")
            if not SoDKy.isdigit():
                print("Mã đăng ký phải là số. Vui lòng nhập lại.")
            elif not manager.validate_SoDKy(SoDKy):
                print("Mã đăng ký đã được sử dụng. Vui lòng nhập lại.")
            else:
                break

        while True:
            HoTen = input("Nhập họ tên đầy đủ: ")
            if HoTen.strip():
                break
            else:
                print("Họ tên không được để trống. Vui lòng nhập lại.")
        while True:
            DateOfBirth = input("Nhập ngày sinh (dd/mm/yyyy): ")
            if manager.validate_date(DateOfBirth):
                break
            else:
                print("Ngày sinh không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")
        while True:
            Phai = input("Nhập giới tính (Nam hoặc Nữ): ")
            if Phai in ['Nam', 'Nữ']:
                break
            else:
                print("Giới tính phải là 'Nam' hoặc 'Nữ'. Vui lòng nhập lại.")
        while True:
            DiaChi = input("Nhập địa chỉ: ")
            if DiaChi.strip():
                break
            else:
                print("Địa chỉ không được để trống. Vui lòng nhập lại.")
        while True:
            MaSoDienKe = input("Nhập mã của đồng hồ điện sử dụng: ")
            if MaSoDienKe.isdigit():
                break
            else:
                print("Mã đồng hồ điện phải là số. Vui lòng nhập lại.")
        while True:
            DiaChiLapDat = input("Nhập địa chỉ lắp đặt đồng hồ điện: ")
            if DiaChiLapDat.strip():
                break
            else:
                print("Địa chỉ lắp đặt không được để trống. Vui lòng nhập lại.")
        while True:
            LoaiHo = input("Nhập loại hộ (Public utility, Business, Production, Consumption): ")
            if LoaiHo in ['Public utility', 'Business', 'Production', 'Consumption']:
                break
            else:
                print("Loại hộ phải là 'Public utility', 'Business', 'Production', hoặc 'Consumption'. Vui lòng nhập lại.")
        subscriber = Subscriber(SoDKy, HoTen, DateOfBirth, Phai, DiaChi, MaSoDienKe, DiaChiLapDat, LoaiHo)
        manager.add_subscriber(subscriber)
    elif choice == '2':
        while True:
            SoDKy = input("Nhập mã đăng ký: ")
            if not SoDKy.isdigit():
                print("Mã đăng ký phải là số. Vui lòng nhập lại.")
            elif  manager.validate_SoDKy(SoDKy):
                print("Mã đăng ký không tồn tại. Vui lòng nhập lại.")
            else:
                break
        print("Nhập thông tin mới cho người đăng ký")
        while True:
            HoTen = input("Nhập họ tên đầy đủ: ")
            if HoTen.strip():
                break
            else:
                print("Họ tên không được để trống. Vui lòng nhập lại.")
        while True:
            DateOfBirth = input("Nhập ngày sinh (dd/mm/yyyy): ")
            if manager.validate_date(DateOfBirth):
                break
            else:
                print("Ngày sinh không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")
        while True:
            Phai = input("Nhập giới tính (Nam hoặc Nữ): ")
            if Phai in ['Nam', 'Nữ']:
                break
            else:
                print("Giới tính phải là 'Nam' hoặc 'Nữ'. Vui lòng nhập lại.")
        while True:
            DiaChi = input("Nhập địa chỉ: ")
            if DiaChi.strip():
                break
            else:
                print("Địa chỉ không được để trống. Vui lòng nhập lại.")
        while True:
            MaSoDienKe = input("Nhập mã của đồng hồ điện sử dụng: ")
            if MaSoDienKe.isdigit():
                break
            else:
                print("Mã đồng hồ điện phải là số. Vui lòng nhập lại.")
        while True:
            DiaChiLapDat = input("Nhập địa chỉ lắp đặt đồng hồ điện: ")
            if DiaChiLapDat.strip():
                break
            else:
                print("Địa chỉ lắp đặt không được để trống. Vui lòng nhập lại.")
        while True:
            LoaiHo = input("Nhập loại hộ (Public utility, Business, Production, Consumption): ")
            if LoaiHo in ['Public utility', 'Business', 'Production', 'Consumption']:
                break
            else:
                print("Loại hộ phải là 'Public utility', 'Business', 'Production', hoặc 'Consumption'. Vui lòng nhập lại.")
        new_data = {'HoTen': HoTen, 'DateOfBirth': DateOfBirth, 'Phai': Phai, 'DiaChi': DiaChi, 'MaSoDienKe': MaSoDienKe, 'DiaChiLapDat': DiaChiLapDat, 'LoaiHo': LoaiHo}
        manager.edit_subscriber(SoDKy, new_data)
    elif choice == '3':
        while True:
            SoDKy = input("Nhập mã đăng ký: ")
            if not SoDKy.isdigit():
                print("Mã đăng ký phải là số. Vui lòng nhập lại.")
            elif  manager.validate_SoDKy(SoDKy):
                print("Mã đăng ký không tồn tại. Vui lòng nhập lại.")
            else:
                break
        manager.delete_subscriber(SoDKy)
    elif choice == '4':
        while True:
            LoaiHo = input("Nhập loại hộ (Public utility, Business, Production, Consumption): ")
            if LoaiHo in ['Public utility', 'Business', 'Production', 'Consumption']:
                break
            else:
                print("Loại hộ phải là 'Public utility', 'Business', 'Production', hoặc 'Consumption'. Vui lòng nhập lại.")
        manager.view_subscribers_by_household_type(LoaiHo)
    elif choice == '5':
        manager.view_raw_data()
    else: 
        print("Lựa chọn phải là một số từ 0 đến 5. Vui lòng nhập lại.")