mad_title = "Welcome to Mad Libs! (3 libs)"
mad_banner = "=" * len(mad_title)

print(f"{mad_banner}\n{mad_title}\n{mad_banner}\n")

while True:
    print("List of games:")
    print("1. The Funny 'P' Story")
    print("2. Trip to the zoo")
    print("3. Getting ready for school")

    lib_selection = input("Select the lib you want to play (enter 1-3): ")

    try:
        lib_selection = int(lib_selection)
        if lib_selection in range(1,4):
            break
        else:
            print("ERROR: That is an invalid number selection\n")

    except ValueError:
        print("ERROR: You need to enter a number between 1-3\n")

if lib_selection == 1:
    lib_rule = "Rules: Every word must start with the letter 'P'"
    lib_banner = "*" * len(lib_rule)
    print(f"\n{lib_banner}\nMad Lib: The Funny 'P' Story\n{lib_rule}\n{lib_banner}")
    last_name = input("Last Name: ")
    adjective_one = input("Adjective: ")
    verb_one = input("Verb: ")
    plural_fruit = input("Plural Fruit: ")
    adjective_two = input("Adjective: ")
    adjective_three = input("Adjective: ")
    adjective_four = input("Adjective: ")
    first_name = input("Boy's First Name: ")
    verb_two = input("Verb: ")
    plural_noun_one = input("Plural Noun: ")
    verb_three = input("Verb that ends with ed: ")
    plural_noun_two = input("Plural Noun: ")
    noun_one = input("Noun: ")
    plural_noun_three = input("Plural Noun: ")
    food_one = input("Food: ")
    noun_two = input("Noun: ")
    verb_four = input("Verb that ends with ing: ")
    noun_three = input("Noun: ")
    noun_four = input("Noun: ")
    verb_five = input("Verb that ends with ed: ")
    adjective_five = input("Adjective: ")
    noun_five = input("Noun: ")
    verb_six = input("Verb: ")
    adjective_six = input("Adjective: ")
    plural_noun_four = input("Plural Noun: ")
    verb_seven = input("Verb: ")
    noun_six = input("Noun: ")
    adjective_seven = input("Adjective: ")

    # Output the Mab Lib
    print(f"\nPeter {last_name} was a {adjective_one} boy who liked to {verb_one} purple {plural_fruit}.")
    print(f"He was proud, {adjective_two} and proved to be possibly {adjective_three}.")
    print(f"Peter had a {adjective_four} brother named {first_name} who pretended to {verb_two} with Peter's {plural_noun_one},")
    print(f"but Peter didn't like that, so he {verb_three} {first_name}'s pants down and picked {plural_noun_two} from his pocket")
    print(f"{first_name} then pooped on Peter's {noun_one} to get revenge and that's when Peter put {plural_noun_three} on {first_name}'s {food_one} pizza-pocket")
    print(f"The boys continued to push each other pointlessly until {first_name} peed on a {noun_two} while {verb_four} on a {noun_three} and falling on a pail, letting go of his precious {noun_four}.")
    print(f"Peter felt bad and picked {first_name} up and {verb_five} him persistently until {first_name} perked up")
    print(f"{first_name} looked at Peter and planted a {adjective_five} kiss on his pink {noun_five} which made Peter {verb_six} precisely.")
    print(f"They forgave each other for being {adjective_six}, exchanged {plural_noun_four} and proudly played a game called {verb_seven} the {noun_six} please.")
    print(f"The brothers then became two pleasantly {adjective_seven} people!")
    print("\nThe End")

elif lib_selection == 2:
    print("\nSike, only 1 is a valid answer")
elif lib_selection == 3:
    print("\nSike, only 1 is a valid answer")
