import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random


def circle_plt(dna_stack):
    labels = list()
    sizes = list()

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=random.randint(0, 360))
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def horizon_bar_plt(dna_stack):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))  # np.arange(x) = [0, 1, 2 ... x-1]
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()


def linear_plt(dna_stack):
    fig, ax = plt.subplots()


if __name__ == '__main__':
    # Formatting data to plotter
    '''
    a = ['GACCGGCCTAG', 'GATCCGGGC', 'GACC', 'GGCCTAGGATCC', 'GGGC', 'GACC', 'GGCCTAG', 'GATCC', 'GGGC']
    times = [1, 3, 5, 2, 4]
    circle_plt(a)
    '''
    horizon_bar_plt(None)
