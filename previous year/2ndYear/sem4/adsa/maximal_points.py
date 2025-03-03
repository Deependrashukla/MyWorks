
import random
import matplotlib.pyplot as plt


def leftRight(input):
    maximalPoints = []  # Initialize an empty list to store maximal points
    steps = 0  # Initialize a counter to keep track of the number of steps taken
    for i in input:  # Iterate over each point in the input list
        steps += 1  # Increment the step counter
        while len(maximalPoints) > 0 and maximalPoints[-1][1] <= i[1]:  # Check if the current point is greater than the top of the stack
            steps += 1  # Increment the step counter
            maximalPoints.pop()  # Pop the top of the stack until it is empty or the top of the stack has a greater y-coordinate than the current point
        maximalPoints.append(i)  # Append the current point to the stack
    
    return maximalPoints, steps  # Return the list of maximal points and the number of steps taken



def rightLeft(input):
    maximalPoints = [input[-1]]  # Initialize an empty list to store maximal points and add the last point in the input list
    steps = 0  # Initialize a counter to keep track of the number of steps taken
    for i in input[-1::-1]:  # Iterate over each point in the input list in reverse order
        steps+=1  # Increment the step counter
        if i[0] == maximalPoints[-1][0] and i[1] > maximalPoints[-1][1]:  # Check if the current point is greater than the second last maximal point
            maximalPoints.insert(-1, i)  # Insert the current point before the second last maximal point
        if i[1] > maximalPoints[-1][1]:  # Check if the current point is greater than the last maximal point
            maximalPoints.append(i)  # Append the current point to the list of maximal points
    return maximalPoints, steps  # Return the list of maximal points and the number of steps taken



def generate_random_original_points(n):
    
    """
    It will return the random number pairs generated in list of tuples.
    """
    return [(random.randint(1, 100), random.randint(1, 100)) for _ in range(n)]




def plot_points(ax, points, label):
    x, y = zip(*points)
    ax.scatter(x, y, label=label)

def plot_lines(ax, points, label):
    x, y = zip(*points)
    ax.plot(x, y, label=label)

def main():
    n = 13
    original_points = generate_random_original_points(n)
    original_points.sort()

    print("Input original_points:", original_points)

    left_to_right_maximal_points, left_to_right_comparisons = leftRight(original_points)
    print("\nLeft to Right Maximal points:", left_to_right_maximal_points)
    print("Left to Right Number of Comparisons:", left_to_right_comparisons)

    right_to_left_maximal_points, right_to_left_comparisons = rightLeft(original_points)
    print("\nRight to Left Maximal points:", right_to_left_maximal_points)
    print("Right to Left Number of Comparisons:", right_to_left_comparisons)

    fig, ax = plt.subplots()

    # Plot input points
    plot_points(ax, original_points, 'Input Points')

    # Plot left to right maximal points
    plot_points(ax, left_to_right_maximal_points, 'Left to Right Maximal Points')
    plot_lines(ax, left_to_right_maximal_points, 'Left to Right Connecting Lines')

    # Plot right to left maximal points
    plot_points(ax, right_to_left_maximal_points, 'Right to Left Maximal Points')
    plot_lines(ax, right_to_left_maximal_points, 'Right to Left Connecting Lines')

    ax.legend()
    plt.show()

main()
