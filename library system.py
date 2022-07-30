from datetime import datetime
from os import system

#normal user can borrow up to two books at once
#admin user can borrow up to three books at once


#user login
users = {
    "2203332" : "040303-03-0303",
    "2203333" : "040404-04-0404"
}

admin = {
    "2203006" : "040202-02-0202"
}


'''
{bookid : name, author, subject, availability}
'''


#list of books
books = {
    "A001" : ["Introduction to Python", "Y. Daniel Liang", "Computer Science", "Available"],
    "A002" : ["Introduction to Biology", "name1", "Biology", "Not Available"],
    "A003" : ["Introduction to Physics", "name2", "Physics", "Not Available"],
    "A004" : ["Introduction to Chemistry", "name3", "Chemistry", "Not Available"],
    "A005" : ["Introduction to Calculus", "name4", "Maths", "Not Available"]
}

#borrow history
# time : user, book id, returned or not
# time = yyyy-mm-dd hh-mm-ss
history = {
    "2022/07/25 09:27:01" : ["2203333", "A003", 'no'],
    "2022/07/28 14:24:55" : ["2203006", "A001", "yes"],
    "2022/07/28 16:38:45" : ["2203332", "A002", "no"],
    "2022/07/29 15:46:12" : ["2203006", "A005", "no"],
    "2022/07/29 17:48:19" : ["2203333", "A004", 'no']

}


#get the current time
def getTime():
    dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return dt

#check if user enter correct yes or no function
def checkValidity(act, text):

    while True:
        if act in ['Y', 'y', 'N', 'n']:
            return act
            break
        else:
            print()
            print("Please enter y/n only")
            act = input(text)

#login page
def login():


    getID = "Please enter your ID : "
    getPassword = "Please enter your password : "

    loginUser = input(getID)
    loginPassword = input(getPassword)

    if loginUser in admin:
        if loginPassword == admin.get(loginUser):
            adminLogin(loginUser)
        else:
            print("\nThe password is incorrect. Please try again.")
            login()

    elif loginUser in users:
        if loginPassword == users.get(loginUser):
            normalLogin(loginUser)
        else:
            print("\nThe password is incorrect. Please try again.")
            login()

    else:
        print("\nInvalid user.")
        login()

#registration page
def registration():
    ID = input("Please sign up your id : ")

    while True:
        if ID in users.keys() or ID in admin.keys():
            print()
            print("The id is already exist")
            ID = input("Please sign up your id : ")
        else:
            break

    password =  input("Please sign up your password(at least 8 character) : ")

    while True:
        if len(password) < 8:
            print("Your password is too short")
            password = input("Please sign up your password(at least 8 character) : ")
        else:
            break

    users[ID] = password

    normalLogin(ID)


adminAction = "\n1. Search book/Borrow book\n"\
              "2. Return book\n" \
              "3. Check borrow history\n" \
              "4. Exit\n" \
              "5. Register new book\n\n" \
              "Please enter your action : "

userAction = "\n1. Search book/Borrow book\n" \
             "2. Return book\n" \
             "3. Check borrow history\n" \
             "4. Exit\n\n" \
             "Please enter your action : "

adminHistory = "\n1. Check ownself history\n" \
               "2. Check all history\n\n" \
               "Please enter your action : "

#admin power
def adminLogin(user):
    action = input(adminAction)

    action = testAction(action, adminAction, 1)

    instruction(action, user, role= 1)
    #library(user, action)

#normal user
def normalLogin(user):
    action = input(userAction)

    action = testAction(action, userAction, 2)

    instruction(action, user, role= 2)
    #library(user, action)


#check if the input is a valid action
def testAction(value, text, role):

    isCorrect = False
    isInteger = False

    while not isCorrect or not isInteger:

        while not isInteger:
            try:
                value = int(value)
                isInteger = True
            except ValueError:
                print("\nPlease enter a valid action")
                value = input(text)

        if role == 1:
            if value < 1 or value > 5:
                print("\nPlease enter a valid action")
                value = input(text)
                isInteger = False
            else:
                isCorrect = True

        else:
            if value < 1 or value > 4:
                print("\nPlease enter a valid action")
                value = input(text)
                isInteger = False
            else:
                isCorrect = True

    return value


def instruction(act, userID, role):

    system('cls')

    if act == 1:
        searchBook(userID, role)
    elif act == 2:
        returnBook(userID, role)
    elif act == 3:
        checkHistory(userID, role)
    elif act == 4:
        print()
    else:
        bookRegistration(userID, role)

def returnToMainMenu(userID, role):
    print()
    n = input("Press enter to return to main menu")

    system('cls')

    if role == 1:
        adminLogin(userID)
    else:
        normalLogin(userID)


#action 1
def searchBook(id, role):
    reference = (input("Please enter the id/title/name/subject of the book you wish to search : ")).lower().strip().replace(" ","")


    specialBookListKeys = [k.lower() for k in books.keys()]
    specialBookListName = [v[0].lower().strip().replace(" ","") for v in books.values()]
    specialBookListAuthor = [v[1].lower().strip().replace(" ","") for v in books.values()]
    specialBookListSubject = [v[2].lower().strip().replace(" ","") for v in books.values()]


    if reference in specialBookListKeys:
        reference = reference.upper()

        print()
        print("Book id :", reference)
        print("Title :", books[reference][0])
        print("Author :", books[reference][1])
        print("Subject :", books[reference][2])
        print("Availability :", books[reference][3])

        if books[reference][3] == "Available" :
            borrowBook(id, role, reference)
        else: 
            returnToMainMenu(id, role)

    elif reference in specialBookListName:
        reference = specialBookListKeys[specialBookListName.index(reference)].upper()

        print()
        print("Book id :", reference)
        print("Title :", books[reference][0])
        print("Author :", books[reference][1])
        print("Subject :", books[reference][2])
        print("Availability :", books[reference][3])

        if books[reference][3] == "Available" :
            borrowBook(id, role, reference)
        else: 
            returnToMainMenu(id, role)

    elif reference in specialBookListAuthor:
        reference = specialBookListKeys[specialBookListAuthor.index(reference)].upper()

        print()
        print("Book id :", reference)
        print("Title :", books[reference][0])
        print("Author :", books[reference][1])
        print("Subject :", books[reference][2])
        print("Availability :", books[reference][3])

        if books[reference][3] == "Available" :
            borrowBook(id, role, reference)
        else: 
            returnToMainMenu(id, role)

    elif reference in specialBookListSubject:
        reference = specialBookListKeys[specialBookListSubject.index(reference)].upper()

        print()
        print("Book id :", reference)
        print("Title :", books[reference][0])
        print("Author :", books[reference][1])
        print("Subject :", books[reference][2])
        print("Availability :", books[reference][3])

        if books[reference][3] == "Available" :
            borrowBook(id, role, reference)
        else: 
            returnToMainMenu(id, role)

    else:
        print("\nThe book you searched for is not found")
        returnToMainMenu(id, role)


'''
need to solve when the date is more than one month
'''
def borrowBook(id, role, bookid):

    historyTime = [k for k in history.keys()]
    historyID = [v[0] for v in history.values()]
    historyBook = [v[1] for v in history.values()]
    isReturned = [v[2] for v in history.values()]

    text = "\nDo you wish to borrow this book ? (y/n) : "
    wantToBorrow = input(text)

    wantToBorrow = checkValidity(wantToBorrow, text)

    if wantToBorrow in ['Y', 'y']:
        #admin can borrow up to three book at once
        if role == 1:
            count = 0
            for i in range(len(historyID)):
                if id == historyID[i]:
                    if isReturned[i] == "no":
                        count += 1

            if count < 3:

                #update history
                time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                history[time] = [id, bookid, 'no']

                dt = datetime.now().strftime("%d")

                dt = int(dt)
                dt += 7
                dt = str(dt)

                dt = datetime.now().strftime("%Y/%m/" + dt + " %H:%M:%S")

                #set the book as not available
                books[bookid] = [books[bookid][0], books[bookid][1], books[bookid][2], "Not Available"]

                print("\nYou have successfully borrow the book.\n"
                      "Please return the book by", dt, "or penalty will be applied.")


                returnToMainMenu(id, role)

            else:
                print("\nYou can borrow up to 3 books at once only.\n"
                      "Please return previously borrowed book first.")

                returnToMainMenu(id, role)

        #normal user can borrow up to two books at once
        else:
            count = 0
            for i in range(len(historyID)):
                if id == historyID[i]:
                    if isReturned[i] == "no":
                        count += 1

            if count < 2:

                time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                history[time]=  [id, bookid, 'no']

                dt = datetime.now().strftime("%d")

                dt = int(dt)
                dt += 7
                dt = str(dt)

                dt = datetime.now().strftime("%Y/%m/" + dt + " %H:%M:%S")

                books[bookid] = [books[bookid][0], books[bookid][1], books[bookid][2], "Not Available"]

                print("\nYou have successfully borrow the book.\n"
                      "Please return the book by", dt, "or penalty will be applied.")

                returnToMainMenu(id, role)

            else:
                print("\nYou can borrow up to 2 books at once only.\n"
                      "Please return previously borrowed book first.")

                returnToMainMenu(id, role)

    returnToMainMenu(id, role)

#action 2
def returnBook(id, role):

    historyTime = [k for k in history.keys()]
    historyID = [v[0] for v in history.values()]
    historyBook = [v[1] for v in history.values()]
    isReturned = [v[2] for v in history.values()]

    newLst = []
    count = 0
    for i in range(len(historyID)):
        if id == historyID[i] and isReturned[i] == "no":
            count += 1
            newLst.append(historyBook[i])
            print(historyTime[i])
            print("user :", historyID[i])
            print("book id :", historyBook[i])

            print()

    #print
    if count == 0:
        print("You have no book that are not return")

        returnToMainMenu(id, role)

    else:
        returning(newLst, id, role)


def returning(lst, id, role):

    historyTime = [k for k in history.keys()]
    historyID = [v[0] for v in history.values()]
    historyBook = [v[1] for v in history.values()]
    isReturned = [v[2] for v in history.values()]

    wantToReturn = input("Enter the book id that you wish to return : ").upper()

    if wantToReturn in lst:
        books[wantToReturn] = [books[wantToReturn][0], books[wantToReturn][1], books[wantToReturn][2], "Available"]

        idx = historyBook.index(wantToReturn)

        history[historyTime[idx]] = [historyID[idx], historyBook[idx], 'yes']
        print("\nThe book is returned successfully.\n"
              "Thank you.")

        returnToMainMenu(id, role)

    else:
        print("\nThe book id is invalid")
        retry = input("Do you want to Re-enter ? (y/n) : ")
        retry = checkValidity(retry, "Do you want to Re-enter ? (y/n) : ")

        if retry in ['Y', 'y']:
            print()
            returning(lst, id, role)

        else:
            print("\nThank you")

            returnToMainMenu(id, role)


#action 3
def checkHistory(id, role):

    historyID = [v[0] for v in history.values()]

    #admin
    if role == 1:
        who = input(adminHistory)

        isValid = False
        while not isValid:
            if who in ["1", "2"]:
                isValid = True
                if who == "1":
                    for i in range(len(historyID)):
                        if id == historyID[i]:
                            historyPrinting(i)

                    returnToMainMenu(id, role)

                if who == "2":
                    for i in range(len(historyID)):
                        historyPrinting(i)

                    returnToMainMenu(id, role)

            else:
                print("\nPlease enter a valid action.")
                who = input(adminHistory)

    else:
        for i in range(len(historyID)):
            if id == historyID[i]:
                historyPrinting(i)

        returnToMainMenu(id, role)

#print the history
def historyPrinting(index):

    historyTime = [k for k in history.keys()]
    historyID = [v[0] for v in history.values()]
    historyBook = [v[1] for v in history.values()]
    isReturned = [v[2] for v in history.values()]

    print()
    print(historyTime[index])
    print("user :", historyID[index])
    print("book id :", historyBook[index])

    if isReturned[index] == "yes":
        print("The book is returned")
    else:
        print("The book is not returned")

'''
action 4 repeat if keyin exist book id (need to solve)
'''

#action 4
def bookRegistration(id, role):
    code = input("PLease key in the code of the book : ")

    if code in books:
        print("The code is already exist")

        reEnter = input("Do you want to register again? (y/n) : ")

        reEnter = checkValidity(reEnter, "Do you want to register again? (y/n) : ")

        if reEnter in ["y", "Y"]:
            isReEnterValid = True
            print()
            bookRegistration()

        elif reEnter in ["N", 'n']:
            isReEnterValid = True
            print("\nthank you")

            returnToMainMenu(id, role)


    else:
        title = input("Please key in the title of the book : ")
        author = input("Please key in the author of the book : ")
        subject = input("Please key in the subject of the book : ")

        print()
        print("Book id :", code)
        print("Title :", title)
        print("Author :", author)
        print("Subject :", subject)

        confirmation = input("Is the information correct? (y/n) : ")

        confirmation = checkValidity(confirmation,"Is the information correct? (y/n) : ")

        if confirmation in ['Y', 'y']:
            books.update(code= [title, author, subject, "available"])
            print("The book is registered successfully")

            returnToMainMenu(id, role)

        elif confirmation in ['N', 'n']:
            print()
            bookRegistration()

#menu

''' 
login
password
new user
'''

def checkUser():
    text = "Welcome to MeTAR Library" \

    text2 = "Are you a new user ? (y/n) : "

    print(text)
    newUser = input(text2)

    newUser = checkValidity(newUser, text2)

    if newUser in ["N", 'n']:
        system('cls')
        login()

    else:
        registration()


'''
time function??
'''

checkUser()


