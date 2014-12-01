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
    thisfile = open("E:\prp.txt")
    output_file = open("E:\pout.txt",'a+')
    str1=thisfile.read()
    text=nltk.word_tokenize(str1)
    #text=nltk.word_tokenize("This is test . I am eating .")
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

    count = 0
    for itera in a:
        if itera[1].startswith('V'):

            output_file.write("{")
            for ele in l[count]:
                output_file.write(ele)
                if l[count].index(ele) <> len(l[count])-1:
                    output_file.write("/ ")

            count+=1
            output_file.write("} ")

        else:
            output_file.write(itera[0]+" ")

    thisfile.close()
    output_file.close()


if __name__ == '__main__':
    main()