import sys, json, difflib, sqlite3

dbfname = 'Dictionary.db'


# Define functions

# Identify user input and figure out word to look up. Returns word id
def translate(tcword, wordlist):
    # Attempts to match user input to dictionary lookup key
    if tcword.lower() in wordlist.keys():
        return wordlist[tcword.lower()]
    elif tcword.title() in wordlist.keys():
        return wordlist[tcword.title()]
    elif tcword.upper() in wordlist.keys():
        return wordlist[tcword.upper()]
    else:
        similar_word = difflib.get_close_matches(tcword, wordlist.keys(), 1)
        if len(similar_word) > 0:
            print("Could not find word " + lcword + ". Perhaps you meant " + similar_word[0] + ".")
            while True:
                lcresponse = input("Enter Y (yes) /N (no)?")
                if lcresponse.lower().rstrip() in ["y","yes"]:
                    return wordlist[similar_word[0]]
                elif lcresponse.lower().rstrip()  in ["n", "no"]:
                    return None
                else:
                    print("Could not interpret the response. Please re-enter. Y/N")

        else:
            return  None

# Print definitions list
def print_definitions(id, cn):

    definitions_list = cn.execute("""
        SELECT def_no, definition
        FROM  definitions
        WHERE word_id = ?
        """, (id,)).fetchall()

    if len(definitions_list) == 0:
        sys.exit("There was a problem fetching information for word " + word + ".")

    for (def_no, defn) in definitions_list:
        print(str(def_no) + ": " + defn)


# Load definitions
try:
    conn = sqlite3.connect(dbfname)
    c = conn.cursor()
except:
    sys.exit("Could not find definition file " + dbfname + ". Exiting program.")

# Instantiate word bank
wordbank = dict(c.execute('SELECT word, word_id FROM words').fetchall())

# Get user input
print("Welcome to the python interactive dictionary.")
print("We have definitions for " + str(len(wordbank)) + " words.")

lcword = input("Please enter word to look up.")
lookup_id = translate(lcword, wordbank)

if lookup_id != None:
    print_definitions(lookup_id, c)
else:
    print('The word does not exist. Please double check.')

# close connection
conn.close()
