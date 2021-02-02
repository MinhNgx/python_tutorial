class Sieunhan:
    suc_manh = 50
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = "Sieu nhan " + ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst] #xoa space dau va cuoi trong list
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)
    
infor_str = "do - Kiem - do"
sieu_nhan_A = Sieunhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)