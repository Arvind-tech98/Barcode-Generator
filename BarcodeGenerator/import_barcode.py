import barcode
from barcode.writer import ImageWriter

#Define content of the barcode as a string
num = input("Enter the code to generate barcode = ")

#Get the requied barcode format
barcode_format = barcode.get_barcode_class('upc')

#Generate barcode and render as image
my_barcode = barcode_format(num, writer = ImageWriter())

#Save Barcode as PNG
my_barcode.save("generated_barcode")