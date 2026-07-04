import math

def calculate_volume():
    print("--- Cylindrical Tank Volume Calculator ---")
    try:
        radius_input = input("Enter the radius of the tank: ")
        radius = float(radius_input)
        
        height_input = input("Enter the height of the tank: ")
        height = float(height_input)
        
        if radius < 0 or height < 0:
            print("Error: Radius and height must be non-negative values.")
            return

        volume = math.pi * (radius ** 2) * height
        print(f"The volume of the tank is: {volume:.2f}")
        
    except ValueError:
        print("Error: Please enter a valid numeric value for radius and height.")

if __name__ == "__main__":
    calculate_volume()
