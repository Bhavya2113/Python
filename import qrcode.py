import qrcode
'''qr=qrcode.make("https://www.linkedin.com/in/bhavyasrivadlamudi/")
qr.save("docpy.png")'''




















qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter your name:")
age=int(input("Enter your age:"))
email=input("enter your email:")
mobile=int(input("enter your mobile:"))
data={"Name":name,"Age":age,"Email":email,"mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("mydetails_in_qr.png")