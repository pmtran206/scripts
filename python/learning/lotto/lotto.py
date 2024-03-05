import re
import os


from plotly.graph_objs import Bar, Layout
from plotly import offline

def make_three_digit(x,y,z):
    return (int(x)*100 + int(y)*10 + int(z))

def yearly_list(filename):
    filepath = filename
    lines = []

    with open(filepath) as f:
        lines = f.readlines()

    stripped = [s.strip() for s in lines]

    tagged_numbers = []

    for t in stripped:
        if re.search(r'<li>\d</li>', t):
            tagged_numbers.append(t)

    numbers = []

    for n in tagged_numbers:
        numbers.append(n[4])

    daily_list = []

    x = 0
    while x < len(numbers):
        daily = 0
        daily = make_three_digit(numbers[x], numbers[x+1], numbers[x+2])
        daily_list.append(daily)
        x +=3

    daily_list  = daily_list[1::2]

    return daily_list

def graph(frequencies):
    #visualize
        
    x_values = list(range(0, 1000))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Numbers'}
    y_axis_config = {'title': 'Frequency'}

    my_layout = Layout(title='Pick 3 results',
                    xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='lotto.html')

    
def box(x, y, z):
    combos = []
    tupl1 = (x, y, z)
    tupl2 = (x, z, y)
    tupl3 = (y, x, z)
    tupl4 = (y, z, x)
    tupl5 = (z, y, x)
    tupl6 = (z, x, y)

    possibles = [ tupl1, tupl2, tupl3, tupl4, tupl5, tupl6]

    for tup in possibles:
        if tup not in combos:
            combos.append(tup)
    return(combos)

def generate_boxes():
    boxes = []
    for x in range(0,10):
        for y in range(0,10):
            for z in range(0,10):
                boxes.append(box(x,y,z))
    return boxes

def add_occurrences(tmplist, freq):
    outfile = "box-occurrences.txt"

    with open(outfile, 'w') as f:

        for b in tmplist:
            total = 0
            for tup in b:
                num = int(str(tup[0]) + str(tup[1]) + str(tup[2]))
                numstring = str(tup[0]) + str(tup[1]) + str(tup[2])
                
                f.write(f"{numstring} - {freq[num]}" + ",")
                total = total + freq[num] 
            f.write(f"-- Total:{total} \n")

def main():  

    frequencies = [0] * 1000
    directory = './numbers/'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            result = yearly_list(f)
            for pick in result:
                frequencies[pick]  += 1

    #print(frequencies)
    graph(frequencies)
    
    boxlist = generate_boxes()
    add_occurrences(boxlist, frequencies)
 

if __name__ == '__main__':
    main()