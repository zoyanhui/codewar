import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test as Test

CODES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def to_base_64(string):
    if not string:
        return ""
    asc = [ord(x) for x in string]
    encoded_str = []
    i = 0
    while i + 3 <= len(asc):
        encoded_str.append(CODES[(asc[i] & 0xFC) >> 2])
        encoded_str.append(CODES[((asc[i] & 0x03) << 4) | ((asc[i+1] & 0xF0) >> 4)])
        encoded_str.append(CODES[((asc[i+1] & 0x0F) << 2) | ((asc[i+2] & 0xC0) >> 6)])
        encoded_str.append(CODES[(asc[i+2] & 0x3F)])
        i+=3
    if i == len(asc) - 2:
        encoded_str.append(CODES[(asc[i] & 0xFC) >> 2])
        encoded_str.append(CODES[((asc[i] & 0x03) << 4) | ((asc[i+1] & 0xF0) >> 4)])
        encoded_str.append(CODES[(asc[i+1] & 0x0F) <<2])
        # encoded_str.append("=")
    elif i == len(asc) - 1:
        encoded_str.append(CODES[(asc[i] & 0xFC) >> 2])
        encoded_str.append(CODES[(asc[i] & 0x03) << 4])
        # encoded_str.append("==")
    return ''.join(encoded_str)


    
def from_base_64(string):
    if not string:
        return ""
    string += '=' * (len(string) % 4)
    decoded_str = []
    i = 0
    while i+4 <= len(string):
        a, b, c, d = CODES.index(string[i]), CODES.index(string[i+1]), CODES.index(string[i+2]), CODES.index(string[i+3])
        decoded_str.append(chr((a<<2 | b >> 4) & 0xFF))
        if c < 64:
            decoded_str.append(chr((b << 4 | c >> 2) & 0xFF))
        if d < 64 :
            decoded_str.append(chr((c << 6 | d) & 0xFF))
        i+=4
    return ''.join(decoded_str)


if __name__ == '__main__':
    tests = [
          # ["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
          # ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
          # ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
          # ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
          # ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
          # ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
          # ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
          # ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
          # ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"],
          ["rWxLy- W7HtOqft,", 'cld4THktIFc3SHRPcWZ0LA']]


    for test in tests:
        result=to_base_64(test[0])
        Test.assert_equals(result, test[1])
        Test.assert_equals(from_base_64(result), test[0])

    Test.run_test()
