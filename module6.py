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
    #thisfile = open("E:\sidbi project\project.txt")
    #str1=thisfile.read()
    #text=nltk.word_tokenize(str1)
    text=nltk.word_tokenize("I love you")
    a=nltk.pos_tag(text)
    l = list()
    from nltk.corpus import wordnet as wn
    for itera  in a:
        if itera[1].startswith('V'):
            word=itera[0]
            l1=list()
            l1.append(word)
            print('\n'+word)
            for ss in wn.synsets(word):
                for sg in ss.lemma_names():
                    temp=nltk.word_tokenize(str(sg))
                    if ((nltk.pos_tag(temp))[0][1]) == itera[1] and (str(sg) not in l1):
                        l1.append(str(sg))
                        print(str(sg)+'\t')
            l.append(l1)
            #thisfile.close()


if __name__ == '__main__':
    main()
