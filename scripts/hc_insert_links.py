#
# inserts clickable links to books in index list
#

from common import RomanToDecimal 
import re
import os.path

roman = RomanToDecimal()
adr_str = r'[https://archive.org/stream/harvardclassics$vol$elio#page/\1/mode/1up \1]\2'
volstr = '$vol$'
pgstr = '$pg'

exstr = "* [[Thought]], aberrations of, four principal, ii, 295 (19); \"act in fancy,'* xlv, 813; action and, Carlyle on, xv, 355; Channing on, xxviii, 333-48, 352-55; Descartes on reality of, xxxiv, 29; duty of man, xlviii, 59 (146); Hobbes on, xxxiv, 325-30, 334 359-62; Hume on limits of, xxxvii, 317-20, 322, 346; not wisdom, viii, 360; liberty of, Mill on, xxv, 218-59, 260; liberty of, Milton on, iii, 232-8; makes place, vii, 327 (5); man born for, xlviii, 417; Pascal on, 119 (339) 120 (346-8), 124 (365), 125 (370); preventing power of, 95 (259); as product of matter, xxxiv, 106-9; Rousseau on, 251-3; Schiller on courage of, xxxii, 243; sensation and, xxxvii, 316; Socrates on pure, ii, 54; study and, Confucius on, xliv, 8 (15), 55 (30); swifter than time, xviii, 324; Walton on sympathy of, xv, 341 "

fileobj = open(os.path.dirname(__file__) + '/../Harvard Classics/harvardclassics50_ix_mmx.txt', 'r') # open for reading
#f = open(os.path.dirname(__file__) + '/../data.yml')

tststr = fileobj.readlines() # read all lines into array
fileobj.close()
#tststr = tststr[0:100]
def dectostr(num, minlen):
	numstr = str(num)
	numzeros = minlen-len(numstr)
	zeros = ''
	if numzeros > 0:
		for i in range(numzeros): zeros += '0'
	return zeros + numstr

def process_term_list(ix_list):
	"""
	process each term in list:
	'xxi, 201' -> 'xxi, [https://archive.org/stream/harvardclassics21elio#page/201/mode/2up 201]'
	"""
	retval = []
	for term in ix_list:
		newterm = process_term(term)
		print newterm
		retval.append(newterm)
	return retval

def process_term(termstr):
	"""
	"""
	if not re.search(r'[ivxl]+', termstr ): return termstr
	term_lst = re.split(" ([ivxl]+),", termstr) # yields quadruples
	retval = term_lst[0]
	#print term_lst
	for i in range(1, len(term_lst), 2):
		ix = term_lst[i]
		pgs = term_lst[i+1]
		#print 'ix=' + ix + '; pgs=' + pgs
		#print
		roman.num = ix
		vol = dectostr(roman.calc(), 2)
		adr = adr_str.replace(volstr, str(vol))

		pgs_w_adr = re.sub(r'([0-9]+)([;,\- ])', adr, pgs)
		#print 'pgswadr=' + pgs_w_adr
		retval += ' ' + ix + ', ' + pgs_w_adr

	return retval

#print process_term(exstr)
result = process_term_list(tststr)

fileobj = open(os.path.dirname(__file__) + '/../Harvard Classics/harvardclassics50_ix_mmx_links.txt', 'w') # open for reading
#f = open(os.path.dirname(__file__) + '/../data.yml')

fileobj.write(str.join('', result)) # read all lines into array
fileobj.close()
