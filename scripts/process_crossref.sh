cat cr_in.txt|perl -0777 -p -e 's/see /see \n/g; s/; /; \n/g; s/\n\n+/\n/g; s/\. \n/. \n\n/g; s/ \n([a-z0-9])/ $1/g; s/\n([A-Z]{2})/\n* $1/g; ' | sed '1 i\
=====Cross-References=====' > cr_out.txt