import segno 
me = my_website_address = 'hirerivers.netlify.app'
#this line construst the qr code 
qr = segno.make(me) 
#creat your own filename and then run the file to genrate your very own qr code / use .png to generate an IMG
qr.save('hireriversanthony.png', dark='darkred', data_dark='darkorange', data_light='yellow')