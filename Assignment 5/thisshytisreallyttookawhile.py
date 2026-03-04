#yea for real, it took me a while to figure it out (but not too long), i even ask Lam about it lol.
import random
def approximate_pi(total_points):
    inside_circle = 0

    for _ in range(total_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y < 1:
            inside_circle = inside_circle + 1
    pi_value = 4 * inside_circle / total_points
    return pi_value


points = int(input("random points? 🥴: "))
pi_approx = approximate_pi(points)
print("not accuracy pi:", pi_approx)
