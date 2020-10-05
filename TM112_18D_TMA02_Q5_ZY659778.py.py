# TM112 18D TMA02 Question 5

def float_rounded_up(float):
    """Round up a float to the nearest integer"""
    integer = int(float)
    if int(float) != float: 
        integer = int(float + 1)
    return integer


# Add your code here
class floor():
    width = 100
    length = 100
    height = 10
    #width = float(input('floor width:'))
    #length = float(input('floor length:'))
    #height = float(input('floor height:'))
    floor_to_cover = (width*length*height)

class lorry():
    width = 20
    length = 50
    height = 10
    #width = float(input('lorry width:'))
    #length = float(input('lorry length:'))
    #height = float(input('lorry height:'))
    lorry_capacity = (width*length*height)


class cylinder():
    radius = 5
    length = 10
    #radius = float(input('cylinder radius:'))
    #length = float(input('cylinder length:'))
    capacity = radius*2*length


def cylinders_per_lorry(lorry,cyinder):
    cylinder_in_row = float_rounded_up(lorry.width/(cylinder.radius*2))
    cylinder_columns = float_rounded_up(lorry.length/cylinder.length)

return(cylinders_in_row*cylinder_columns)

def cylinders_required(cylinder,floor):
    return float_rounded_up(floor.floor_to_cover/cylinder.capacity)

lorries_required = (cylinders_required(cylinder,floor)/cylinders_per_lorry(lorry,cylinder))

def open():
    returnString = """To cover a floor with the below dimensions:
    each lorry can carry %d cylinders

    you will needa total of %d cylinders, in %d lorries

    """%(cylinders_per_lorry(lorry,cylinder),cylinders_required(cylinder,floor),lorries_required)
    return(returnString)

print(open())

 

