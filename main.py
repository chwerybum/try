print('''
*******************************************************************************
 _                     _                   
| |                   | |                  
| | _____   _____  ___| |_ ___  _ __ _   _ 
| |/ _ \ \ / / _ \/ __| __/ _ \| '__| | | |
| | (_) \ V /  __/\__ \ || (_) | |  | |_| |
|_|\___/ \_/ \___||___/\__\___/|_|   \__, |
                                      __/ |
                                     |___/ 
*******************************************************************************
''')
print("Welcome to Oyen Dating Simulator.")
print("Your mission is successful if you win Oyen\'s heart.\n") 

choice_1 = input("You will invite Oyen for a walk, choose the color of the shirt you will wear! Type 'Blue', 'Red', or 'Orange'\n").lower()

if choice_1 == "orange":
  choice_2 = input ("\n You successfully chose a shirt that matches with Oyen. Where will you take her for a date now? Type 'swimming pool', 'playground', or 'restaurant' \n").lower()
  if choice_2 == "swimming pool":
    print("Cats can't swim, Oyen drowned. Game over >:(")
  else:
    choice_3 = input("\nYou successfully took Oyen for a walk. Now, choose a meal for Oyen. Type 'seblak', 'fish', or 'chicken' \n".lower())
    if choice_3 == "seblak" :
      print("Oyen can't eat seblak, she is not good with spicy food, Game over! >:(")
    elif choice_3 == "fish" :
      print("Oyen is not in the mood to eat fish, Game over! >:(")
    else:
      print("Congratulations! You successfully invited Oyen for a date and she is happy with you! you win!")
else:
  print("Oyen is not happy with your shirt choice, Game over!")

