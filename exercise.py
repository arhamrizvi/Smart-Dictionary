import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user =  "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)


cursor = con.cursor()

def translate(word):
    word = word.lower()

    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()

    if len(results) == 0:
        like_query = cursor.execute("SELECT * FROM Dictionary WHERE Expression LIKE %s LIMIT 4" , ("%"+ word + "%",))
        results = cursor.fetchall()
        if len(results) == 0:
            return "Sorry the word doesnt exist"
        yn = input("Did you mean %s instead? Enter Y for Yes, N for No " %results)
        if yn == 'Y':
            return results
        elif yn == 'N':
            return "sorry the word doesnt exist"
        else:
            return "wrong input. Program closing"

    return results


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    if len(output)>0:
        counter =1
        for result in output:    
            print(str(counter)+". "+word+": "+result[1])
            counter+=1
else:
    print(output)

