per_inch = 2.54
inch = int(input("How long?"))
cm = inch * per_inch

desc = "{0}インチ = {1}センチ".format(inch, cm)
print(desc)