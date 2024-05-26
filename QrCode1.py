import qrcode

myqr = qrcode.make("https://www.youtube.com/watch?v=EppKhWIZOv8")
myqr1 = qrcode.make("https://www.youtube.com/watch?v=8Vs2Q2TwKuY")

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)


