import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID =")

#upi://pay?pa=UPI_ID&=NAME&Amount&cu=CURRENCY&=MESSAGE
#Defining the payment URl Based on the payment apps you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code as an image

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the qr code (you may need )
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()