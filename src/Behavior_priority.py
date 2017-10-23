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

def alpha(curr,new):
    return (-P3.dot(curr,new) + math.sqrt(P3.dot(curr,new)**2 - P3.dot(new,new)*(P3.dot(curr,curr)-max_acc^2))/P3.dot(new,new)

def priority_behavior(boid):
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
        v1 += other.position - boid.position * (1 / boid.position.distance(other.position) ** 2)

    # velocity matching
    v2 = P3.P3(0, 0, 0)
    for b in nby:
        v2 += b.velocity
    if len(nby) > 1:
        v2 *= 1 / len(nby)
    v2 -= boid.velocity

    # flock centering
    v3 = P3.P3(0, 0, 0)
    for b in nby:
        v3 += b.position
    if len(nby) > 1:
        v3 *= 1 / len(nby)
    v3 -= boid.position

    #scalling temp

    v1 *= 0.00001
    v2 *= 0.00002
    v3 *= 0.001

    res = v1  # res includes only v1
    # res *= 1 / 100
    print("bringing in v1: {} ".format(v1.distance()))



    if res.distance() > max_acc:
        res = (max_acc / res.distance()) * res
        return res
    print("bringing in v2: {} ".format(v2.distance()))
    alpha1 = (-2 * (P3.dot(v1, v2)) + math.sqrt(math.pow((2 * P3.dot(v1, v2)), 2) + (4 * (P3.dot(v2, v2))) * (math.pow(max_acc, 2) - P3.dot(v1, v2)))) / 2 * P3.dot(v2, v2)
    alpha1 = alpha(res,v2)
    print(alpha1)
    if alpha1 < 1:
        return res + alpha1 *v2
    res = res + v2
    print("Bringing in v3: ".format(v3.distance()))

    alpha2 = (-2 * (P3.dot(res, v3)) + math.sqrt(math.pow((2 * P3.dot(res, v3)), 2) + (4 * (P3.dot(v3, v3))) * (math.pow(max_acc, 2) - P3.dot(res, v3)))) / 2 * P3.dot(v3, v3)
    alpha2 = alpha(res,v3)
    if alpha2 < 1:
        return res + alpha2 * v3
    else:
        print("in else")
        return res +v3

# END OF PRIORITY VECTORS
