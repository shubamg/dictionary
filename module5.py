#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      shubamg
#
# Created:     01-12-2014
# Copyright:   (c) shubamg 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     otherfile = open("E:\sidbi project\other_2.txt",'a+')
     #otherfile.write("\t");
     from nltk.corpus import wordnet as wn
     for ss in wn.synsets('love'):
        for sg in ss.lemma_names():
            if str(sg) != 'love':
                otherfile.write(str(sg)+'\t')
        otherfile.write('\n')
        #print(str((ss.lemma_names())[0]))
     print('over')
     otherfile.close()



if __name__ == '__main__':
    main()
