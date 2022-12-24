import cmath
def addOne(number):
    return number + 1
def addDouble(number):
    return number * 2
def add(distance,number):
    return number + distance
def stepUpTimes(times,number):
    return number + times * number
def numberTimes(times,number):
    return number * times
def aNumberOfFactorial(number):
    result = 1
    for item in range(1,number+1):
        result = result * item
    return result
def squareRoot_negativeNumber(number):
    num_sqrt = cmath.sqrt(number)
    copiseded_numbertimes = '{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(number,
    num_sqrt.real,num_sqrt.imag)
    return copiseded_numbertimes
def 四舍五入(n):
    string = str(n)
    array = list(string)
    last = int(array[len(array)-1])
    if last <= 4:
        return string
    else:
        if n < 10:
            return "10"
        else:
            array[len(array)-1] = "0"
            second = int(array[len(array)-2])
            second += 1
            array[len(array)-2] = str(second)
            return "".join(array)
def 猜出你的年龄():
    print("在1~10内选一个数：")
    print("下面，将你生日转换为下面格式:\n\"你的生日几月几号+0\"，\n如4月4日，就是\"440\"")
    print("OK，接下来，将这个数乘2加5，\n然后将结果乘50，\n回答，这个数是什么")
    answer = input("回答我：\n")
    number = int(answer)
    numList = [1,2,3,4,5,6,7,8,9,10]
    for i in numList:
        if not answer.isalnum or int(answer) != (i * 2 + 5) * 50:
            print('不能输入范围外的内容')
            Error = {"错误":"用户输入范围外内容"}
            return [None,None,{"Error":Error}]
            break
        else:
            number += 1772
            answer = input("输入你出生的年份\n别以为前面在装虚弄假\n因为我会猜出你猜的数加年龄：\n")
            if len(answer) > 4 or len(answer) < 4:
                print('不能输入范围外的数')
            else:
                number -= int(answer)
                List = list(str(number))
                return [List[0],List[1]+List[2],{"Error":None}]
#result = 猜出你的年龄()
#if result[2]["Error"] == None:
    #print("你一开始选的数字是：\n{}\n你的年龄是：\n{}".format(result[0],result[1]))
#else:
    #print("错误")
def squareRoot_positiveNumber(number):
    num_sqrt = number ** 0.5
    copiseded_number = ' %0.3f 的平方根为 %0.3f'%(number ,num_sqrt)
    return copiseded_number
def squareOfANumber(number):
    result = number * number
    return result
def division(Divisor,Dividend):
    result = 'the quotient is: %s'% (Dividend/Divisor)
    return result
def divisionOne(Dividend):
    result = 'the quotient is: %s'% (Dividend/1)
    return result
def toThePowerOfNumber_positiveNumber(number,Power):
    num_sqrt = number ** Power
    copiseded_number = ' %0.3f 的 %0.3f 次方为 %0.3f'%(number,Power,num_sqrt)
    return copiseded_number
def toThePowerOfNumber_negativeNumber(number,Power):
    num_sqrt = number ** Power
    copiseded_numbertimes = '{0} 的 {1:0.3f}次方为 {2:0.3f}+{3:0.3f}j'.format(number,Power,
    num_sqrt.real,num_sqrt.imag)
    return copiseded_numbertimes
def subtraction(substractor,subtrahend):
    copiseded_number = subtrahend - substractor
    return copiseded_number
def subtractionOne(subtrahend):
    copiseded_number = subtrahend - 1
    return copiseded_number
def primeNumber_list_1_997_MinMaxNumber():
    copiseded_number = [29,71,113,173,229,281,349,409,463,541,601,659,733,809,863,941,2,31,73,127,179,233,283,353,419,467,547,607,661,739,811,877,947,3,37,79,131,181,239,293,359,421,479,557,613,673,743,821,881,953,5,41,83,137,191,241,307,367,431,487,563,617,677,751,823,883,967,7,43,89,139,193,251,311,373,433,491,569,619,683,757,827,887,971,11,47,97,149,197,257,313,379,439,499,571,631,691,761,829,907,977,13,53,101,151,199,263,317,383,443,503,577,641,701,769,839,911,983,17,59,103,157,211,269,331,389,449,509,587,643,709,773,853,919,991,19,61,107,163,223,271,337,397,457,521,593,647,719,787,857,929,997,23,67,109,167,277,347,401,461,523,599,653,727,797,859,937,168]
    List_min = min(copiseded_number)
    List_max = max(copiseded_number)
    print('max:',List_max)
    print('min:',List_min)
    return copiseded_number
