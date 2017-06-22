import mysql.connector
conn = mysql.connector.connect(user='root', password='8267836785', host='127.0.0.1', database='sys')
cur = conn.cursor(buffered=True)


def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 2

    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1,
               LD(s[:-1], t[:-1]) + cost])
    return res



s=input('Bir kelime girin : ').lower()
length_input=len(s)
length_input_minus_one=len(s)-1
length_input_plus_one=len(s)+1
cur.execute('''SELECT WORD FROM nlp_2 WHERE CHAR_LENGTH(WORD) = %d'''%length_input_minus_one)
similar_words_minus_one=cur.fetchall();
cur.execute('''SELECT WORD FROM nlp_2 WHERE CHAR_LENGTH(WORD) = %d'''%length_input)
similar_words_same=cur.fetchall();
cur.execute('''SELECT WORD FROM nlp_2 WHERE CHAR_LENGTH(WORD) = %d'''%length_input_plus_one)
similar_words_plus_one=cur.fetchall();

words=[]

print('Aşağıdakilerden birini mi demek istediniz : ')
for i in range(0,len(similar_words_minus_one)):
    similar=similar_words_minus_one[i][0]
    for j in range(0,len(s)-1):
        if(similar[0]==s[0] and similar[1]==s[1]):
            words.append(similar_words_minus_one[i][0])
            #print("minus one")
            #print(similar_words_minus_one[i][0])

for i in range(0,len(similar_words_same)):
    similar=similar_words_same[i][0]
    for j in range(0,len(s)-1):
        if(similar[0]==s[0] and similar[1]==s[1]):
            words.append(similar_words_same[i][0])
            #print("same")
            #print(similar_words_same[i][0])

for i in range(0,len(similar_words_plus_one)):
    similar=similar_words_plus_one[i][0]
    for j in range(0,len(s)-1):
        if(similar[0]==s[0] and similar[1]==s[1]):
            words.append(similar_words_plus_one[i][0])
            #print("plus one")
            #print(similar_words_plus_one[i][0])

distinct_words=[]
for x in words:
    x=x.lower()
    if(x not in distinct_words):
        distinct_words.append(x)

for i in range(0,len(distinct_words)-1):
    if(LD(s, distinct_words[i])<=1):
        print(distinct_words[i])


