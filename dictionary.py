import mysql.connector
from difflib import get_close_matches

connnect = mysql.connector.connect(
    user ="ardit700_student",
    password ="ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input("Enter a word:  ")

cursor = connnect.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression ='%s'" %word) 
result = cursor.fetchall()

if result:
    for res in result:
        print(res[1])
elif len(get_close_matches(word,result.expression())) > 0:
    yn = input("Did you mean %s instead? If yes press y, in no press n.")
    if yn == "y":
        print(result[get_close_matches(word, result.expression)[0]])
    elif yn =="n":
        print("Word does not exist")
    else:
        print("Sorry I did not catch that")
else:
    print("No word found")