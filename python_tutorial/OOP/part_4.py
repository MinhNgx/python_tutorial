class SieuNhan:
    suc_manh = 50
    def __init__(self,ten,vu_khi,mau_sac):
        self.ten = "Sieu nhan " + ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        super().__init__()

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self,ten,vu_khi,mau_sac,su_thu):
        super().__init__(ten,vu_khi,mau_sac) #super la class ma minh ke thua
        self.su_thu = su_thu

SieuNhanDo = SieuNhanGao("do", "Cung", "Do", "vitcon")
print(SieuNhanDo.__dict__)
print(SieuNhanDo.suc_manh)
 
