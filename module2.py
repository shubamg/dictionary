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
    flag1 =0;
    # flag 1 = 0 implies no reversal of para, otherwise reverse them.
    flag2 =0;
    # flag 2 = 0 implies no reversal of individual sentences , otherwise not.
    seperator=['.','!','?'];
    thisfile = open("E:\sidbi project\project.txt")
    str=thisfile.read()
    a= str.split('\n')
    thisfile.close()
    otherfile = open("E:\sidbi project\other.txt",'a+')
    otherfile.write("\t");
    for j in (a):
        l=list();
        p=0;
        q=0;
        while(q<len(j)):
            while(q<len(j) and j[q] not in seperator):
                q=q+1;
            l.append(j[p:q+1]);
            p=q+1;
            q=q+1;
        for i in reversed(l):
            if  i:
                print(i);
                otherfile.write(i);
        otherfile.write("\n\t");
        del l[:];
    otherfile.close()


if __name__ == '__main__':
    main()

