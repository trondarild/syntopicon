#
# script for pulling out index terms for particular volumes of HC
#

# read index list

def to_roman(decimal):
	return 'xx'

def get_ixterm(term_str):
	'''
	Pull out index term of a line
	'''
	return ''

def get_pagenums_for_vol(roman_str):
	'''
	Pull out page numbers for a given volume number
	'''
	return ''


'''
result = ''
for i in 1-50:
	roman = to_roman(i)
	result += 'Volume ' + str(i) + ':' 
	for line in index_list:
		if roman in line:
			# pull out term and page numbers
			ixterm = get_ixterm(line)
			pagenums = get_pagenums_for_vol(roman)
			# add ixterm and pagenums to result
			result += '* ' + ixterm + ', ' + pagenums + '\n'
	# write out for volume
	print result # or write to file
'''