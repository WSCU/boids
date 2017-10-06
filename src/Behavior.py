import P3


def behavior(boid):
<<<<<<< HEAD
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
=======
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
>>>>>>> master

    # velocity matching
    v2 = P3.P3(0, 0, 0)
    for b in nby:
<<<<<<< HEAD
        v2 += b.vel
    if len(nby) > 1:
        v2 *= 1/len(nby)
=======
        v2 += b.velocity
    if len(nby) > 1:
        v2 *= 1/len(nby)
    v2 -= boid.velocity
>>>>>>> master

    # flock centering
    v3 = P3.P3(0, 0, 0)
    for b in nby:
        v3 += b.position
    if len(nby) > 1:
<<<<<<< HEAD
        v3 *= 1 / len(nby)  # might need parenthesis around division

    behavior_vel = 10*v1 + 1*v2 + 1*v3
    delta_vel = behavior_vel + -1 * boid.vel
    return P3.P3.normalize(delta_vel)
=======
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
>>>>>>> master
