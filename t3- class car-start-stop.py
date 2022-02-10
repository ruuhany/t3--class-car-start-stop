class car:
    def __init__(self,name,year): 
        self.name=name
        self.year=year
        self.color=None
        self.state=False
    
    def start_enginer(self):
        if self.state==True:
            t='ماشین قبلا روشن است'
        else:
            self.state=True 
            t='ماشین روشن شد'   
        return t

    def stop_enginer(self):
        if self.state==True:
            self.state=False 
            t='ماشین خاموش شد'
        else:
           t='ماشین روشن نیست'
        return t

car_bmw=car("BMW",2018)
car_benz=car("BENZ",2018)
car_bmw.price=3000
car_benz.color='red'

print(car_bmw.start_enginer())
print(car_bmw.stop_enginer())
print(car_benz.stop_enginer())