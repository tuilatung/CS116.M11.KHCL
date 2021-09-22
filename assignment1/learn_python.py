class SinhVien:
    def __init__(self, id, ten) -> None:
        self.id = id
        self.ten = ten
    def show(self):
        print("ID: ", self.id)
        print("Ten: ", self.ten)

sv = SinhVien(123, "Tung")
sv.show()