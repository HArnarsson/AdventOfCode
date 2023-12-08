from math import floor, ceil, sqrt


# See pdf for more info
def find_num_solutions(t, d):
    r_1 = (t-sqrt(t*t-4*d))/2
    r_2 = (t+sqrt(t*t-4*d))/2

    if not r_1.is_integer():
        if r_1 < 0:
            r_1 = 1
        else:
            r_1 = ceil(r_1)
        r_2 = floor(r_2)
    else:
        # If t^2 - 4*d is a perfect square, we have to discard
        # those exact integer solutions
        r_1 += 1
        r_2 -= 1

    # after these transformations, our valid solutions are:
    # r_1 <= x <=  r_2, therefore the number of solutions is r_2-r_1+1
    return int(r_2 - r_1 + 1)

filename = "input.txt"
with open(filename, 'r') as file:
    tmp_times = file.readline().strip().split(': ')[1].strip().split(' ')
    times = [int(tmp_times[i]) for i in range(len(tmp_times)) if tmp_times[i] != '']
    tmp_dist = file.readline().strip().split(': ')[1].strip().split(' ')
    distances = [int(tmp_dist[i]) for i in range(len(tmp_dist)) if tmp_dist[i] != '']
    
tally = 1
for t, d in zip(times, distances):
    tally*=find_num_solutions(t, d)
print(tally)