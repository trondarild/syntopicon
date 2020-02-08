#
# script for pulling out index terms for particular volumes of HC
#

# capture pre-ix: [\w \-]+, xxxii, [0-9]+

# alternative: iterate through all terms once, but for each line
# find all volumes and add to string by means of map so get a map of 
# all volumes to a string of all refs

import re
# read index list

tststr =[ 
"* [[Aaron]], references to, in Psalms, xllv, 243 (20), 2J2 (6), 281 {.2(i), 283 (16); beard of, 319 (2); and the golden calf, 444 (40-1); breastplate of, iv, 153, 388; Calvin on, xxxix, 45 ; Browning on, xlii, 1 143; Mohammed on, xlv, 922 ",
"* [[Abano]], Pietro d', xix, 205, note 35 ",
"* [[Abas]], in the Aeneid, xiii, 79, 332, 341 ",
"* [[Abascantius]], L. Satrius, ix, 379 ",
"* [[Abbagliato]], Dante on, xx, 124, and note 7 ",
"* [[Abbati]], Bocca degli, xx, 135, note 8 ",
"* [[Abaddon]], Hebrew for destruction, xliv, 116, note 13; Milton on, iv, 415 ",
"* [[Abbondio]], Don, in The Betrothed, meets the bravoes, xxi, 9-15; character and times of, 16-20; tells Perpetua his mishap, 21-4; plans to put Renzo off, 25-6; with Renzo, 27-30; owns truth to Renzo, 31-3; his fever, 34; on night of Renzo's intended marriage, 119-24, 132; ordered to go to Lucia, 385-9; with the Unnamed on the way, 390-5; returns with Lucia, 396-404; complained of, by Agnese, 415; with the Cardinal, 425-7; reprimanded by Cardinal, 433-44; during German invasion, 493-502, 508-13; at castle of Unnamed, 515-17; returns home, 517-20; with Renzo on latter's return, 569-71; anxieties abGJt marrying Renzo, 645, 651-4; consents to perform ceremony, 655-8; advises Marquis how to aici lovers, 658-61 ",
"* [[Abbott]], T. K., translator of Kant, xxxii, 315 ",
"* [[Abbott]], Capt., at Gettysburg, xliii, 409, 411 ",
"* [[Abdallah ibn Umm Maktum]], xlv, 895 note ",
"* [[Abd-el-Melik]], xvi, 310, 339 ",
"* [[Abd-es-Samad]], the shiek, xvi, 313-37 ",
"* [[Abdication]], Rousseau on right of, xxxiv, 225 ",
"* [[Abdiel]], in Paradise Lost, rebukes Satan, iv, 204; leaves the rebel 129 angels, 205-6; arrival among the faithful, 207-8; combat with Satan, 209-12; in the battle, 216; Bagehot on Milton's, xxviii, 204-5 A Becket (see Becket) ",
"* [[Abel and Cain]], Milton on, iv, 333-4; Mohammed on, xlv, loii; taken from Limbo by Christ, xx, 18; and the tree of Eve, xxxv, 196 ",
"* [[Abelard]], Carlyle on, xxv, 379 ",
"* [[Aberfeldy]], The Birks of, vi, 292-3 ",
"* [[Aberrant species]], xi, 468 ",
"* [[Abiathar]], Winthrop on, xliii, 100 ",
"* [[Abide with Me]], xlv, 580-1 ",
"* [[Abihu]], Browning on, xlii, 1143 ",
"* [[Ability]], Penn on, worldly, i, 392-5; with humility, i, 411, (247); M. Aurelius on low natural, ii, 225 (5), 246 (5), 252 (52), 255 (67), 258 (8); generally accompanied by frankness, iii, 18; certain to make itself felt, v, 297 ",
"* [[Abime]], the Saracen, xlix, 157, 158 ",
"* [[Abimelech]], and David, xliv, 184 ",
"* [[Abindarraez]], story of, xiv, 47 ",
"* [[Abishag]], reference to, xli, 499 ",
"* [[Abolitionism]], Lowell on, xxviii, 459 ",
"* [[Abortion]], Hippocrates on, xxxviii, 3 ",
"* [[Abou Ben Adhem]], xli, 893-4 ",
"* [[Abra]], Pompeia's maid, xii, 282 ",
"* [[Abradatas]], xxvii, 23 ",
"* [[Abraham]], Milton on, iv, 348-9; and Ephron, x, 32; Bunyan on, xv, 107, 240-1; and Sarah, xxxvi, 285; Paul on, 370; the covenant with, xliv, 280 (9) ; Stephen on, 442 (2-8) ; Mohammed on, xlv, 915, 921-2, 967, 993; and Ib!is, 965, note 5; Pascal on, xlviii, 167 (502), 202, 205, 207, 220 (644), 289 (822); 303; taken from Limbo, XX, 18 ",
"* [[Abraxa]], early name of Utopia, xxxvi, 182 ",
"* [[Abridgments]], Swift on, xxvii, 119 ",
"* [[Abriorix]], Gaulish chief, xii, 295 ",
"* [[Abrotonon]], mother of Themistocles, xii, 5 ",
"* [[Absalom]], and David, xx, 120; Psalm when David fled from, xliv, 148- 9; Bunyan on, xv, 313; Davia*3 grief for, 423 130 GENERAL INDEX ",
"* [[Abscesses]], antiseptic treatment of, xxxviii, 277-80 ",
"* [[Absence]], by Landor, xli, 923 ",
"* [[Absence]], Present in, xl, 321 ",
"* [[Absence]], Lovelace on, xl, 366; Confucius on, xliv, 30-1 ",
"* [[Absentees]], taxation of, x, 560 ",
"* [[Absolutes]], Plato on knowledge of, ii, 64-6; participation in, 94-6; further remarks on, 97-8; Schiller on search for, xxxii, 252; Mazzini on, xxxii, 401 ",
"* [[Absolution]], Luther on unjust, xxxvi, 289; Pascal on, xlviii, 309 (870), 316 (904-5), 322 (923) ",
"* [[Abstemiousness]], Pliny on, ix, 312-13 ",
"* [[Abstinence]], Comus on folly of, iv, 65-6; Hindu doctrine of, xlv, 876-7 ",
"* [[Abstract ideas]], Plato on, 11, 64-6; Epictetus on, 157 (109); Schiller on, xxxii, 252; Rousseau on, xxxiv, 257; Berkeley on, xxxvii, 225-6; Hume on, 436, 438 note ",
"* [[Abstract names]], Hobbes on, xxxiv, 341 ",
"* [[Abstract philosophy]], Hume on, xxxvii, 306-15, 370 ",
"* [[Abstract reasoning]], Hume on, xxxvii, 437-8, 443 ",
"* [[Abstract sciences]], Pascal on, xlviii, 58 (144) ",
"* [[Absurdities]], Hobbes on, xxxiv, 346-7 ",
"* [[Abt Vogler]], xlii, 1 1 44-8 ",
"* [[Abu Bekr]], xlv, 977, note 24 ",
"* [[Abu Ghal]], xlv, 889, note 3 ",
"* [[Abu-I-Abbas El-Khidr]], xvi, 338 ",
"* [[Abu Laheb]], xlv, 1003, note 20 ",
"* [[Abu Sufian]], xlv, 955, note 2 ",
"* [[Abuses]], Sidney on, xxvii, 38; Luther on, xxxvi, 324-5; Dryden on, xxxix, 183, note 36; Pascal on, xlviii, 318 (916) ",

]

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
			print line
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
		dct[ix] = dct.get(ix, '') + '\n* ' + term + ':' + pre + ', ' + pgs
#print dct
rom_dec = RomanToDecimal()
for key in dct.keys():
	rom_dec.num = key
	print '\n\nVolume ' + str(rom_dec.calc())
	print dct[key]

#print tst.split(';')