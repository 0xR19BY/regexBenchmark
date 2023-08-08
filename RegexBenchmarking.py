import re
import time

class RegexPerformanceBenchmark:
    def __init__(self, field, regextestfile):
        self.field = field
        self.regextestfile = regextestfile

    #The open keeps fucking
    def testRegex(self, field, regextestfile, loops):
        x = 0
        startTime = time.time() #The time in which it takes from the python interpreter to go line to line is a performance issue and will not match the speed of regex running in .NET

        while x < loops:
            try:
                regexOpened = open(regextestfile, 'r') #Have to open and close these (not as "with as x") as they kept autoclosing
                fieldOpened = open(field, 'r')
                regex = re.findall(regexOpened.read(), fieldOpened.read())
                x = x + 1
        
            except re.error as e:
                return None

        endTime = time.time()
        elaspedTime = endTime - startTime

        return elaspedTime, len(regex)
        
'''
Wondering if I should use two .txt files for the input of regex, or if it should be inputted via CLI. Think I'll do it from 
the two .txt files.
'''
def main():
    regexTest1 = RegexPerformanceBenchmark.testRegex('Test1', 'field_file.txt', 'regex1.txt', 10000)
    regexTest2 = RegexPerformanceBenchmark.testRegex('Test2', 'field_file.txt', 'regex2.txt', 10000)

    print(f"Against the sample 'field_file.txt', the performance of expression 1 yields: \n {regexTest1} \n ---------------")
    print(f"Against the sample 'field_file.txt', the performance of expression 2 yields: \n {regexTest2} \n ---------------")    

main()