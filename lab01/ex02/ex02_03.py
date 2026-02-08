#input: số
#output: kiểm tra số đó có phải số chẵn hay không

so = int(input("NHập một số nguyên: "))
if so%2==0:
    print(so, "là số chẵn")
else:
    print(so, "không phải là số chẵn")