
def  numReverse(n):
    numList=list(str(n))
    numList.reverse()
    return [int(i) for i in numList]


def phoneNumberMasking(phoneNumber):
    listNum=list(phoneNumber)
    newNumber  =""
    for i, j in enumerate(listNum):
        if len(phoneNumber) -i >4:
            newNumber +="*"
        else:
            newNumber +=j
    return newNumber
