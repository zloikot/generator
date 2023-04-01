import sys, click


@click.command()
@click.option("--max_number",default = 10, help = "Максимальное число нумерации")
@click.option("--column_name", default = "name", help ="Название колонки")
@click.option("--len_block", default = 5, help="Длина генерируемой последовательности")

# 
# max_number,len_block,column_name = int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]

def chaos_generator(max_number, len_block, column_name):
    extender = '0000000000'

    spisok = [(extender+str(i))[-len_block:] for i in range(1,max_number+1)]

    with open('temp.txt','w') as temp:
        temp.write(column_name+'\n')
        for i in spisok:
            temp.write(str(i)+'\n')

