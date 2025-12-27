#!/usr/bin/env python3.10

def sort(width: int, height: int, length: int, mass: int):
    if type(width) is not int or type(height) is not int or type(length) is not int \
        or type(mass) is not int:
        raise TypeError("All dimensions and mass must be integers.")
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be positive integers.")

    is_heavy = mass >= 20
    is_bulky = width * height * length >= 1_000_000 or \
               width >= 150 or height >= 150 or length >= 150
    
    if is_heavy and is_bulky: 
        return "REJECTED"
    elif is_heavy or is_bulky: 
        return "SPECIAL"
    return "STANDARD"

def Test(width: int, height: int, length: int, mass: int, expected: str = None):
    category = sort(width, height, length, mass)    
    print(f"Package {height}x{length}x{width}, volume: {width*height*length}, mass: {mass}kg, category: {category}")
    if category != expected and expected is not None:
        print(f"Test failed: expected {expected}, got {category}")
        raise AssertionError("Test failed")
    else:
        print("TEST PASSED")


if __name__ == "__main__":   
    Test(100, 100, 100, 20, "REJECTED")      # High volume and bulky
    Test(100, 150, 50, 20, "REJECTED")       # High width and bulky
    Test(150, 50, 100, 20, "REJECTED")       # High height and bulky
    Test(100, 150, 50, 20, "REJECTED")       # High length and bulky

    Test(100, 100, 100, 10, "SPECIAL")       # High volume not bulky
    Test(100, 150, 50, 10, "SPECIAL")        # High width not bulky
    Test(150, 50, 100, 10, "SPECIAL")        # High height not bulky
    Test(100, 150, 50, 10, "SPECIAL")        # High length not bulky

    Test(50, 50, 50, 30, "SPECIAL")          # Bulky
    Test(50, 50, 50, 10, "STANDARD")         # Standard

    try:
        Test(0, 50, 50, '10')       # Invalid width
    except TypeError as e:
        print(f"TypeError caught: TEST PASSED") 

    try:
        Test(50, -50, 50, 10)       # Invalid height
    except ValueError as e:
        print(f"ValueError caught: TEST PASSED")     
        