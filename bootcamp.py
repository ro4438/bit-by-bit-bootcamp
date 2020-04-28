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
print("The Binary Equivalent: ", decimal_to_binary(number))
print("----------------------")

#get value at specific location in Pascal's Triangle
def pascal_triangle(lineNumber):
    list1 = list()
    list1.append([1])
    i = 1
    while (i <= lineNumber):
        j = 1
        l = []
        l.append(1)
        while (j < i):
            l.append(list1[i - 1][j] + list1[i - 1][j - 1])
            j = j + 1
        l.append(1)
        list1.append(l)
        i = i + 1
    return list1

def binomial_coef(n, k):
    pascalTriangle = pascal_triangle(n)
    return (pascalTriangle[n][k - 1])

row_number = int(input("Enter Pascal's Triangle Row Number: "))
element_number = int(input("Enter Element Number For Designated Row (Must be less than row number value): "))
print(f"Row: {row_number}, Element: {element_number} - Value: {binomial_coef(row_number, element_number)}")
print("----------------------")

#Pig Latin Converter
words = str(input("Enter some text to translate to pig latin: "))
print(f"You entered: {words}")
words = words.split(' ') #create list of words from string of text
translated = []
for i in words:
    if len(i) >= 3: #I only want to translate words greater than 3 characters
      i = i[1:] + i[0] + "ay"
    translated.append(i)
print("Translated: ", " ".join(translated))
print("----------------------")
print("Done")
