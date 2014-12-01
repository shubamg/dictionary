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
    pass

if __name__ == '__main__':
    main()
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
    import nltk
    diff=2# interval is defined here
    start=3 # starting value is defined here , 1 indexed
    count=0
    #thisfile = open("E:\sidbi project\project.txt") #file for reading
    #otherfile = open("E:\sidbi project\other_7.txt",'a+') # file for writng
    #str1=thisfile.read()
    #thisfile.close()
    #text=nltk.word_tokenize(str1)
    text=nltk.word_tokenize("This is test . I am eating .")
    a=nltk.pos_tag(text)
    l = list()
    from nltk.corpus import wordnet as wn
    for itera in a:
        s=itera[1][0]
        if s>='A' and s<='Z':# s is not a punctuation
            count=count+1
            if(count>=start and count%diff==start%diff):# words to be changed
                word=itera[0]
                l1=list()
                l1.append(word)
                print(word)
                for ss in wn.synsets(word):# synonym sets of word
                    for sg in ss.lemma_names():# each word in a particular synonym set
                        temp=nltk.word_tokenize(str(sg))# get tuple for that word
                        if ((nltk.pos_tag(temp))[0][1]) == itera[1] and (str(sg) not in l1):# if type is both is same and it is not already in list
                            l1.append(str(sg))# add it to the list
                            print(str(sg)+'\t')
                l.append(l1)
                del l1[:]
                print("\n")




if __name__ == '__main__':
    main()
