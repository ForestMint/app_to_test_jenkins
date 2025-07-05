


def convert_decimal_to_digital(decimal):

  digital = ""

  power = 7

  while power> -1:
    if decimal >= 2**power :
      digital = digital + "1"
      decimal -= 2**power
    else :
      digital = digital + "0"
    
    power -=1

  return digital

  