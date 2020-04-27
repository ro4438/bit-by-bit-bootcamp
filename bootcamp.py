#binary conversion function and call
decimal_accuracy = 7

def decimal_to_binary(num):  # Function inputs a float value and returns a binary equivalent

    whole = []  # The part before decimal point
    fractional = ['.']  # The part after decimal point

    decimal = round(num % 1, decimal_accuracy)  # Extract fractional number part of decimal
    w_num = int(num)  # Extract whole number part of decimal.
    i = 0

    # Loop to find binary of fractional part.
    while (decimal != 1 and i < decimal_accuracy):
        decimal = decimal * 2
        fractional.append(int(decimal // 1))
        decimal = round(decimal % 1, decimal_accuracy)
        if (decimal == 0): break  # Removes trailing zeros.
        i = i + 1

    # Loop to find binary of whole number part.
    while (w_num != 0):
        whole.append(w_num % 2)
        w_num = w_num // 2
    whole.reverse()

    final_value = float("".join(map(str, whole+fractional))) 
    if final_value.is_integer():
      return int(final_value)
    else: 
      return final_value
# Converts user input to float which is a string initially
number = float(input("Enter Any base-10 Number: "))
print("The Binary Equivalant: ", decimal_to_binary(number))
print("----------------------")




print("Done")
