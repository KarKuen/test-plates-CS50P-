import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity plates may contain a max of 6 characters and minimum of 2
    if 2 <= len(s) <= 6:
        #first number used cannot be 0
        for i in range(len(s)):
            if s[i].isnumeric():
                if s[i] == '0':
                    return(False)
                else:
                    break
        #all vanity plates must start with at least 2 letters
        if s[0].isalpha() and s[1].isalpha():
            #noperiods,spaces,punctuation marks
            for letter in s:
                if letter in string.punctuation:
                    return(False)

            iscenter = False
            number = False
            for text in s[2:]:
                if text.isnumeric():
                    number = True
                if text.isalpha() and number == True:
                    iscenter = True

            return(not iscenter)
        else:
            return(False)

        return(True)

    else:
        return(False)

if __name__ == '__main__':
    main()