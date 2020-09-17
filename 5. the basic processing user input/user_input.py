# user input is something in which we can defined it by itself what is the user want to insert


def temp(value):
    if value < 20:
        return "cold"

    elif value > 20 and value < 30:
        return "pleasant"
    else:
        return "hot"


celcius = int(input("enter your temperature "))# but it is string bydefault so we need to tell it float ,int

print(temp(celcius))