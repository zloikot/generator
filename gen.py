import sys, click


@click.command()
@click.option("--min_number",default = 1, help = "Минимальное число нумерации")
@click.option("--max_number",default = 10, help = "Максимальное число нумерации")
@click.option("--column_name", default = "name", help ="Название колонки")
@click.option("--len_block", default = 5, help="Длина генерируемой последовательности")
@click.option("--file_name", default = 'temp.txt', help="имя генерируемого файла")
# 
# max_number,len_block,column_name = int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]

def chaos_generator(min_number, max_number, len_block, column_name,file_name):
    extender = '0000000000'

    spisok = [(extender+str(i))[-len_block:] for i in range(min_number,max_number+1)]

    with open(file_name,'w') as temp:
        temp.write(column_name+'\n')
        for i in spisok:
            temp.write(str(i)+'\n')


if __name__ == '__main__':
    chaos_generator()