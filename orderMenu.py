from customtkinter import *
from PIL import Image
from vendingMachine import *

string = ''
counter = 0
counter2 = 1

vm = VendingMachine()

class Images:
    def headerbg(root):
        headbg = Image.open("IconTBO\Header.png")
        imgHead = CTkImage(light_image=headbg, size=(600, 135))
        headLabel = CTkLabel(master=root,
                             text='',
                             image=imgHead,   
                             ).pack()
                             
    def gambarStart(root):
        GambarStart1 = Image.open("IconTBO\GambarStart.png")
        gambar1 = CTkImage(light_image=GambarStart1, size=(189, 270))
        startGambar = CTkLabel(master=root,
                             text='',
                             image=gambar1,   
                             ).place(x=21,
                                     y=230, 
                             )
        GambarStart2 = Image.open("IconTBO\GambarStart2.png")
        gambar2 = CTkImage(light_image=GambarStart2, size=(189, 270))
        startGambar2 = CTkLabel(master=root,
                             text='',
                             image=gambar2,   
                             ).place(x=409,
                                     y=230, 
                             )
                             
    def thxtext(root):
        thxtext = Image.open("IconTBO\ThxText.png")
        thximg = CTkImage(light_image=thxtext, size=(490, 250))
        thxLabel = CTkLabel(master=root,
                           text='',
                           image=thximg,
                           ).place(x=54,
                                   y=153,
                            )
                         
    def iceIcon(root):
        iceIcontxt = Image.open("IconTBO\Ice.png")
        iceIconimg = CTkImage(light_image=iceIcontxt, size=(180, 180))
        iceIconLabel = CTkLabel(master=root,
                           text='',
                           image=iceIconimg,
                           ).place(x=49,
                                   y=236,
                            )
                           
    def womenwithcoffee(root):
        womencoffee = Image.open("IconTBO\With teal background.png")
        womencoffeeimg = CTkImage(light_image=womencoffee, size=(216, 282))
        womencoffeeLabel = CTkLabel(master=root,
                           text='',
                           image=womencoffeeimg,
                           ).place(x=68,
                                   y=205,
                            )
                           
    def sugarIcon(root):
        sugarIcontxt = Image.open("IconTBO\Sugar.png")
        sugarimg = CTkImage(light_image=sugarIcontxt, size=(160, 197.23))
        sugarLabel = CTkLabel(master=root,
                           text='',
                           image=sugarimg,
                           ).place(x=59, 
                                   y=244,
                            )
                           
    def icecoffee(root):
        iceCoffeetext = Image.open("IconTBO\IceCoffee.png")
        iceCoffeeimg = CTkImage(light_image=iceCoffeetext, size=(89.51, 130))
        iceCoffeeLabel = CTkLabel(master=root,
                           text='',
                           image=iceCoffeeimg,
                           fg_color="#FFE0BC",
                           ).place(x=378,
                                   y=223,
                            )
                           
    def hotcoffee(root):
        hotCoffeetxt = Image.open("IconTBO\HotCoffee.png")
        hotcoffeeimg = CTkImage(light_image=hotCoffeetxt, size=(130.99, 130))
        hotIconLabel = CTkLabel(master=root,
                           text='',
                           image=hotcoffeeimg,
                           fg_color="#FFE0BC",
                           ).place(x=129,
                                   y=223,
                            )
                           
    def cupImge(root):
        cupImge = Image.open("IconTBO\Cup3Size.png")
        cupSizeimg = CTkImage(light_image=cupImge, size=(238, 300))
        cupSizeLabel = CTkLabel(master=root,
                           text='',
                           image=cupSizeimg,
                           fg_color="#FFE0BC"
                           ).place(x=35,
                                   y=200,
                            )
                           
    def varianimg(root):
        varianImge = Image.open("IconTBO\Coffeevariation.png")
        variationimg = CTkImage(light_image=varianImge, size=(238, 242))
        varianLabel = CTkLabel(master=root,
                           text='',
                           image=variationimg,
                           fg_color="#FFE0BC"
                           ).place(x=42,
                                   y=208,
                            )
                           
    def paymentimg(root):
        paymentImge = Image.open("IconTBO\Payment Image.png")
        paymentimg = CTkImage(light_image=paymentImge, size=(240, 230))
        paymentLabel = CTkLabel(master=root,
                           text='',
                           image=paymentimg,
                           fg_color="#FFE0BC"
                           ).place(x=20,
                                   y=220,
                            )
                           
    def toppingimg(root):
        toppingImge = Image.open("IconTBO\ToppingsImg.png")
        toppingimg = CTkImage(light_image=toppingImge, size=(240, 190.77))
        toppingLabel = CTkLabel(master=root,
                           text='',
                           image=toppingimg,
                           fg_color="#FFE0BC"
                           ).place(x=41,
                                   y=227,
                            )
                             
    def cuptext(root):
        cuptext = Image.open("IconTBO\CupSize.png")
        cupimg = CTkImage(light_image=cuptext, size=(205, 70))
        cpLabel = CTkLabel(master=root,
                           text='',
                           image=cupimg,
                           ).place(x=35, y=158,
                            )
    
    def temperaturetext(root):
        temperatureText = Image.open("IconTBO\Hot or Ice.png")
        temperatureImg = CTkImage(light_image=temperatureText, size=(205, 70))
        cpLabel = CTkLabel(master=root,
                           text='',
                           fg_color="#FFE0BC" ,
                           image=temperatureImg,
                           ).place(x=198, y=143,
                            )
    
    def lvlIcetext(root):
        lvlIceText = Image.open("IconTBO\IceLevel.png")
        lvlIceImg = CTkImage(light_image=lvlIceText, size=(205, 70))
        lvlIceLabel = CTkLabel(master=root,
                           text='',
                           image=lvlIceImg,
                           ).place(x=35, y=158,
                            )
                           
    def lvlSugartext(root):
        lvlSugarText = Image.open("IconTBO\SugarLevel.png")
        lvlSugarImg = CTkImage(light_image=lvlSugarText, size=(205, 70))
        lvlIceLabel = CTkLabel(master=root,
                           text='',
                           image=lvlSugarImg,
                           ).place(x=35, y=158,
                            )
    
    def variantext(root):
        varianText = Image.open("IconTBO\Variation.png")
        varianImg = CTkImage(light_image=varianText, size=(245, 70))
        varianLabel = CTkLabel(master=root,
                           text='',
                           image=varianImg,
                           ).place(x=35, y=135,
                            )
    
    def toppingtext(root):
        toppingText = Image.open("IconTBO\Toppings.png")
        toppingImg = CTkImage(light_image=toppingText, size=(245, 70))
        toppingLabel = CTkLabel(master=root,
                           text='',
                           image=toppingImg,
                           ).place(x=35, y=135,
                            )
    
    def paymenttext(root):
        paymentText = Image.open("IconTBO\Payment.png")
        paymentImg = CTkImage(light_image=paymentText, size=(245, 70))
        paymentLabel = CTkLabel(master=root,
                           text='',
                           image=paymentImg,
                           ).place(x=35, y=135,
                            )
    
    def whenconfirmtext(root):
        whenconfirmText = Image.open("IconTBO\Ingin_menambah_pesanan.png")
        whenconfirmImg = CTkImage(light_image=whenconfirmText, size=(350, 85))
        whenconfirmLabel = CTkLabel(master=root,
                           text='',
                           image=whenconfirmImg,
                           ).place(x=30, y=135,
                            )
                           
    def Secondconfirmtext(root):
        secondconfirmText = Image.open("IconTBO\Second confirm.png")
        secondconfirmImg = CTkImage(light_image=secondconfirmText, size=(300, 125))
        secondconfirmLabel = CTkLabel(master=root,
                           text='',
                           image=secondconfirmImg,
                           ).place(x=26, y=232,
                            )

#untuk text header
def headertext(root):
    textImg = Image.open("kreasiKopi2.png")
    tImg = CTkImage(light_image=textImg, size=(155, 74))
    ImgLabel = CTkLabel(master=root,
                        text='',
                        fg_color="#A8661E",
                        bg_color="#A8661E",
                        image=tImg,
                        ).place(x=21, y=23,
                            
                        )

def printingstruk(root):
    global string
    struktemp = ''
    isiStruk = None
    hargatotal = 0
    
    struktemp = string + '9'
    isiStruk = vm.transition(struktemp)
    hargatotal = vm.Totalharga()
    siStruk = ''
    if isiStruk is not None:
            pembayaran = ''
            siStruk += f"======================= Struk Pesanan ======================\n"
            for pesanan in isiStruk:
                if isinstance(pesanan, itemData):
                    if pesanan.varian:
                        siStruk += f" Rasa: {pesanan.varian}\n"
                    else:
                        siStruk += f''
                    if pesanan.cupsize:
                        siStruk += f" Ukuran: {pesanan.cupsize}\n"
                    else:
                        siStruk += f''
                    if pesanan.temperaturecoffee or pesanan.levelIce:
                        siStruk += f" Temperatur: {pesanan.temperaturecoffee} | {pesanan.levelIce if pesanan.temperaturecoffee == 'Ice' else 'Hot Coffee'}\n"
                    else:
                        siStruk += f''
                    if pesanan.levelSugar:
                        siStruk += f" Gula: {pesanan.levelSugar}\n"
                    else:
                        siStruk += f''
                    if pesanan.topping:
                        siStruk += f" Topping: {pesanan.topping}\n"
                    else:
                        siStruk += f''
                    pembayaran = pesanan.payment
                    siStruk += "\n"
            siStruk += f" Pembayaran: {pembayaran}\n\nHarga Total Pesanan: {hargatotal}\n"
            siStruk += f"=============================================================="
    else:
        print("Error")
    text_widget = CTkTextbox(master=root, 
                             width=492, 
                             height=252,
                             corner_radius=18,
                             fg_color='#FFCC6D', 
                             text_color='white',
                        )
    text_widget.insert("1.0", siStruk)
    text_widget.configure(state="disabled")
    text_widget.place(x=58, y=148) 

#untuk clear window
def clear_window(root):
        for widget in root.winfo_children():
            widget.destroy()
            
#Start page
def startpage(root, current_menu, size):
    global string
    global counter
    global counter
    string = ''
    counter = 0
    counter2 = 1
    clear_window(root)
    dualima(root, size)
    Images.headerbg(root)
    headertext(root)
    Images.gambarStart(root)
    mulaiPesanopen = Image.open("IconTBO\mulaiPesan.png")
    mulaiPesanImg = CTkImage(light_image=mulaiPesanopen, size=(261, 97))
    btn_strt = CTkButton(
    root,
    text='', 
    image= mulaiPesanImg,
    command=lambda: selectcup(root, current_menu, size),
    fg_color="transparent",
    hover=DISABLED
    )
    btn_strt.tkraise()
    btn_strt.place(x=177, y=153,
                )

def pesananlain(root, current_menu, size):
    startpage(root, current_menu, size)

#untuk memasukan nilai ke string
def cupSize(invalue):
    global string
    string += invalue
    current_menu= 'cupSize'

def temperature(invalue):
    global string
    string += invalue
    current_menu= 'temperature'
    
def icelevel(invalue):
    global string
    string += invalue
    current_menu= 'iceLevel'
    
def sugarlevel(invalue):
    global string
    string += invalue
    current_menu= 'sugarlevel'
    
def varian(invalue):
    global string
    string += invalue
    current_menu = 'variation'
    
def topping(invalue):
    global string 
    string += invalue
    current_menu = 'topping'
    
def confirm(invalue):
    global string
    string += invalue
    current_menu = '24'
    
def payment(invalue):
    global string
    string += invalue
    current_menu = 'payment'

def finalconfirm(invalue):
    global string
    string += invalue
    current_menu = 'lastconfirm'
    
def dualima(root, invalue):
    global string
    string += invalue
    for value in string:
        if value in ['!', '']:
            clear_window(root)
            current_menu = 'start'
            string = ''
        else:
            current_menu = '25'
            
def tambah(invalue):
    global string
    if invalue in ['!','']:
        invalue = ''
        string = ''
    else:   
        string += invalue

        current_menu = 'cupSize'

def finalconfirm(invalue):
    global string
    string += invalue

#untuk mengganti tampilan
#cup
def selectcup(root, current_menu, size):
    global counter
    global counter2
    counter += 1
    counter2 = 1
    clear_window(root)
    Images.headerbg(root)
    Images.cupImge(root)
    Images.cuptext(root)
    headertext(root)
    tambah(size)
    smallbtnimg = Image.open("IconTBO\small.png")
    smalltextimg = CTkImage(light_image=smallbtnimg, size=(185, 47))
    smallbtn = CTkButton(master=root, 
                        text='', 
                        image=smalltextimg,
                        command=lambda size='a': selecttemper(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=362,
                        )         
    mediumbtnimg = Image.open("IconTBO\medium.png")
    mediumtxtimg = CTkImage(light_image=mediumbtnimg, size=(185, 47))
    mediumbtn = CTkButton(master=root, 
                        text='', 
                        image=mediumtxtimg,
                        command=lambda size='b': selecttemper(root, current_menu, size),
                        fg_color="transparent",
                        hover= DISABLED,
                    ).place(x=350, y=308,
                        ) 
    bigbtnimg = Image.open("IconTBO\large.png")
    bigtxtimg = CTkImage(light_image=bigbtnimg, size=(185, 47))
    bigbtn = CTkButton(master=root, 
                        text='', 
                        image=bigtxtimg,
                        command=lambda size='c': selecttemper(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=254,
                        ) 
                        
    root.mainloop()

#temperature    
def selecttemper(root, current_menu, size):
    clear_window(root)
    Images.temperaturetext(root)
    Images.icecoffee(root)
    Images.hotcoffee(root)
    Images.headerbg(root)
    headertext(root)
    cupSize(size)
    hotbtnimg = Image.open("IconTBO\hot.png")
    hottxtimg = CTkImage(light_image=hotbtnimg, size=(210, 35))
    hotbtn = CTkButton(master=root, 
                        text='', 
                        image=hottxtimg,
                        command=lambda size='d': selectsugar(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=89, y=363,
                        ) 
    icetxtbtnimg = Image.open("IconTBO\icetxt.png") 
    icetextimg = CTkImage(light_image=icetxtbtnimg, size=(210, 35))
    icebtn = CTkButton(master=root, 
                        text='', 
                        image=icetextimg,
                        command=lambda size='e': selectice(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=320, y=363,
                        ) 

#sugar
def selectsugar(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.lvlSugartext(root)
    Images.sugarIcon(root)
    headertext(root)
    sugarlevel(size)
    nosugarbtnimg = Image.open("IconTBO\pNoSugar.png")
    nosugartxtimg = CTkImage(light_image=nosugarbtnimg, size=(163, 34))
    nosugarbtn = CTkButton(master=root, 
                        text='', 
                        image=nosugartxtimg,
                        command=lambda size='i': selectvariant(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=399, 
                        ) 
    lesssugarbtnimg = Image.open("IconTBO\lessSugar.png")
    lesssugartxtimg = CTkImage(light_image=lesssugarbtnimg, size=(163, 34))                
    lesssugarbtn = CTkButton(master=root, 
                        text='', 
                        image=lesssugartxtimg,
                        command=lambda size='j': selectvariant(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=343,
                        )
    normalsugarimg = Image.open("IconTBO\pNormalSugar.png")
    normalsugartxtimg = CTkImage(light_image=normalsugarimg, size=(163, 34))                
    normalsugarbtn = CTkButton(master=root, 
                        text='', 
                        image= normalsugartxtimg,
                        command=lambda size='k': selectvariant(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=287,
                        )
    extrasugarimg = Image.open("IconTBO\extraSugar.png")
    extrasugartxtimg = CTkImage(light_image=extrasugarimg, size=(163, 34))                
    extrasugarbtn = CTkButton(master=root, 
                        text='', 
                        image=extrasugartxtimg,
                        command=lambda size='l': selectvariant(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=231,
                        )

#Icelevel
def selectice(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.lvlIcetext(root)
    Images.iceIcon(root)
    headertext(root)
    icelevel(size)
    lessiceimg = Image.open("IconTBO\lessIce.png")
    lessicetxtimg = CTkImage(light_image=lessiceimg, size=(163, 34))
    lessicebtn = CTkButton(master=root, 
                        text='', 
                        image=lessicetxtimg,
                        command=lambda size='f': selectsugar(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=362, 
                        ) 
    normaliceimg = Image.open("IconTBO\pnormalice.png")
    normalicetxtimg = CTkImage(light_image=normaliceimg, size=(163, 34))                
    normalicebtn = CTkButton(master=root, 
                        text='', 
                        image=normalicetxtimg,
                        command=lambda size='g': selectsugar(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=306,
                        )
    extraiceimg = Image.open("IconTBO\extraIce.png")
    extraicetxtimg = CTkImage(light_image=extraiceimg, size=(163, 34))
    extraicebtn = CTkButton(master=root, 
                        text='', 
                        image=extraicetxtimg,
                        command=lambda size='h': selectsugar(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=250,
                        )

#Varian
def selectvariant(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.variantext(root)
    Images.varianimg(root)
    headertext(root)
    varian(size)
    dolceltteimg = Image.open("IconTBO\dolceLatte.png")
    dolcelttetxtimg = CTkImage(light_image=dolceltteimg, size=(233, 43.65))
    dolcelttebtn = CTkButton(master=root, 
                        text='', 
                        image=dolcelttetxtimg,
                        command=lambda size='m': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=191,
                        ) 
    caramachiimg = Image.open("IconTBO\caramelMacchiato.png")
    caramachitxtimg = CTkImage(light_image=caramachiimg, size=(233, 41))
    caramachiabtn = CTkButton(master=root, 
                        text='', 
                        image=caramachitxtimg,
                        command=lambda size='n': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=239,
                        )
    hazelatteimg = Image.open("IconTBO\hazelnutLatte.png")
    hazelattetxtimg = CTkImage(light_image=hazelatteimg, size=(233, 41))
    hazelattebtn = CTkButton(master=root, 
                        text='', 
                        image=hazelattetxtimg,
                        command=lambda size='o': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=284, 
                        )
    americanoimg = Image.open("IconTBO\pamericano.png")
    americanotxtimg = CTkImage(light_image=americanoimg, size=(233, 41))
    americanbtn = CTkButton(master=root, 
                        text='', 
                        image=americanotxtimg,
                        command=lambda size='p': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=329,
                        )
    moccaimg = Image.open("IconTBO\moccacino.png")
    moccatxtimg = CTkImage(light_image=moccaimg, size=(233, 41))
    moccabtn = CTkButton(master=root, 
                        text='', 
                        image=moccatxtimg,
                        command=lambda size='q': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=374,
                        )
    cappuimg = Image.open("IconTBO\cappucino.png")
    capputxtimg = CTkImage(light_image=cappuimg, size=(233, 41))
    cappubtn = CTkButton(master=root, 
                        text='', 
                        image=capputxtimg,
                        command=lambda size='r': selecttopping(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=419,
                        )
    
#Toppings
def selecttopping(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.toppingtext(root)
    Images.toppingimg(root)
    headertext(root)
    topping(size)
    pearlimg = Image.open("IconTBO\pearl.png")
    pearltxtimg = CTkImage(light_image=pearlimg, size=(233, 48.65))
    pearlbtn = CTkButton(master=root, 
                        text='', 
                        image=pearltxtimg,
                        command=lambda size='s': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=202,
                        ) 
    grassjelimg = Image.open("IconTBO\grassJelly.png")
    grassjeltxtimg = CTkImage(light_image=grassjelimg, size=(233, 43))
    grassjelbtn = CTkButton(master=root, 
                        text='', 
                        image=grassjeltxtimg,
                        command=lambda size='t': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=253,
                        )
    whipcrmimg = Image.open("IconTBO\whipCream.png")
    whipcrmtxtimg = CTkImage(light_image=whipcrmimg, size=(233, 41))                
    whipcrmbtn = CTkButton(master=root, 
                        text='', 
                        image=whipcrmtxtimg,
                        command=lambda size='u': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=300,
                        )
    carasauceimg = Image.open("IconTBO\caramelSauce.png")
    carasaucetxtimg = CTkImage(light_image=carasauceimg, size=(233, 42))
    carasaucebtn = CTkButton(master=root, 
                        text='', 
                        image=carasaucetxtimg,
                        command=lambda size='v': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=344, 
                        )
    notopimg = Image.open("IconTBO\pnoTopping.png")
    notoptxtimg = CTkImage(light_image=notopimg, size=(200, 35))
    notopbtn = CTkButton(master=root, 
                        text='', 
                        image=notoptxtimg,
                        command=lambda size='w': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=396,
                        )

#state 24
def transit24(root, current_menu, size):
    topping(size)
    size = '8'
    firstconfirm(root, current_menu, size)
                    
#first confirm / state 24
def firstconfirm(root, current_menu, size):
    global counter
    global counter2
    clear_window(root)
    Images.headerbg(root)
    Images.whenconfirmtext(root)
    Images.womenwithcoffee(root)
    headertext(root)
    confirm(size)
    tambahbtnimg = Image.open("IconTBO\ptambahPesanan.png")
    tambahtxtimg = CTkImage(light_image=tambahbtnimg, size=(212, 35))
    tambahbtn = CTkButton(master=root, 
                        text='', 
                        image=tambahtxtimg,
                        command=lambda size='y': selectcup(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=278,
                        )
    if counter == 0:
        pembayaranbtnimg = Image.open("IconTBO\lanjut ke pembayaran.png")
        pembayarantxtimg = CTkImage(light_image=pembayaranbtnimg, size=(217, 35))
        pembayaranbtn = CTkButton(master=root, 
                            text='', 
                            image=pembayarantxtimg,
                            state=DISABLED,
                            command=lambda size='x': selectpayment(root, current_menu, size),
                            fg_color="transparent",
                            hover=DISABLED,
                        ).place(x=350, y=323
                            )
    else:
        pembayaranbtnimg = Image.open("IconTBO\lanjut ke pembayaran.png")
        pembayarantxtimg = CTkImage(light_image=pembayaranbtnimg, size=(217, 35))
        pembayaranbtn = CTkButton(master=root, 
                            text='', 
                            image=pembayarantxtimg,
                            state=NORMAL,
                            command=lambda size='x': selectpayment(root, current_menu, size),
                            fg_color="transparent",
                            hover=DISABLED,
                        ).place(x=350, y=323
                            )
    if counter2 == 0:
        batalbtnimg = Image.open("IconTBO\pbatalkan pesanan ini.png")
        bataltxtimg = CTkImage(light_image=batalbtnimg, size=(217, 35))                    
        batalbtn = CTkButton(master=root, 
                        text='', 
                        image=bataltxtimg,
                        state = DISABLED,
                        command=lambda size='z': secondconfirm(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=368,
                        ) 
    else:
         batalbtnimg = Image.open("IconTBO\pbatalkan pesanan ini.png")
         bataltxtimg = CTkImage(light_image=batalbtnimg, size=(217, 35))                    
         batalbtn = CTkButton(master=root, 
                        text='', 
                        image=bataltxtimg,
                        state = NORMAL,
                        command=lambda size='z': secondconfirm(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=368,
                        )                  
                    
#25
def secondconfirm(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.Secondconfirmtext(root)
    headertext(root)
    confirm(size)
    jadibtnimg = Image.open("IconTBO\konfirmasi.png")
    jaditxtimg = CTkImage(light_image=jadibtnimg, size=(200, 35))
    jadibtlbtn = CTkButton(master=root, 
                        text='', 
                        image=jaditxtimg,
                        command=lambda size='A': transitbatal(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=222,
                        ) 
    cancelbtnimg = Image.open("IconTBO\pbatal200px.png")
    canceltxtimg = CTkImage(light_image=cancelbtnimg, size=(200, 35))                    
    cancelbtn = CTkButton(master=root, 
                        text='', 
                        image=canceltxtimg,
                        command=lambda size='B': firstconfirm(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=270,
                        )
    resetallbtnimg = Image.open("IconTBO\pbatalPesan.png")
    resetalltxtimg = CTkImage(light_image=resetallbtnimg, size=(200, 35))                
    resetallbtn = CTkButton(master=root, 
                        text='', 
                        image=resetalltxtimg,
                        command=lambda size='!': pesananlain(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=318,
                        )

def transitbatal(root, current_menu, size):
    global counter
    global counter2
    if size =='A':
        counter2 -= 1
        counter -= 1
    firstconfirm(root, current_menu, size)
    
#Payment Method
def selectpayment(root, current_menu, size):
    clear_window(root)
    Images.headerbg(root)
    Images.paymentimg(root)
    Images.paymenttext(root)
    headertext(root)
    payment(size)
    qrisbtnimg = Image.open("IconTBO\qris.png")
    qristxtimg = CTkImage(light_image=qrisbtnimg, size=(200, 35))
    qrisbtn = CTkButton(master=root, 
                        text='', 
                        image=qristxtimg,
                        command=lambda size='0': lastconfirm(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=285,
                        ) 
    cashbtnimg = Image.open("IconTBO\cash.png")
    cashtxtimg = CTkImage(light_image=cashbtnimg, size=(205, 35))                    
    cashbtn = CTkButton(master=root, 
                        text='', 
                        image=cashtxtimg,
                        command=lambda size='1': lastconfirm(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=350, y=330,
                        )
                    
#Last Confirm
def lastconfirm(root, current_menu, size):
    clear_window(root)
    payment(size)
    Images.headerbg(root)
    printingstruk(root)
    headertext(root)
    confirmbtnimg = Image.open("IconTBO\cetakStruk.png")
    confirmtxtimg = CTkImage(light_image=confirmbtnimg, size=(240, 35))
    confirmbtn = CTkButton(master=root, 
                        text='', 
                        image=confirmtxtimg,
                        command=lambda size='9': cetakstruk(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=58, y=415,
                        ) 
    buungbtnimg = Image.open("IconTBO\pbatal240px.png")
    buungtxtimg = CTkImage(light_image=buungbtnimg, size=(240, 35))
    buungbtn = CTkButton(master=root, 
                        text='', 
                        image=buungtxtimg,
                        command=lambda size='': transit24(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=310, y=415,
                        )
                    
#Cetak Struk
def cetakstruk(root, current_menu, size):
    global string
    clear_window(root)
    Images.thxtext(root)
    Images.headerbg(root)
    headertext(root)
    finalconfirm(size)
    current_menu = 'end'
    order = string
    if current_menu == 'end':      
        pesanan = vm.transition(order)
        hargatotal = vm.Totalharga()
        if pesanan is not None:
            if hargatotal != 0:
                pembayaran = ''
                print(f"=======================!Struk Pesanan!======================\n")
                for pesanan in pesanan:
                    if isinstance(pesanan, itemData):
                        print(f" Rasa: {pesanan.varian}") if pesanan.varian else ""
                        print(f" Ukuran: {pesanan.cupsize}") if pesanan.cupsize else ""
                        print(f" Temperatur: ", f"{pesanan.temperaturecoffee} | {pesanan.levelIce if pesanan.temperaturecoffee == 'Ice' else 'Hot Coffee'}") if pesanan.temperaturecoffee or pesanan.levelIce else ""
                        print(f" Gula: {pesanan.levelSugar}") if pesanan.levelSugar else ""
                        print(f" Topping: {pesanan.topping}") if pesanan.topping else ""
                        pembayaran = pesanan.payment
                        print("")
                print(f" Pembayaran: {pembayaran}\n\nHarga Total Pesanan: {hargatotal}\n")
                print(f"==============================================================")
            elif hargatotal == 0:
                print(f"==============================================================\n")
                print("\t\t\t\t\t\t\tDITUNGGU PESANANNYA DI LAIN HARI")
                print(f"\n==============================================================\n")       
        else:
            print(f"============================Error!============================\n")
            print("\t\t\tInputan salah!\n")
            print(f"==============================================================\n")
    else:
        string = ''
        print(f"!Error!")
    closebtnimg =Image.open("IconTBO\kembali ke menu mulai.png")
    closetxtimg = CTkImage(light_image=closebtnimg, size=(420, 35))            
    closebtn = CTkButton(master=root, 
                        text='', 
                        image=closetxtimg,
                        command=lambda size='': pesananlain(root, current_menu, size),
                        fg_color="transparent",
                        hover=DISABLED,
                    ).place(x=89, y=418,
                        )
                    