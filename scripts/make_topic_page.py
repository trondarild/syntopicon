#
# chops syntopicon into discrete topics with ref list
# and makes mediawiki pages for each topic
#
import re
import sys
import os
import string
from collections import OrderedDict

bookname = "[[Great books of the Western world volume # (book)|refname]]"

pagetemplate = """
[[Great books of the Western world - A Syntopicon (book)]] : [[<topic_name> (the great ideas)]]

==Intuition==
'''<topic_name>''' (also called [[also called::<idea_name> <topic_ix> (the great ideas)]])

==References==
<topic_ref_list>

[[Category:<idea_name> (syntopicon)]]
"""

# read syntopicon text

path = "./"
filename = "tstinput.txt" #"syntopicon-ideas.txt"
# expand and join path and filename
fileandpath = os.path.join(os.path.expanduser(path), filename)
fileobj = open(fileandpath, 'r') # open for reading
textblock = fileobj.read() # read all as signle block
fileobj.close()
#print textblock
# clean nobreaking space
# printable = set(string.printable)
# out = []
# for l in lines:
#   a = l.decode("utf-8").replace(u"\xc2", "").replace(u"\xa0", " ").encode("utf-8")
#   if not a == '\n': out.append(a)
# lines = out

# parcel into ideas


# for each idea, extract references
ideaname = re.match(r'==Chapter .+? ([A-Z ]+)==', textblock).group(1)
ideaname = ideaname.title()
# for references, extract each topic and its references
topics = re.split('\#', textblock)
out = ''
# extract topic name and code
for topic in topics:
	topic_lines = re.split('\n', topic)
	topic_complex = topic_lines[0].split(' ', 1)
	topic_refs = re.split('\n', topic, 1)[1]
	topic_ref_lines = topic_refs.split('\n')
	topic_refs = ''
	for line in topic_ref_lines:
		#print line
		if line == '':
			continue
		line_cmplx = re.split(' ', line, 1)
		booknum = line_cmplx[0]
		tail = line_cmplx[1]
		booklnk = bookname.replace('#', booknum).replace('refname', booknum)
		topic_refs = topic_refs + '* ' + booklnk + ' ' + tail + '\n'
	#topic_refs = '\n'.join(topic_ref_lines)
	topic_code = topic_complex[0].replace('.', '')
	topic_name = topic_complex[1]
	#print 'code=' + topic_code + '; name= ' + topic_name
	#print topic_refs
	
	# add link to book page to each reference item

	# generate mediawiki page for topic
	page = pagetemplate.replace('<topic_name>', topic_name)
	page = page.replace('<topic_ix>', topic_code)
	page = page.replace('<topic_ref_list>', topic_refs)
	page = page.replace('<idea_name>', ideaname)
	out = out + page + '\n\n\n'

print out
# add page to a file for the current idea 
filename = ideaname + "_ref.txt"
fileobj = open(filename, 'w') # open for writing
fileobj.write(out)
fileobj.close()

print "wrote to file: " + filename
print
print
