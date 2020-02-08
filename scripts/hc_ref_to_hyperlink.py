#
# translates sentence references to actual links
#

# Example
# "Air, composition of, xxx, 150-1; elasticity of, 155-6; "
# -> "Air, composition of, xxx , [http://adress/page=150 150-1]; elasticity of, [http://adress/page=155 155-6]; "

# pattern:
# romannumeral, [0-9]+(-,;) 
test_str = "Air, composition of, xxx, 150-1; elasticity of, 155-6; "

adr_str = 'https://archive.org/details/harvardclassics$vol$elio/page/$pgnum$/mode/1up'
vol_str = '$vol$'
pg_str = '$pgnum$'

def roman_to_number(romanstr):
	number = 0
	return number

def process_ref_string (refstr):
	retval = ''
	return retval

# main