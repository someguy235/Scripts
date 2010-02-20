import libgmail

ga = libgmail.GmailAccount("yourUserName@gmail.com", "yourPassword")
ga.login()
GREFolder = ga.getMessagesByLabel('GRE Words')

mails = [[],[]]
x = 0

for mail in GREFolder:
    if ('M-W\'s' in mail.subject):
        message = mail[0].source
        test = message[(message.find('The Word of the Day for ')):(message.find('Example sentence:'))]
        test = test[test.find('style47')+12:]
        word = test[:test.find('</b')]
        mails[0].append(word)
        test = test[test.find(': ')+2:]
        definition = test[:test.find('</span>')]
        definition = definition.replace('\n', '')
        definition = definition.replace('&nbsp', '')
        definition = definition.replace('=', '')
        definition = definition.replace('&mdash', '')
        definition = definition.replace(';', '')
        while ('<' in definition):
            partA = definition[:definition.find('<')]
            partB = definition[definition.find('>')+1:]
            definition = partA + partB
        mails[1].append(definition)
        print word
    elif('Peterson\'s' in mail.subject):
        pass
        message = mail[0].source
        test = message[message.find('<!-- begin content -->'):message.find('Example:')]
        test = test[test.find('Word of the Day')+15:]
        test = test[test.find('<div'):]
        word = test[test.find('>')+1:test.find('</div>')]
        mails[0].append(word)
        definition = test[test.find('Definition:'):]
        definition = definition.replace('\n', '')
        definition = definition[11:]
        while ('<' in definition):
            partA = definition[:definition.find('<')]
            partB = definition[definition.find('>')+1:]
            definition = partA + partB
        mails[1].append(definition)
        print word
    elif('Dictionary.com' in mail.subject):
        message = mail[0].source
        test = message[message.find('<span class="hw">')+17:]
        word = test[:test.find('</span>')]
        mails[0].append(word)
        test = test[test.find('</span>')+8:]
        test = test[:test.find('<blockquote>')]
        test = test.replace('\n', '')
        while('<' in test):
            partA = test[:test.find('<')]
            partB = test[test.find('>')+1:]
            test = partA + partB
        definition = test[:]
        mails[1].append(definition)
        print word

output = open('GREWords(temp).txt', 'w')

for word in range(len(mails[0])):
    output.write(mails[0][word].upper()+': '+mails[1][word]+'\n')


output.close()
