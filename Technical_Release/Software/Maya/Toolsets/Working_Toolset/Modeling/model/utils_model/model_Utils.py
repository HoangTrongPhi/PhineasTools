class modeling_Utils:
    @staticmethod
    def splitString(comp):
        """
        Tách số nguyên nằm trong dấu ngoặc vuông của chuỗi.
        Ví dụ: 'cube[12]' -> trả về 12 (int).
        """
        try:
            return int(str(comp).split('[')[1].split(']')[0])
        except (IndexError, ValueError):
            return None  # Trả về None nếu không đúng định dạng

    @staticmethod
    def inLineMessage(message, fadeTime=3):
        """
        Hiển thị thông báo (console), mô phỏng chức năng inViewMessage trong Maya.
        - message: Nội dung thông báo.
        - fadeTime: Thời gian tự động ẩn thông báo (giây), chỉ in ra màn hình, không fade thực sự.
        """
        print(f"[INLINE MESSAGE] {message} (Sẽ ẩn sau {fadeTime} giây)")
        # Ở môi trường thật có thể dùng threading + time.sleep để ẩn sau fadeTime,
        # hoặc tích hợp UI custom nếu chạy ngoài Maya.


