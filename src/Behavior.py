import P3


def behavior(boid):
    max_acc = 1
    r = 10
    nby = [other for other in boid.flock.boids if boid.id > other.id and boid.flock.distance_matrix[boid.id][other.id] <
           r or other.id > boid.id and boid.flock.distance_matrix[other.id][boid.id] < r]

    # collision avoidance
    threshold = 3
    avoid = [other for other in nby if boid.id > other.id and boid.flock.distance_matrix[boid.id][other.id] < threshold
             or other.id > boid.id and boid.flock.distance_matrix[other.id][boid.id] < threshold]
    v1 = P3.P3(0, 0, 0)
    for other in avoid:
        v1 += other.position.vectorTo(boid.position) * (1 / boid.position.distance(other.position))

    # velocity matching
    v2 = P3.P3(0, 0, 0)
    for b in nby:
        v2 += b.vel
    if len(nby) > 1:
        v2 *= 1/len(nby)

    # flock centering
    v3 = P3.P3(0, 0, 0)
    for b in nby:
        v3 += b.position
    if len(nby) > 1:
        v3 *= 1 / len(nby)  # might need parenthesis around division

    behavior_vel = 10*v1 + 1*v2 + 1*v3
    delta_vel = behavior_vel + -1 * boid.vel
    return P3.P3.normalize(delta_vel)