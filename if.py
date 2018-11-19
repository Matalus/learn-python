is_male = True
is_tall = False

if is_male and is_tall: # if
   print("You are a tall male")
elif is_male and not(is_tall): # else if
   print("You are male but not tall")
elif not(is_male) and is_tall: # else if
   print("You are not a male but are tall")
else: #else
   print("You are either not male or not tall or both")