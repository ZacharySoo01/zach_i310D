def calculate_volume_of_sphere(radius):
    pi = 3.14
    volume = (4 / 3) * pi * radius **3
    return volume

radius1 = 35
vol1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {vol1}")

radius2 = 45
vol2 = calculate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {vol2}")
