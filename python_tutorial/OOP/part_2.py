class SieuNhan:
    suc_manh=50
    so_thu_tu = 1
    def __init__(self,ten,vu_khi,mau_sac):
        self.ten = "Sieu nhan " + ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1
        super().__init__()

    def xin_chao(self):
        print("Xin chao. Ta la ", self.ten)
        print("Chi so suc manh la", self.suc_manh)
sieu_nhan_A = SieuNhan("do","Kiem","Do")

sieu_nhan_A.xin_chao()


