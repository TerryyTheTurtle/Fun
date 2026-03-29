banner_message = "Welcome to my Pyramid Scheme"
banner_styling = "^" * len(banner_message)

print(f"{banner_styling}\n{banner_message}\n{banner_styling}\n")

while True:
    custom_char = (str(input("Enter a single character: ")))
    if len(custom_char) > 1:
        print("ERROR: You must enter a single character. Try again.\n")
    else:
        break

while True:
    custom_number = input("Enter a number between 3-9: ")
    try:
        custom_number = int(custom_number)
        if custom_number in range(3,10):
            break
        else:
            print("ERROR: This is not a number between 3-9. Try again.\n")
    except ValueError:
        print("ERROR: You have not entered an integer. Try again.\n")

# Build the pyramid
print("\nBEHOLD YOUR PYRAMID!!!")
pyramid_scheme = custom_char
pyramid_shape = (custom_number * 2) - 1
for x in range(custom_number):
    print(pyramid_scheme.center(pyramid_shape))
    pyramid_scheme = custom_char + pyramid_scheme + custom_char
