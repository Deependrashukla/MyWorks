def activity_selection(slst, flst):
    n = len(flst)
    ilst = list(range(n))
    ilst.sort(key=lambda i : flst[i])
    selected_activities = []
    latest = slst[0]
    for i in ilst:
        if slst[i] >= latest:
            # print("[",slst[i], flst[i],"]")
            selected_activities.append((slst[i], flst[i]))
            latest = flst[i]
    return selected_activities

start_times = [3,1,3,7,4,9]
finish_times = [4,6,5,8,6,11]   
selected = activity_selection(start_times, finish_times)
for activity in selected:
    print(activity)

import matplotlib.pyplot as plt

def plot_activities(selected_activities):
    plt.figure(figsize=(8, 4))
    for i, (start, finish) in enumerate(selected_activities):
        plt.plot([start, finish], [i, i], label=f"Activity {i+1}", marker='o')
    plt.xlabel("Time")
    plt.ylabel("Activity")
    plt.title("Selected Activities")
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot the selected activities
plot_activities(selected)

lst = [(1,4),(2,3),(4,5),(8,9),(9,10)]


