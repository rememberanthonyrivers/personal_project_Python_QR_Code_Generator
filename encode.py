import segno 
#the below line assigns the address that will be linked to the qr code 
greet = '\n*** Welcome to My QR Code Generator! *** \n'
web_address = input(greet + '\n\tEnter the infomation you would like to save to a QR Code : \n')

#the below line makes the qr code 
qr = segno.make(web_address, micro=False) 

#create your own filename and then run the file to genrate your very own qr code / use .png to generate an IMG
qr.save('site.png')

print("\n\t*** Thank you for using my Program, Enjoy your new QR Code! ***\n")