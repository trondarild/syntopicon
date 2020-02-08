#
# various common snippets
#

class RomanToDecimal:
    def __init__(self):
        self.num = 0
        self.rom_val = {'i': 1,
                        'v': 5,
                        'x': 10,
                        'l': 50,
                        'c': 100,
                        'd': 500,
                        'm': 1000}

    def calc(self):
        int_val = 0
        for i in range(len(self.num)):
            if i > 0 and self.rom_val[self.num[i]] \
                         > self.rom_val[self.num[i-1]]:
                int_val += self.rom_val[self.num[i]] \
                           - 2 * self.rom_val[self.num[i-1]]
            else:
                int_val += self.rom_val[self.num[i]]
        return int_val

def decToRoman(num,s,decs,romans):
	"""
	  convert a Decimal number to Roman numeral recursively
	  num: the decimal number
	  s: the roman numerial string
	  decs: current list of decimal denomination
	  romans: current list of roman denomination
	"""
	if decs:
	  if (num < decs[0]):
	    # deal with the rest denomination
	    return decToRoman(num,s,decs[1:],romans[1:])		  
	  else:
	    # deduce this denomation till num<desc[0]
	    return decToRoman(num-decs[0],s+romans[0],decs,romans)	  
	else:
	  # we run out of denomination, we are done 
	  return s

def to_roman(decimal):
	decimalDens=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
	romanDens_upper=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
	romanDens_lower=["m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"]

	return decToRoman(decimal, '', decimalDens, romanDens_lower)
