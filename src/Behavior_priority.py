import P3

def behavior(boid):
    max_acc = .1
    max_vel = 25
    r = 200
    nby = [other for other in boid.flock.boids if boid.id > other.id and boid.flock.distance_matrix[boid.id][other.id] <
           r or other.id > boid.id and boid.flock.distance_matrix[other.id][boid.id] < r]

    # collision avoidance
    r2 = 50
    avoid = [other for other in nby if boid.id > other.id and boid.flock.distance_matrix[boid.id][other.id] < r2
             or other.id > boid.id and boid.flock.distance_matrix[other.id][boid.id] < r2]
    v1 = P3.P3(0, 0, 0)
    for other in avoid:
        v1 += other.position - boid.position * (1 / boid.position.distance(other.position)**2)

    # velocity matching
    v2 = P3.P3(0, 0, 0)
    for b in nby:
        v2 += b.velocity
    if len(nby) > 1:
        v2 *= 1/len(nby)
    v2 -= boid.velocity

    # flock centering
    v3 = P3.P3(0, 0, 0)
    for b in nby:
        v3 += b.position
    if len(nby) > 1:
        v3 *= 1 / len(nby)
    v3 -= boid.position

    # Robin: Cod = .35, mass = 0.0182kg, density = 1.09kg/m^3, body frontal area = 4.6cm^2
    # c = coefficient of drag * density * perpendicular area * 1/2
    c = .0088 * 1
    drag = c * boid.velocity.distance()**2
    drag_vector = -1 * boid.velocity * drag

    delta_vel = 50*v1 + 800*v2 + 5000*v3  #  - drag_vector

    acc = P3.P3.normalize(delta_vel) * max_acc

    return acc if acc.distance() < delta_vel.distance() else delta_vel

# PRIORITY VECTORS, DESIRES:

def priority_behavior(boid):
    #max_acc = .1
    #max_vel = 25
    #r = 200
    #nby = [other for other in boid.flock.boids if boid.id > other.id and boid.flock.distance_matrix[boid.id][other.id] <
           #r or other.id > boid.id and boid.flock.distance_matrix[other.id][boid.id] < r]

    # Vector 1: Desire to be in middle of flock. As pv1
    # the difference between the mean position of the boids local neighbors
    # and the boids current position
    boidsp_sum = 0
    for x in nby: #?
        boidsp_sum += x
    mean_position = boidsp_sum / len(nby)
    pv1 = P3.P3(0, 0, 0)
    for x in nby: #?
        v1 = mean_position - boid.position

    # Vector 2: Desire to fly in same direction. As pv2
    # the difference between the mean velocity of the boids local neighbors
    # and the boids current velocity
    sum_vel = 0
    for x in nby:
        sum_vel += x.velocity
    mean_velocities = sum_vel/len(nby)
    pv2 = mean_velocities - boid.position

    # Vector 3: Obstacle avoidance. As pv3
    # a weighted sum of differences between close neighbors’ positions
    # and boids current position as well as differences from stationary objects
    diff_boids
    for x in nby:
        diff_boids = x - boid.position
    pv3 = 0


# END OF PRIORITY VECTORS
