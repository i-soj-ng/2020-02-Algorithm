import pickle
dbfilename = 'test3_4.dat'

# read the data
def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return[]

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

# command
def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")

        # add the data
        if parse[0] == 'add':
            try:   # Age와 Score에 숫자가 아닌 다른 문자를 넣으면 발생하는 에러를 잡음
                if str(type(int(parse[2]))) != "<class 'int'>" or str(type(int(parse[3]))) != "<class 'int'>":
                    print("Input correct age and score")
                else:
                    record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                    scdb += [record]
            except ValueError as e:
                print("Input correct age and score")
            except:
                if len(parse) < 4:
                    print("Input name, age, score")

        # delete the data
        elif parse[0] == 'del':
            dl = len(scdb)
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                if dl == len(scdb):   # 없는 이름을 넣었을 때
                    print("No Name")

            except:   # 이름을 넣지 않았을 때
                if len(parse) < 2:
                    print("Enter Name")

        # show all data
        elif parse[0] == 'show':
            try:
                if len(parse) == 1:
                    sortKey = 'Name'
                elif len(parse) == 2:
                    sortKey = parse[1]
                showScoreDB(scdb, sortKey)

            except:   # 잘못된 sortKey를 넣었을 때
                for p in scdb:
                    if (p['Name'] or p['Age'] or p['Score']) != parse[1]:
                        print("Input correct sortKey")
                        break

        # find the data and show it
        elif parse[0] == 'find':
            try:
                fd = []
                fd_len = len(fd)
                for p in scdb:
                    if p['Name'] == parse[1]:
                        fd += [p]
                        keyname = 'Name'
                        showScoreDB(fd, keyname)
                if fd_len == len(fd):   # 없는 이름을 넣었을 때
                    print("No Name")

            except:   # 이름을 넣지 않았을 때
                if len(parse) < 2:
                    print("Enter name")

        # modify score data
        elif parse[0] == 'inc':
            if len(parse) == 3:
                try:
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            a = int(p['Score'])
                            p['Score'] = str(a + int(parse[2]))
                            break
                except:
                    for p in scdb:
                        if p['Name'] != parse[1]:
                            print("Enter correct name")
            else:
                print("Enter name and amount")

        # quit
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)