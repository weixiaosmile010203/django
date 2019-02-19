import logging

#关闭日志的语句
# logging.disable(logging.DEBUG)


#定义日志显示的语法格式
logging.basicConfig(filename='logTest.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#定义日志输出的内容
logging.debug('start of program')


def Num_ands(n):
    logging.debug('start of n(%s)' % n)
    sum = 0

    for i in range(n+1):
        logging.debug('sum is ' + str(sum) + ', i is ' + str(i))
        sum += i
    logging.debug('End of Sum(%s)' % sum)
    return sum


print(Num_ands(10))