import re

from farayand.parking import *

cars_list = [{'name': 'pride', 'model': 'sd2', 'plate': '13t123_iran88', 'color': 'white'},
{'name': 'pego', 'model': 'sam3', 'plate': '12i526_iran33', 'color': 'red'}]



print(re.match(f"Name car: {name:>10} Model: {model:>10}  Plate: {plate:>25} Color: {color:>5}" , "Name car: pride      Model: sam3      plate: 12i526  Color: white"))