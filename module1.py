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

def main():
    thisfile = open("E:\sidbi project\project.txt")
    str=thisfile.read()
    a= str.split('\n')
    thisfile.close()
    otherfile = open("E:\sidbi project\other.txt",'a+')
    otherfile.write("\t");
    for j in (a):
        b=j.split('.')
        for i in reversed(b):
            if  i:
                print(i+'.')
                otherfile.write(i+'.');
        otherfile.write("\n\t");
    otherfile.close()


if __name__ == '__main__':
    main()

