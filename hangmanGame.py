from getword import wordList

def pictures(num):
    stages=[
    """
    ------
    |    |
    |
    |
    |
    |
    -
    """,
    """
    ------
    |    |
    |    o
    |
    |
    |
    -
    """,
    """
    ------
    |    |
    |    o
    |    |
    |    |
    |
    -
    """,
    """
    ------
    |    |
    |    o
    |   \|
    |    |
    |
    -
    """,
    """
    ------
    |    |
    |    o
    |   \|/
    |    |
    |
    -
    """,
    """
    ------
    |    |
    |    o
    |   \|/
    |    |
    |   /
    -
    """,
    """
    ------
    |    |
    |    o
    |   \|/
    |    |
    |   / \\
    -
    """,
    """
    ------
    |    |
    |    o
    |   \|/     R.I.P
    |    |
    |   / \\
    -
    """,
    """
  ||   /~\   ||
  \\\\  | oo)  //
   \\\\__\=/__//
     |  <> |
     |  <> |
    """
    ]
    return(stages[num])


def middle(word):
    emptyList=[]
    wrongList=[]
    count=0
    pictureState=(pictures(0))
    for i in range(len(word)):
        emptyList.append("-")
    print("Guess a random letter")
    letter=input()
    while(count!=6):
        if(len(letter)!=1):
            print("Invalid, please TYPE A LETTER: ")
            print()
            print("Guess a random Letter")
            letter=input()
        elif letter not in word:
            count+=1
            pictureState=pictures(count)
            wrongList.append(letter)
            print(pictureState,"   ",emptyList)
            print("Wrong Guesses:", wrongList)
            print("WRONG try again")
            print("Lives remaining: ",(6-count))
            print()
            print("Guess a random LETTER")
            letter=input()
            if count==6:
                print(pictures(7),"   ",emptyList)
                print(wrongList)
                print("correct answer:", word)
        elif letter in word:
            count1=word.count(letter)
            list=[]
            num=0
            if(count1==1):
                in1=word.index(letter)
                num=in1
                emptyList[num]=letter
            else:
                n=0
                while(n<count1):
                    in2=word.index(letter,num)
                    num=in2+1
                    list.append(in2)
                    n+=1
            for i in list:
                emptyList[i]=letter

            if(emptyList.count("-")!=0):
                print(pictureState,"   ",emptyList)
                print("Wrong Guesses:", wrongList)
                print("CORRECT!")
                print()
                print("Guess a random LETTER")
                letter=input()
            else:
                count=6
                print(pictures(8),"   ",emptyList)
                print("Congratulations you are a genius!")


def main():
    myword=wordList()
    word=(myword.thisWord)
    middle(word)
main()
