class itemData:
    def __init__(self):
        self.cupsize = ''
        self.temperaturecoffee = ''
        self.levelIce = ''
        self.varian = ''
        self.levelSugar = ''
        self.topping = ''
        self.payment = ''
        self.hargaCup = 0
        self.hargaVariant = 0
        self.hargaTopping = 0
        
    def setcup(self, cup):
        self.cupsize = cup
    
    def sethargaVar(self, hargaVar):
        self.hargaVariant = hargaVar
    
    def sethargaTopp(self, hargatopp):
        self.hargaTopping = hargatopp
    
    def sethargaCup(self, hargaCup):
        self.hargaCup = hargaCup
        
    def setTemperature(self, temperature):
        self.temperaturecoffee = temperature
        
    def setIce(self, ice):
        self.levelIce = ice
        
    def setSugar(self, sugar):
        self.levelSugar = sugar
        
    def setVarian(self, varian):
        self.varian = varian
        
    def setTopping(self, topping):
        self.topping = topping
    
    def setPayment(self, payment):
        self.payment = payment
        

class VendingMachine:
    def __init__(self):
        self.state = 'start'
        self.payment_method = None
        self.cupSize = None
        self.temperature = None
        self.iceLevel = None 
        self.sugarLevel = None
        self.toppings = None
        self.variation = None
        self.order_list = []
    
    def Totalharga(self):
        hargatotal = 0
        for pesanan in self.order_list:
            hargatotal += pesanan.hargaCup
            hargatotal += pesanan.hargaVariant
            hargatotal += pesanan.hargaTopping
        return hargatotal
    
    def resetPesanan(self):
        self.cupSize = None
        self.temperature = None
        self.iceLevel = None
        self.variation = None
        self.sugarLevel = None
        self.toppings = None 
        self.payment_method = None
        self.state = 'start'       

    def transition(self, input):
        self.order_list = []
        self.state = 'start'
        total_harga = 0
        for letter in input:
            if self.state == 'start':
                temp = itemData()
                current_order = itemData()
                
                #Untuk memilih size cup
                if letter == 'a':
                    self.cupSize = 'Small'
                    self.state = 'cupSize'
                    temp.setcup(self.cupSize)
                    temp.sethargaCup(2000)
                elif letter == 'b':
                    self.cupSize = 'Medium'
                    self.state = 'cupSize'
                    temp.setcup(self.cupSize)
                    temp.sethargaCup(4000)
                elif letter == 'c':
                    self.cupSize = 'Large'
                    self.state = 'cupSize'
                    temp.setcup(self.cupSize)
                    temp.sethargaCup(6000)
                    
                #Untuk memilih temperatur    
            elif self.state == 'cupSize':
                if letter == 'd':
                    self.temperature = 'Hot'
                    self.state = 'temperature'
                    temp.setTemperature(self.temperature)
                elif letter == 'e':
                    self.temperature = 'Ice'
                    self.state = 'iceLevel1'
                    temp.setTemperature(self.temperature)
                    
                #Untuk memilih ice level
            elif self.state == 'iceLevel1':
                if letter == 'f':
                    self.iceLevel = 'Less ice'
                    self.state = 'iceLevel'
                    temp.setIce(self.iceLevel)
                elif letter == 'g':
                    self.iceLevel = 'Normal ice'
                    self.state = 'iceLevel'
                    temp.setIce(self.iceLevel)
                elif letter == 'h':
                    self.iceLevel = 'Extra ice'
                    self.state = 'iceLevel'
                    temp.setIce(self.iceLevel)
                    
                #Untuk memilih sugar level
            elif self.state in ['temperature', 'iceLevel']:
                if letter == 'i':
                    self.sugarLevel = 'No Sugar'
                    self.state = 'sugarLevel'
                    temp.setSugar(self.sugarLevel)
                elif letter == 'j':
                    self.sugarLevel = 'Less Sugar'
                    self.state = 'sugarLevel'
                    temp.setSugar(self.sugarLevel)
                elif letter == 'k':
                    self.sugarLevel = 'Normal Sugar'
                    self.state = 'sugarLevel'
                    temp.setSugar(self.sugarLevel)
                elif letter == 'l':
                    self.sugarLevel = 'Extra Sugar'
                    self.state = 'sugarLevel'
                    temp.setSugar(self.sugarLevel)
                    
                #Untuk memilih varian kopi
            elif self.state == 'sugarLevel':
                if letter == 'm':
                    self.variation = 'Dolce Latte'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(25000)
                elif letter == 'n':
                    self.variation = 'Caramel Macchiato'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(20000)
                elif letter == 'o':
                    self.variation = 'Hazelnut Latte'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(22000)
                elif letter == 'p':
                    self.variation = 'Americano'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(24000)
                elif letter == 'q':
                    self.variation = 'Moccacino'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(22000)
                elif letter == 'r':
                    self.variation = 'Cappucino'
                    self.state = 'variation'
                    temp.setVarian(self.variation)
                    temp.sethargaVar(20000)
                    
                #Untuk memilih topping
            elif self.state == 'variation':
                if letter == 's':
                    self.toppings = 'Pearl'
                    self.state = 'toppings'
                    temp.setTopping(self.toppings)
                    temp.sethargaTopp(5000)
                elif letter == 't':
                    self.toppings = 'Grass Jelly'
                    self.state = 'toppings'
                    temp.setTopping(self.toppings)
                    temp.sethargaTopp(4000)
                elif letter == 'u':
                    self.toppings = 'Whip Cream'
                    self.state = 'toppings'
                    temp.setTopping(self.toppings)
                    temp.sethargaTopp(5000)
                elif letter == 'v':
                    self.toppings = 'Caramel Sauce'
                    self.state = 'toppings'
                    temp.setTopping(self.toppings)
                    temp.sethargaTopp(4000)
                elif letter == 'w':
                    self.toppings = 'No Topping'
                    self.state = 'toppings'
                    temp.setTopping(self.toppings)
                    temp.sethargaTopp(0)
                    
                #Ke menu konfirmasi
            elif self.state == 'toppings':
                if letter == '8':
                    self.state = '24'
                
                #Menu konfirmasi ingin ke pembayaran, tambah pesanan, atau batal pesanan
            elif self.state == '24':
                if letter == 'x':
                    self.state = '26'
                if letter == 'y':
                    current_order = temp
                    temp = None
                    self.resetPesanan()
                    self.order_list.append(current_order)
                if letter == 'z':
                    self.state = '25'
                    
                #Konfirmasi apakah jadi batal pesanan
            elif self.state == '25':
                if letter == 'A':
                    temp = itemData()
                    self.resetPesanan()
                    self.state = '24'
                if letter == 'B':
                    self.state = '24'
                if letter == 'D':
                    current_order = None
                    self.order_list = None
                    temp = None
                    self.state = 'start'
                    self.resetPesanan()
                    
                #memilih metode pembayaran
            elif self.state == '26':
                if letter == '0':
                    self.payment_method = 'QRIS'
                    self.state = '27'
                    temp.setPayment(self.payment_method)
                elif letter == '1':
                    self.payment_method = 'Cash'
                    self.state = '27'
                    temp.setPayment(self.payment_method)
                    
                #konfirmasi pesanan terakhir
            elif self.state == '27':
                if letter == '9': #untuk konfirmasi pesanan sudah sesuai
                    self.state = '28'
                    current_order = temp
                    self.order_list.append(current_order)
                    return self.order_list 
                elif letter == '8': #untuk kembali ke menu konfirmasi 2
                    self.payment_method = None
                    self.state = '24'
                else:
                    print("Salah inputan")
            else:
                return None
