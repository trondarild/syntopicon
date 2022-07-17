# assumes input is a "great idea"
# copy into in.txt, output in gi_out.txt
#cat gi_in.txt|sed -E 's/([a-z]) \n([a-z])/\1 \2/g' > gi_out.txt
#cat gi_in.txt|sed -E 's/ \n/ /g' > gi_out.txt
#cat gi_in.txt|sed -E -e ':a' -e 'N' -e '$!ba' -e 's/([a-z\,\.\-]) \n(["a-zA-Z])/\1 \2/g' | sed -E 's/([a-z])\- ([a-z])/\1\2/g' > gi_out.txt
cat gi_in.txt|perl -0777 -p -e 's/THE GREAT IDEAS +//g; s/CHAPTER [0-9]+ *: [A-Z]+ *//g; s/([a-z",;\.\-]) \n(["a-zA-Z])/$1 $2/g; s/([a-z",;\.\-]) \n{3,7}(["a-zA-Z])/$1 $2/g; s/([a-zA-Z])\- ([a-zA-Z])/$1$2/g; s/ JL / /g' | sed '1 i\
[[Adler 1952 - The great ideas (book)]] : [[ (the great ideas)]]' | sed '$ a\
[[Category: (syntopicon)' > gi_out.txt
#cat gi_in.txt|perl -0777 -p -e 's/([a-z",;\.]) \n(["a-zA-Z])/$1 $2/g' > gi_out.txt
#echo "foo foo so foo ignore this" | sed 's/foo/bar/g'
#cat gi_in.txt|tr '\n' ' '> gi_out.txt