from database import session
from tables import TblStock
from tables import MstMerchandise
import random,string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

drinks = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}
for k,v in drinks.items():
        mst_merchandise = MstMerchandise(
            id = randomname(10),
            name = k,
            price = int(v)
        )
        session.add(mst_merchandise)
        session.commit()

samples =session.query(MstMerchandise).all()
for s in samples:
    print(s.id)
    tbl_stock = TblStock(
        id = s.id,
        stock = random.randint(0,3)
    )
    session.add(tbl_stock)
    session.commit()