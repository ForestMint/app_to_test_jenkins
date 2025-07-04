print("Hello World!")
print("Hi")


def convert_decimal_to_digital(decimal):
  value = 128
  digital = ""
  while decimal !=0 :
    if decimal >= value :
      digital += "1"
    else :
      digital +="0"
    value /=2

  return digital
