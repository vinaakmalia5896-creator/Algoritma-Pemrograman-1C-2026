tiket =int(input('membeli tiket: '))
jenis =str(input('jenis tiket: '))
reguler = 40000
vip = 750000
vvip = 100000
if tiket == reguler :
    print('tidak dapat minum')
elif tiket == vip :
    print('mendapat minuman gratis')
elif tiket == vvip :
    print('mendapat minum gratis')

biaya = tiket * jenis

print('bayar: ',biaya)


# input beli tiket tipe tiket bayar tikett udahh