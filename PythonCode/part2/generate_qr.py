import qrcode

def generate_qr(data, file_path="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(file_path)

# 示例调用
generate_qr("https://www.google.com")
