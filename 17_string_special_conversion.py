"""
    letter case conversion
    digital addition and subtraction
"""

a = '123456'
print(a.isdigit())  # True   # composed of pure numbers
b = 'abc'
print(b.isalpha())  # True   # composed of pure letters
c = 'bACDef%$'
print(c.swapcase())  # BacdEF%$  # letter case conversion
d = 'abCDF'
print(d.upper())  # ABCDF
print(d.lower())  # abcdf

## d.isupper()   d.islower()


## method1
def transform(string):
    new_str = ''
    for i in string:
        if i.isdigit():
            new_str += str(9 - int(i))
        else:
            new_str += i.swapcase()
    return new_str

## method2
def transform2(string):
    new_str = ''
    for i in string:
        if i.isdigit():
            new_str += str(9 - int(i))
        elif i.isupper():
            new_str += i.lower()
        elif i.islower():
            new_str += i.upper()
        else:
            new_str += i
    return new_str

if __name__ == '__main__':
    string = 'ava1241@o3#1-1231;.,,^$d'
    print(transform(string))   # AVA8758@O6#8-8768;.,,^$D
    print(transform2(string))  # AVA8758@O6#8-8768;.,,^$D


###
string = 'ava1241@o3#1-1231;.,,^$d'
result = ''.join([str(9 -int(i)) if i.isdigit() else i.swapcase() for i in string])
print(result)                     
            
