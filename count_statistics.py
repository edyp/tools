import sys
import re

testlog = open(str(sys.argv[1]), 'r')
testtxt = testlog.read()
testlog.close()
testjudgement = re.findall('([0-9]{4}: FAILED|[0-9]{4}: PASSED)', testtxt)

passedtestcounter = {}

for test in testjudgement:
    testnumber = int(test.split()[0].replace(':', ''))
    if 'PASSED' in test:
        if testnumber in passedtestcounter:
            passedtestcounter[testnumber] += 1
        else:
            passedtestcounter[testnumber] = 1
    elif 'FAILED' in test:
        if not testnumber in passedtestcounter:
            passedtestcounter[testnumber] = 0

print ("tc\tpass/runs\tpassrate")
for test in passedtestcounter:
    print (str(test) + "\t" + str(passedtestcounter[test]) + "/5\t" + str(passedtestcounter[test]/0.05) + "%")
