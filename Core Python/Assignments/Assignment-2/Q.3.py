# 3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter the feet : '))
inches = float(input('Enter the inches : '))

meter_feet = feet * 0.305
centimeter_feet = feet * 30.48

meter_inch = inches * 0.0254
centimeter_inch = inches * 2.54

print(f'{meter_feet} meters for {feet} feets')
print(f'{centimeter_feet} centimeters for {feet} feets')

print(f'{meter_inch} meters for {inches} inches')
print(f'{centimeter_inch} centimeters for {inches} inches')