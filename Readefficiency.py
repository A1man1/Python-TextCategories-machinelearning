import re as regex 


def  Readtesting(comment):
        grade=''
        read=''
        num_sentence = len(regex.split("[!?.]+", comment))
        num_word=len(regex.split("\s",comment))
        s1=len(regex.findall("[aeiouyAEIOUY]+",comment))
        s2=len(regex.findall("[^aeiouyAEIOUY]+[eE]\\b",comment))
        s3=len(regex.findall("\\b[^aeiouyAEIOUY]*[eE]\\b",comment))
        num_syllable=s1-(s2-s3)
        flesch=206.835 - 1.015 *  num_word / num_sentence - 84.6 *  num_syllable / num_word
        if(flesch>=90):
               read="Very Easy"
               grade="5th Level"
        elif(flesch>=80):
               read="Easy"
               grade="6th Level"
        elif(flesch>=70):
               read="Fairly Easy"
               grade="7th-8th Level"
        elif(flesch>=60):
               read="Standard"
               grade="10th Level"
        elif(flesch>=50):
              read="Flairly Difficult"
              grade="12th Level"
        elif(flesch>=30):
              read="Difficult"
              grade="College Level"
        elif(flesch<29):
              read="Very Confusing"
              grade="Graduate Level"
        
        return  str(read+" : "+grade)
