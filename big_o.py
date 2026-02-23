colours = ['yellow', 'blue', 'green', 'white', 'black']
other_colours = ['orange', 'brown']

def complex_algo(colours):
    count_colours = 0

    for color in colours:
        print(color)
        count_colours += 1
    
    for other_color in other_colours:
        print(other_color)
        count_colours += 1
    
    print(count_colours)

complex_algo(colours)