#input: các dòng văn bản từ người dùng, 
#output: chuyển các dòng thành chữ in hoa

print("nhập các dòng văn bản( nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    
print("\nCác dòng đã nhập sau khi đã chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())