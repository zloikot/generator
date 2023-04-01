import sys, click

max_number,len_block,column_name = int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
extender = '0000000000'

spisok = [(extender+str(i))[-len_block:] for i in range(1,max_number+1)]

with open('temp.txt','w') as temp:
   temp.write(column_name+'\n')
   for i in spisok:
      temp.write(str(i)+'\n')

