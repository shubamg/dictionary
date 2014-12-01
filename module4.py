#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      shubamg
#
# Created:     29-11-2014
# Copyright:   (c) shubamg 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# This writes the words within braces in a text file
def main():
    thisfile = open("E:\sidbi project\curly.txt")
    str=thisfile.read()
    otherfile=open("E:\sidbi project\other4.txt",'a+')
    a= str.split('{')
    for j in (a):
        if '}'  in j:
            b = j.split('}')
            otherfile.write(b[0]+'\n')
    otherfile.close()
    thisfile.close()



if __name__ == '__main__':
    main()