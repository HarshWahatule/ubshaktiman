import qrcode

def generate_qr(query):
    img = qrcode.make(query)
    
