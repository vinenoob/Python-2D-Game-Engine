__author__ = 'jn186953'
background = []
with open("background.txt", "r") as w:
    for thing in w:
        print(thing)
        tmplst = []
        for meh in thing:
            if meh.isdigit():
                tmplst += meh
        background += [tmplst]


