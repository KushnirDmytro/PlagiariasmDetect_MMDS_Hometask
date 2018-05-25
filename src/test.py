print (ord('z') - ord(' '))
print (ord('0'))
print (ord(' '))

def string_to_number (str):
    # genearating unique number for input string
    return sum( [ (ord(ch) - ord(' ')) * 40^k for k,ch in enumerate(str)] )

print(string_to_number( 'z' * 1))