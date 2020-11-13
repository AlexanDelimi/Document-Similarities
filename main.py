import glob


def words(stringIterable):
 lineStream = iter(stringIterable)
 for line in lineStream:  # enumerate the lines
    for word in line.split():  # further break them down
        yield word

numberofdocs = 7
while (numberofdocs > 6) or (numberofdocs < 2):
    try:
        numberofdocs = int(input('Choose how many documents (max.6)'))
    except ValueError:
        print('Number%d \n' % (numberofdocs))


numberofresults=17
while (numberofresults>15) or (numberofresults<1):
    try:
        numberofresults=int(input('Choose how many results (max.15)'))
    except ValueError:
        print('Number%d \n' % (numberofresults))


def metro(f):
    met = 0
    for re in f:
        temporary = f[str(re)]*f[str(re)]
        met = met + temporary
    metr = pow(met, 0.5)
    return metr


def cosin(a, b):
    summa = 0
    if len(a)==len(b):
        for x in a:
            temp = a[str(x)]*b[str(x)]
            summa = summa+temp
        d1 = metro(a)
        d2 = metro(b)
        try:
            cos = summa/(float(d1)*float(d2))
        except ZeroDivisionError:
            cos = 0
        return cos

def main():
    files=[]
    files = (glob.glob("pythondocs\\*.txt"))
    bagofwords = []
    archive = []
    document1 = []
    document2 = []
    document3 = []
    document4 = []
    document5 = []
    document6=[]
    listofdocs = []
    occurences=[]
    listofdocs.append(document1)
    listofdocs.append(document2)
    listofdocs.append(document3)
    listofdocs.append(document4)
    listofdocs.append(document5)
    listofdocs.append(document6)
    for idx in range(numberofdocs):
        archive.append(open(files[idx], "r", encoding='UTF8'))
        for word in words(archive[idx]):
            bagofwords.append(word)
            listofdocs[idx].append(word)

    # removing special characters
    for idy, item in enumerate(bagofwords):
        bagofwords[idy] = bagofwords[idy].strip(',' '.' '(' ')' '"' ':' ';')
        bagofwords[idy] = bagofwords[idy].lower()

    for yay in range(numberofdocs):
        for hey, item in enumerate(listofdocs[yay]):
            listofdocs[yay][hey] = listofdocs[yay][hey].strip(',' '.' '(' ')' '"' ':' ';')
            listofdocs[yay][hey] = listofdocs[yay][hey].lower()
    bagofwords.sort()
    mydict1 = dict((k,0) for k in words(bagofwords))
    mydict2 = dict((k, 0) for k in words(bagofwords))
    mydict3 = dict((k, 0) for k in words(bagofwords))
    mydict4 = dict((k, 0) for k in words(bagofwords))
    mydict5 = dict((k, 0) for k in words(bagofwords))
    mydict6 = dict((k, 0) for k in words(bagofwords))
    occurences.append(mydict1)
    occurences.append(mydict2)
    occurences.append(mydict3)
    occurences.append(mydict4)
    occurences.append(mydict5)
    occurences.append(mydict6)
    for idz in range(numberofdocs):
       for idc in words(listofdocs[idz]):
           occurences[idz][idc] = listofdocs[idz].count(idc)
    results = {
        "document #1 document #2": cosin(mydict1, mydict2),
        "document #1 document #3": cosin(mydict1, mydict3),
        "document #1 document #4": cosin(mydict1, mydict4),
        "document #1 document #5": cosin(mydict1, mydict5),
        "document #1 document #6": cosin(mydict1, mydict6),
        "document #2 document #3": cosin(mydict2, mydict3),
        "document #2 document #4": cosin(mydict2, mydict4),
        "document #2 document #5": cosin(mydict2, mydict5),
        "document #2 document #6": cosin(mydict2, mydict6),
        "document #3 document #4": cosin(mydict3, mydict4),
        "document #3 document #5": cosin(mydict3, mydict5),
        "document #3 document #6": cosin(mydict3, mydict6),
        "document #4 document #5": cosin(mydict4, mydict5),
        "document #4 document #6": cosin(mydict4, mydict6),
        "document #5 document #6": cosin(mydict5, mydict6)
    }
    for i in range(numberofresults):
        heykey=max(results,key=results.get)
        print("The documents with the %d most similarity are " %(i+1), end = '')
        print(heykey, end = '')
        print(" with similarity ", end = '')
        print(results[str(heykey)])
        results.pop(heykey)


main()

