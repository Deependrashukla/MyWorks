import random

import matplotlib.pyplot as plt

def maximal_left_right(points_list):
    """
    Returns the list of maximal points in an array and the comparisons taking place.

    It uses the left-to-right sweeping algorithm and requires a candidate list in addition.

    Parameter_points: List of all the points to be processed
    Precondition: Type of point should be a list containing the tuple.
    """
    maximal_points = []
    comparisons = 0
    
    for point in points_list:
        comparisons += 1
        while maximal_points and maximal_points[-1][1] <= point[1]:
            comparisons += 1
            maximal_points.pop()
        maximal_points.append(point)
    
    return maximal_points, comparisons

def maximal_right_left(points_list):
    
    """
    Returns the list of maximal points in an array and the comparisons taking place.

    It uses the right-to-left sweeping algorithm and requires a candidate list in addition.

    Parameter_points: List of all the points to be processed
    Precondition: Type of point should be a list containing the tuple.
    """
    
    maximal_point_list = [points_list[-1]]
    comparison  = 0
    for i in range(len(points_list)-2, 0, -1):
      comparison += 1
      if maximal_point_list[-1][1] < points_list[i][1]:
        maximal_point_list.append(points_list[i])
    return maximal_point_list, comparison


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

    left_to_right_maximal_points, left_to_right_comparisons = maximal_left_right(original_points)
    print("\nLeft to Right Maximal points:", left_to_right_maximal_points)
    print("Left to Right Number of Comparisons:", left_to_right_comparisons)

    right_to_left_maximal_points, right_to_left_comparisons = maximal_right_left(original_points)
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
