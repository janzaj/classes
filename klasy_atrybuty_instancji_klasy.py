class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, True, True)

class Cake:

    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling

cake_01 = Cake('orange pudding', 'jelly', 'orange', 'gluten', 'orange syrup' )
cake_02 = Cake('orange biscuits', 'jelly', 'orange', 'gluten', 'orange syrup' )
cake_03 = Cake('orange pudding', 'jelly', 'orange', 'gluten', 'orange syrup' )

bakery_offer = [cake_01, cake_02,cake_03]

for i in bakery_offer:
    print('Today in our offer: {} main taste {} with additives of {}, filled with {}'.format(i.name, i.taste, i.addictions, i.filling))

