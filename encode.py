import segno 
#this line assigns the address that will be linked to the qr code 
website_address = 'www.google.com'
#this line construst the qr code 
qr = segno.make(website_address, micro=False) 
#create your own filename and then run the file to genrate your very own qr code / use .png to generate an IMG
qr.save('site.png')