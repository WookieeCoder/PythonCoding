import math
from os import system,name

input_cal = int(input("Enter 1 for Pythagorian Calculator or Enter 2 for Newton Law of Universal Gravitaion Calculator:    "))

if input_cal == 1:

    print("Input lenghts of sides of the right triangle")
    a = int(input("Side A:  "))
    b = int(input("Side B:  "))
    system("cls")

    square_a = a ** 2
    square_b = b ** 2 
    square_combo = square_a + square_b
    square_root = math.sqrt ( square_combo )
    #Hippotonus = Sqrt ((A**2) + (B**2) )

    print("The Hippotunus of " + str(a) + " Squared " + str(b) + " Squared is " + str(square_root))

else:
    print("Please input correct Selection")

if input_cal == 2:

    m1 = float(input("Enter first planet's Mass:  "))
    m2 = float(input("Enter second planet's Mass: "))
    r = float(input("Enter Distance between planets:  "))
    system("cls")
    g = 0.00000000006674

    #cal_mass = m1 + m2
    #cal_r = r * r
    #cal_combo = cal_mass / cal_r 
    #force = g * cal_combo
    force = ( m1 * m2 ) / (r ** 2) * g
    print ("The attraction force between Planet A and Planet B is " + str( force ) )

else: 
    print("Please Input correct selection")




