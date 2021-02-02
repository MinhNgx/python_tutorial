class SieuNhan:
    def __init__(self,ten,vu_khi,mau_sac):
        self.ten = "Sieu nhan " + ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        super().__init__()
        
    def xin_chao(self):
        return "Xin chao, ta chinh la " + self.ten

sieu_nhan_A = SieuNhan("do","Kiem","Do")
print("Ten cua sieu nhan la:",sieu_nhan_A.ten)
print("Sieu nhan mau:",sieu_nhan_A.mau_sac)
print("Su dung vu khi:",sieu_nhan_A.vu_khi)

print(sieu_nhan_A.xin_chao())
print(SieuNhan.xin_chao(sieu_nhan_A))
