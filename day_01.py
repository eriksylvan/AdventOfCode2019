# https://adventofcode.com/2019/day/1

from math import floor


inputFile = 'input/01_input'

def fuel_calculator(mass):
    '''Calculates the fuel required to launch a given module

    Parameters:
    mass (int): the mass of a module 
        
    Returns:
    int: the amunt of fuel needed to launch
    ''' 
    
    fuel=floor(mass/3)-2
    return fuel

def fuel_calculator_inc_fuel(mass):
    '''Calculates the fuel required to launch a given module, including the fuel

    Parameters:
    mass (int): the mass of a module 
        
    Returns:
    int: the total amunt of fuel needed to launch
    ''' 
    fuel_module=fuel_calculator(mass)
    extra_fuel=fuel_calculator(fuel_module)
    while(extra_fuel>0):
        fuel_module+=extra_fuel
        extra_fuel=fuel_calculator(extra_fuel)
    return fuel_module        


def day01PartOne():
    fuel=0
    rows=0
    with open(inputFile) as input:
        for line in input:
            fuel+=fuel_calculator(int(line))
            rows+=1

    print(f'Solution Day 01, Part one:\nThe total fuel requirements for all of the modules: {fuel} \n\n')

def day01PartTwo():
    fuel=0
    with open(inputFile) as input:
        for line in input:
            fuel_modul = fuel_calculator_inc_fuel(int(line))
            # fuel_modul=fuel_calculator(int(line))
            # extra_fuel=fuel_calculator(fuel_modul)
            # while(extra_fuel>0):
            #     fuel_modul+=extra_fuel
            #     extra_fuel=fuel_calculator(extra_fuel)
            fuel+=fuel_modul

    print(f'Solution Day 01, Part one:\nThe total fuel requirements for all of the modules including the fuel itself: {fuel} \n\n')  

if __name__ == "__main__":
    day01PartOne()
    day01PartTwo()
