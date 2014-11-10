#Hi Griff

#Version 0.1.4

game = []

nothing = True
while (nothing):
    y = raw_input("How many columns? ")
    x = raw_input("How many rows? ")
    try:
        int(x)
        int(y)
        if x < 0 or y < 0:
            print "That doesn't work" 
        elif x > 0 and y > 0:
            x = abs(int(x))
            y = abs(int(y))
            nothing = False 
    except:
        print "One or more of your values is not a positive integer. Please try again."

for i in range(0,x):
    game.append(["0"] * y) 

def print_game(game):
    for i in game:
        print " ".join(i) 

print " "
print_game(game)
print " "      

def replacement(t, u, k):
    game[t-1][u-1] = k 
    print_game(game)
    prompt1()

lst_ruth = [0] * x
total_ruth_strategy = 0 

def set_ruth_values():
    print "Ruth: ", lst_ruth
    global total_ruth_strategy 
    ayy = raw_input("Would you like to replace anything? ").lower()
    if ayy == "yes":
        value_add = True
        while (value_add):
            replacement_float_raw = raw_input("What would you like to use as a replacement value? ")
            try:
                replacement_float = float(replacement_float_raw)
                if replacement_float > 1.0:
                    print "That doesn't work."
                elif replacement_float < 0.0:
                    print "This doesn't work either."
                else: 
                    row_replace = True
                    while (row_replace):
                        row_replace_raw = raw_input("What row would you like to replace? ")
                        try:
                            row_replace = int(row_replace_raw)
                            if row_replace > x or row_replace < 0:
                                print "Oops! Please input a valid row value for Ruth"
                            else:
                                total_ruth_strategy -= lst_ruth[row_replace - 1] 
                                lst_ruth[row_replace - 1] = replacement_float
                                total_ruth_strategy += replacement_float 
                                row_replace = False
                                value_add = False
                                set_ruth_values()
                        except:
                            print "That is not an integer value, I'm afraid"
            except:
                print "Doh! That is not a float"
    elif ayy == "no":
        if sum(lst_ruth) != 1.0:
            print "Ruth does not have a total strategy of 1.0. Please try again. "
            set_ruth_values()
        else:
            print "okay~"
            set_charlie_values()
    else:
        print "Please input either 'yes' or 'no'"
        set_ruth_values()

lst_charlie = [0] * y
total_charlie_strategy = 0 

def set_charlie_values():
    print "Charlie: ", lst_charlie
    global total_charlie_strategy 
    lamo = raw_input("Would you like to replace anything? ").lower()
    if lamo == "yes":
        value_add_char = True
        while (value_add_char):
            replacement_float_char_raw = raw_input("What would you like to use as a replacement value? ")
            try:
                replacement_float_char = float(replacement_float_char_raw)
                if replacement_float_char > 1.0:
                    print "That doesn't work."
                elif replacement_float_char < 0.0:
                    print "This doesn't work either."
                else:
                    replacement_column_edit = True
                    while (replacement_column_edit):
                        row_replace_char_raw = raw_input("What row would you like to replace? ")
                        try:
                            row_replace_char = int(row_replace_char_raw)
                            if row_replace_char < 0 or row_replace_car > y:
                                print "Oops! Index out of range"
                            else:
                                total_charlie_strategy -= lst_charlie[row_replace_char - 1]
                                lst_charlie[row_replace_char - 1] = replacement_float_char
                                total_charlie_strategy += replacement_float_char 
                                replacement_column_edit = False
                                value_add_char = False
                                set_charlie_values()
                        except:
                            print "Oops! Something went wrong. Please try again."
            except:
                print "Dude, what?"
    elif lamo == "no":
        if sum(lst_charlie) != 1.0:
            print "Charlie's total strategy is not equal to 1. Try again. "
            set_charlie_values()
        else:
            print "okay~"
            prompt2()
    else:
        print "Please input either 'yes' or 'no'"
        set_charlie_values()

def prompt2(): 
    print " "
    print_game(game)
    print " "
    print "Ruth: ", lst_ruth
    print "Charlie: ", lst_charlie
    print " "
    response = raw_input("Is this the correct information? ").lower()
    if response == "no":
        permission = True
        while (permission):
            t = raw_input("Which part is incorrect? (game, ruth, charlie").lower()
            if t == "ruth":
                set_ruth_values()
                permission = False
            elif t == "charlie":
                set_charlie_values()
                permission = False
            elif t == "game":
                prompt1()
                permission = False
            else:
                print "Please input 'game', 'ruth', or 'charlie'"
    elif response == "yes":
        calculate_expected_payout()
    else:
        print "Please input either 'yes' or 'no'"
        prompt2()

def prompt1():
    yup = raw_input("Would you like to replace anything? (yes/no) ").lower()
    if yup == "yes":
        a = raw_input("What row? ")
        b = raw_input("Which column? ")
        c = raw_input("Replace with... ")
        nothingness = True
        while (nothingness):
            try:
                int(a)
                int(b)
                float(c)
                if int(a) < 0 or int(b) < 0:
                    print "One of your indices has a negative value. Please try again."
                    prompt1()
                elif int(a) > 0 and int(y) > 0:
                    a = int(a)
                    b = int(b)
                    nothingness = False
            except:
                print "One or more of your values is not an integer. Please try again."
                prompt1()
        if a > x:
            print "That is not a valid ROW value. Please try again."
            prompt1()
        elif b > y:
            print "That is not a valid COLUMN value. Please try again."
            prompt1()
        
        replacement(a, b, c)

    elif yup == "no":
        set_ruth_values()
    elif yup != "yes" or "no":
        print "Please input either 'yes' or 'no'."
        prompt1()

expected_payout_ruth = 0
def calculate_expected_payout():
    global x
    global y
    global expected_payout_ruth
    for i in range(x):
        for j in range(y):
            expected_payout_ruth += (lst_ruth[i] * lst_charlie[j] * float(game[i][j]))
    print " "
    print "Expected payout for Ruth: ", expected_payout_ruth
    print " "
    completion_state()

def completion_state():
    print "Done"

prompt1()
