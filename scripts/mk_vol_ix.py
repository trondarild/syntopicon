#
# script for pulling out index terms for particular volumes of HC
#

# capture pre-ix: [\w \-]+, xxxii, [0-9]+

# alternative: iterate through all terms once, but for each line
# find all volumes and add to string by means of map so get a map of 
# all volumes to a string of all refs

import re
# read index list


fileobj = open('harvardclassics50_ix_mmx.txt', 'r') # open for reading
tststr = fileobj.readlines() # read all lines into array
fileobj.close()

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

def get_ixterm(term_str):
	'''
	Pull out index term of a line
	'''
	#print term_str
	retval = ''
	p = re.compile('\[\[(.+?)\]\]')
	m = p.search(term_str)
	retval += m.group(0) # group(0) takes whole pattern
	return retval

def get_pagenums_for_vol(roman_str, ix_str):
	'''
	Pull out page numbers for a given volume number
	'''
	retval = ''
	# divide string by 
	return ''



result = ''

def print_terms_for_vol(volnum, index_list):
	roman = to_roman(volnum)
	print roman
	result = 'Volume ' + str(volnum) + ':\n' 
	for line in index_list:
		if roman in line:
			#print line
			# pull out term and page numbers
			ixterm = get_ixterm(line)
			pagenums = get_pagenums_for_vol(roman, line)
			# add ixterm and pagenums to result
			result += '* ' + ixterm + ', ' + pagenums + '\n'
	# write out for volume
	print result # or write to file

def do_all_vols():
	ix_lst = []
	for i in range(1, 51):
		print_terms_for_vol(i, ix_lst)

#print_terms_for_vol(32, tststr)
dct = {}
#tst = "* [[Action ]](see also Acts, Activity) ; Demosthenes on, iii, 33; the value of, to the scholar, v, 12-15; Kant on principles of, xxxii, 345-70; two ways of,^ xxxix, 123; Longfellow on, xiii, 13 16, 131 7; Hindu doctrine of, xlv, 809-10, 813-15, 819-20, 823-4, 826, 876-8; Webster on want of, xlvii, 723; Pascal on necessity of, xlviii, 51 (131); sources of, 117 (334); and love, 423-425"
for itm in tststr:
	#print itm
	if itm[0] != '*':
		continue
	tst = itm
	term = get_ixterm(tst)
	term_lst = re.split("(([\w ]+), ([ivxl]+)),", tst) # yields quadruples
	for i in range(1, len(term_lst), 4):
		#print str(i) + ' = ' + term_lst[i]
		#print str(i+1) + ' = ' + term_lst[i+1]
		#print str(i+2) + ' = ' + term_lst[i+2]
		#print str(i+3) + ' = ' + term_lst[i+3]
		ix = term_lst[i+2]
		pre = term_lst[i+1]
		pgs = term_lst[i+3]
		prev = dct.get(ix, '')
		if not term in prev:
			prev += '\n* ' + term + ':'
		dct[ix] =  prev  + pre + ', ' + pgs
		#if ix=='iv': print dct[ix]
#print dct
rom_dec = RomanToDecimal()
for key in dct.keys():
	rom_dec.num = key
	name = 'Volume ' + str(rom_dec.calc())
	#print name

	#print dct[key]
	
	retval = '==Index==\n' + dct[key]
	retval = retval.replace('\n\n', '\n')
	if key=='li': print retval
	#fileobj = open(name + '.txt', 'w') # open for writing
	#fileobj.write(retval)
	#fileobj.close()

#print tst.split(';')