#Python calculator script to help with physics exercises


from decimal import *
import math
getcontext().prec = 3   #setting presicion of scientific notation


#defining classes
class wave:

    def __init__(self, wavelength, ni, Ef):
        self.wavelength = wavelength
        self.ni = ni
        self.Ef = Ef
    def input_length(self, wavelength):
        self.wavelength = Decimal(wavelength)
    def input_ni(self, ni):
        self.ni = Decimal(ni)
    def input_Ef(self, Ef):
        self.Ef = Decimal(Ef)

class metal:

    def __init__(self, lambdazero, nizero, W):
        self.lambdazero = lambdazero
        self.nizero = nizero
        self.W = W
    def input_lambdazero(self, lambdazero):
        self.lambdazero = Decimal(lambdazero)
    def input_nizero(self, nizero):
        self.nizero = Decimal(nizero)
    def input_W(self, W):
        self.W = Decimal(W)

class electron:

    def __init__(self, Ek, v):
        self.Ek = Ek
        self.v = v
    
    def input_Ek(self, Ek):
        self.Ek = Decimal(Ek)
    def input_v(self, v):
        self.v = Decimal(v)

        
#initializing our objects
        
ourwave = wave(0, 0, 0)
plate = metal(0, 0, 0)
photoelectron = electron(0, 0)




#variables
nizero = 0
lambdazero = 0
ni = 0
wavelength = 0
Ef = 0
Ek = 0
W = 0



#constants
h = Decimal("6.63e-34")
c = Decimal("3e+8")
m = Decimal("9.11e-31")
eV = Decimal("1.602e-19")


def countEf():
    if ourwave.ni != 0:
        ourwave.Ef = ourwave.ni*h
    elif ourwave.wavelength != 0:
        ourwave.Ef = h * c / ourwave.wavelength
    elif photoelectron.Ek != 0 and plate.W != 0:
        ourwave.Ef = photoelectron.Ek + plate.W
    

def countW():

    if plate.nizero != 0:
        plate.W = plate.nizero * h
    elif plate.lambdazero != 0:
        plate.W = h * c / plate.lambdazero
    elif photoelectron.Ek != 0 and ourwave.Ef != 0:
        plate.W = ourwave.Ef - photoelectron.Ek   
    

def countEk():   

    if ourwave.Ef >= plate.W and ourwave.Ef != 0 and plate.W != 0:
        photoelectron.Ek = ourwave.Ef - plate.W
        
    elif photoelectron.v != 0:
        photoelectron.Ek = m * photoelectron.v * photoelectron.v / 2


def countV():

    if photoelectron.Ek != 0:
        photoelectron.v = math.sqrt(2*photoelectron.Ek/m)
    

def countnizero():

    if plate.W != 0:
        plate.nizero = plate.W/h
    elif plate.lambdazero != 0:
        plate.nizero = c/plate.lambdazero

def countlambdazero():

    if plate.W != 0:
        plate.lambdazero = h*c/plate.W
    elif plate.nizero != 0:
        plate.lambdazero = c/plate.nizero
    

def countni():

    if ourwave.wavelength != 0:
        ourwave.ni = c / ourwave.wavelength
    elif ourwave.Ef != 0:
        ourwave.ni = ourwave.Ef / h


def countwavelength():

    if ourwave.ni != 0:
        ourwave.wavelength = c / ourwave.ni
    elif ourwave.Ef != 0:
        ourwave.wavelength = h * c / ourwave.Ef
    

print("Welcome to SimpleWavez!")

def choiceoption():
    
    print("\nAvailable options:")
    print("1. Input data")
    print("2. Output data")
    print("3. Exit the program")
    choice = int(input("What is your choice? "))
    return choice



#converts number from 6.5e+19 to 6.5 x 10^19 strings

def converter(number):          
    number = str(number)
    location_of_e = str(number).find('E')
    location_of_plus = str(number).find('+')
    location_of_minus = str(number).find('-')
    length = len(str(number))
    converted =''
    if location_of_e != -1:
        a = number[0:location_of_e]
    else:
        converted = number

    b = number[location_of_e+1:]
    b = b.strip('+')
    

    if converted != number:
        converted = a + ' x 10^' + b
        
    return converted
    
    

def inputdata():
    print("_________________________________________") 
    print("Data that can be read: ")
    print("1. Threshold frequency")
    print("2. Threshold wavelength")
    print("3. Wave frequency")
    print("4. Wavelength")
    print("5. Energy of the photon")
    print("6. Kinetic energy of the escaped electron")
    print("7. The work function")
    print("8. The velocity of the escaped electron")
    print("_________________________________________")

    
    selection = int(input('Choose the number corresponding to the variable you wish to change: '))
    variable = input('Input your variable: ')
    
    check_if_eV = (variable.find("eV") + variable.find("ev")) > 0          #checks whether the value is in J or in eV
                                                                    #.find returns -1 if nothing is found and if something is actually found, it returns index of  the found str
    
    check_if_nm = (variable.find("nm") + variable.find("Nm"))  > 0
    
    if check_if_eV:
        variable = Decimal(variable.strip("eV")) * eV       #converting eV into J
        
    if check_if_nm:
        variable = Decimal(variable.strip("nm")) * Decimal(1e-9)    #converting nm into m with scientific notation
    

    if selection == 1:

        plate.input_nizero(variable)
        
    elif selection == 2:

        
        plate.input_lambdazero(variable)

    elif selection == 3:

        ourwave.input_ni(variable)

    elif selection == 4:

        ourwave.input_length(variable)

    elif selection == 5:

        ourwave.input_Ef(variable)

    elif selection == 6:

        photoelectron.input_Ek(variable)

    elif selection == 7:

        plate.input_W(variable)

    elif selection == 8:

        photoelectron.input_v(variable)

def outputdata():
#Calculates and outputs all variables. First 'for' loop makes sure that everything which was possible to count with the data from input
#is calculated. The second iteration of loop counts the rest, using variables already calculated.

    i = 0
    while i != 2:                  
        
        countni()
        countwavelength()
        countnizero()
        countlambdazero()
        countEf()
        countW()
        countEk()
        countV()
        
        
        i = i + 1

    print("_________________________________________") 
    print("Threshold frequency = {} Hz".format(converter(plate.nizero)))
    print("Threshold wavelength = {} m = {} nm".format(converter(plate.lambdazero), int(plate.lambdazero/Decimal(1e-9))))
    print("Wave frequency = {} Hz".format(converter(ourwave.ni)))
    print("Wavelength = {} m = {} nm".format(converter(ourwave.wavelength), round(float(ourwave.wavelength/Decimal(1e-9)), 3)))
    print("Energy of the photon = {} J = {} eV".format(converter(ourwave.Ef), round(float(ourwave.Ef/eV), 3)))
    print("Kinetic energy of the escaped electron = {} J".format(converter(photoelectron.Ek)))
    print("The work function = {} J = {} eV".format(converter(plate.W), round(float(plate.W/eV), 3)))
    print("The velocity of the escaped electron = {} m/s = {} km/s".format(round(photoelectron.v, 3), photoelectron.v/1000, 3))
    print("_________________________________________")
        
    
        
       

def main():
    choice = choiceoption()
    if choice == 3:
        exit()
    elif choice == 1:
        inputdata()
        main()
    elif choice == 2:
        outputdata()
        main()
    else:
        print("Try again!")
        main()

main()
    
    












    








