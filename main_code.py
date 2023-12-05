bread = 'bread'

#highlighting: outsourced from (https://www.sololearn.com/en/discuss/2359764/how-can-i-put-formated-text-in-python-bold-italic-etc)
red = '\033[91m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'


with open ("terry_ratchett.txt", 'r') as terry:
    for line in terry:
        line = line.strip('\n')
        if bread in line: 
            newline = line.replace(bread, red + italics + underline + bread + end)
            print(newline)