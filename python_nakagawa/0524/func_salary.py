import math

# 給与を渡すと支給額、税額を返す関数
def calcSalary(salary):

  if salary > 1000000:
    over = salary - 1000000
    tax =  over * 0.2 + 100000
  else:
      tax = salary * 0.1

  # 小数点切り上げ
  tax = math.floor(tax)
  pay = salary - tax
  # 支給額と税額を返す
  return tax, pay

    