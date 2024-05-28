class FakeData:
    '''Generate Fake Supermarket Data'''
    __tax = 5.0
    def __init__(self) -> None:
        from faker import Faker
        from datetime import datetime
        self.faker = Faker(locale='en_IN')
        self.datetime = datetime
        self.City = None
        self.Customer_Type = None
        self.Gender = None
        self.Product_Line = None
        self.Unit_Price = None
        self.Quantity = None
        self.Tax = None
        self.Total = None
        self.DT = None
        self.Payment_Mode = None
        return None
    
    def CityName(self) -> None:
        '''Name : City'''
        self.City = self.faker.random_element(['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bengaluru', 'Lucknow', 'Hyderadabad'])
        return None
    
    def CustomerType(self) -> None:
        '''Name : Customer_Type'''
        self.Customer_Type = self.faker.random_element(['Normal', 'Member'])
        return None
    
    def GenderType(self) -> None:
        '''Name : Gender'''
        self.Gender = self.faker.passport_gender()
        return None
    
    def ProductLine(self) -> None:
        '''Name : Product_Line'''
        self.Product_Line = self.faker.random_element(['Health and beauty', 'Electronic accessories', 'Home and lifestyle', 'Sports and travel', 'Food and beverages', 'Fashion accessories'])
        return None
    
    def UnitPrice(self) -> None:
        '''Name : Unit_Price'''
        flag = True
        while flag:
            price = round(float(self.faker.pricetag().lstrip('$').replace(',','')) % 100, 2)
            if price >= 10 and price <= 100:
                self.Unit_Price = price
                return None
    
    def ProductQuantity(self) -> None:
        '''Name : Quantity'''
        self.Quantity = self.faker.random_digit_not_null()
        return None
    
    def TaxProduct(self) -> None:
        '''Name : Tax'''
        self.Tax = round((self.Unit_Price * self.Quantity) * self.__tax/100, 2)
        return None

    def TotalCost(self) -> None:
        '''Name : Total'''
        self.Total = round((self.Unit_Price * self.Quantity) + ((self.Unit_Price * self.Quantity) * self.__tax/100), 2)
        return None
    
    def DateTime(self) -> None:
        '''Name : Date_Time'''
        t = self.faker.time()
        d = self.datetime.strftime(self.datetime.now(), '%Y-%m-%d')
        self.DT = d +' '+ t
        return None
    
    def PaymentMode(self) -> None:
        '''Name : Payment_Mode'''
        self.Payment_Mode = self.faker.random_element(['UPI', 'Credit card', 'Cash'])
        return None

class FakeDataBuilder:
    def __init__(self) -> None:
        self.fake = FakeData()
    def addCity(self) -> object:
        self.fake.CityName()
        return self
    def addCustomerType(self) -> object:
        self.fake.CustomerType()
        return self
    def addGender(self) -> object:
        self.fake.GenderType()
        return self
    def addProductLine(self) -> object:
        self.fake.ProductLine()
        return self
    def addUnitPrice(self) -> object:
        self.fake.UnitPrice()
        return self
    def addProductQuantity(self) -> object:
        self.fake.ProductQuantity()
        return self
    def addTaxProduct(self) -> object:
        self.fake.TaxProduct()
        return self
    def addTotalCost(self) -> object:
        self.fake.TotalCost()
        return self
    def addDateTime(self) -> object:
        self.fake.DateTime()
        return self
    def addPaymentMode(self) -> object:
        self.fake.PaymentMode()
        return self
    def FetchTxn(self):
        return self.fake
