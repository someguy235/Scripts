#From some 'challenge' site
#Can't remember exactly what the goal was
#Not finished

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thrity', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
numbers = []
string = ''

for i in range(0, 9):
    string=ones[i]
    numbers.append(string)
for i in range(0, 10):
    string=teens[i]
    numbers.append(string)
for i in range(0, 8):
    string=tens[i]
    for j in range(0, 10):
        temp = string
        if(j==0):
            pass
        else:
            temp=string+ones[j-1]
        numbers.append(temp)
tempNumbers = numbers[:]
for i in range(9):
    string=ones[i]
    string+='hundred'
    for item in range(len(numbers)):
        temp=string
        temp+=numbers[item]
        tempNumbers.append(temp)
numbers=tempNumbers[:]
numbers.append('thousand')
numbers.append('million')
numbers.sort()









#for number in numbers:
#    print number
print numbers

##eight
##eighteen
##eighteenmillion
##eighteenmillioneight
##eighteenmillioneighteen
##eighteenmillioneighteenthousand
##eighteenmillioneighteenthousandeight
##eighteenmillioneighteenthousandeighteen
