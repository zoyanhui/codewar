# import re
# def decodeMorse(morseCode):
    # allmorse = re.findall('([\.\-]+)(\s*)', morseCode)
    # decrpt = ""
    # for morse, space in allmorse:
    #     if len(space) <= 1:
    #         decrpt += MORSE_CODE[morse]
    #     else:
    #         decrpt += MORSE_CODE[morse] + ' '
    # return decrpt.strip()
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    dwords = []
    for word in morseCode.split("   "):
        dword = ""
        for char in word.split(" "):
            dword += MORSE_CODE[char]
        dwords.append(dword)
    return ' '.join(dwords)


    
