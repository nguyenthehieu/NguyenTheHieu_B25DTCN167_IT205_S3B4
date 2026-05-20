while True :
    quantity_staff = int(input("\nVui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if quantity_staff <= 0 :
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập lớn hơn 0.")

    else :
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {quantity_staff} nhân sự mới")
        break