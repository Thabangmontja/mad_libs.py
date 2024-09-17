#mad Libs Story Generator
#function to create the story
def mad_libs_story():
    #promt user input
    day_adj = input("Enter an adjective to describe the day: ")
    monkey_adj = input("Enter an adjective to describe the monkey: ")
    lion_adj = input("Enter an adjective to describe the lion: ")
    experience_adj = input("Enter an adjective to describe the overall experience: ")

     # Conditional variation based on user input
    if experience_adj.lower() in ['amazing', 'fantastic', 'unforgettable']:
        ending = "I can't wait to go back!"
    else:
        ending = "It was an interesting day, but I think once is enough."

    # Constructing the story
    story = (f"On a beautiful {day_adj} day, I went to the zoo. "
             f"I saw a funny {monkey_adj} monkey swinging from the trees. "
             f"Then, I spotted a majestic {lion_adj} lion lounging in the sun. "
             f"What a wild and {experience_adj} experience! {ending}")
    
    # Display the final story
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Call the function to start the Mad Libs game
mad_libs_story()