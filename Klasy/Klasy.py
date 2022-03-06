carBrand = 'Seat'
carModel = 'Ibiza'

carIsAirBagOK = True
carIsPainting = True
carIsMechanicOK = True

def IsCarDamaged(carIsAirBagOK, carIsPainting, carIsMechanic):
    return not (carIsAirBagOK and carIsPainting and carIsMechanic)

print(IsCarDamaged(carIsAirBagOK, carIsPainting, carIsMechanic))

# rozwiazmy problem wielu zmiennych
car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibiza',
'carIsAirBagOK' : True,
'carIsPainting' : True,
'carIsMechanicOK' : True
}

print(IsCarDamaged())

def IsCarDamaged(aCar):
    return not (aCar['carIsAirBagOK'] and aCar['carIsPainting'] and aCar['carIsMechanicOK'])

print(IsCarDamaged(car_01))

# teraz mamy jedną zmienna 

# wiele slownikow

cars = [car_01, car_02]
for c in cars:
    print('{} {} damaged = {}'.format(c['carBrand'], c['carModel'], IsDamagedCar(c)))

s_01 = {
'cake_01_taste' : 'vanilia',
'cake_01_glaze' : 'chocolade',
'cake_01_text' : 'Happy Birthday',
'cake_01_weight' : 0.7
}


s_02 = {
'cake_02_taste' : 'tee',
'cake_02_glaze' : 'lemon',
'cake_02_text' : 'Happy Python Coding',
'cake_02_weight' : 1.3
}

def show_cake_info(d):
    f = list(d.keys())
    for i in f:
        print(d[i])

#############################


