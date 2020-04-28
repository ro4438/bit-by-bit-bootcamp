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

import random
import simplegui

def new_game():
    global card3, po, state, exposed, card1

    def create(card):
        while len(card) != 8:
            num = random.randrange(0, 8)
            if num not in card:
                card.append(num)
        return card

    card3 = []
    card1 = []
    card2 = []
    po = []
    card1 = create(card1)
    card2 = create(card2)
    card1.extend(card2)
    random.shuffle(card1)
    state = 0
    exposed = []
    for i in range(0, 16, 1):
        exposed.insert(i, False)


def mouseclick(pos):
    global card3, po, state, exposed, card1
    if state == 2:
        if card3[0] != card3[1]:
            exposed[po[0]] = False
            exposed[po[1]] = False
        card3 = []
        state = 0
        po = []
    ind = pos[0] // 50
    card3.append(card1[ind])
    po.append(ind)
    if exposed[ind] == False and state < 2:
        exposed[ind] = True
        state += 1


def draw(canvas):
    global card1
    gap = 0
    for i in range(0, 16, 1):
        if exposed[i] == False:
            canvas.draw_polygon([[0 + gap, 0], [0 + gap, 100], [50 + gap, 100], [50 + gap, 0]], 1, "Black", "Green")
        elif exposed[i] == True:
            canvas.draw_text(str(card1[i]), [15 + gap, 65], 50, 'White')
        gap += 50


frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()

print("Done")

