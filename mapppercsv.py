#!/usr/bin/python
import sys
import csv
def mapper():
    reader = csv.reader(sys.stdin)
    reader.next()
    for line in reader:
        line2 = line
        if len(line2) >= 2:	#some condition
	    try:
	        SYMBOL = line2[0]
                Date = line2[10]
	        Date = Date[7:]
	        Symbol = SYMBOL +' : '+ Date
	        Open = line2[2]
	        High = line2[3]
                print '%s\t%s\t%s' % (Symbol,Open,High)
	    except ValueError:
	        pass
def main():
	# sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()

