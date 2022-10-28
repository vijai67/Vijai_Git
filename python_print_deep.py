# String Fuctions
story = "ongo they are nothing"
print(story.capitalize())

# Chap 3 Prog 1
ENTER = input("ENTER YOUR NAME : \n")
print ("Good afternoon\t" + ENTER)

# Chap 3 Prog 2
letter = '''\nDear <|NAME|>
You Are Selected,
CONGRATS! \nWelcom To ETL Testing
Date : <|DATE|>'''

NAME = input("Enter Your Name : \n")
DATE = input("Enter Today's Date : \n")
letter = letter.replace('<|NAME|>',NAME)
letter = letter.replace('<|DATE|>',DATE)
print('\n',letter,'\n')