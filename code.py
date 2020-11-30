import numpy as np
import math

def room_to_source_coordinates(a, x1, x2, y1, y2):
    xcoord = 0
    ycoord = 0

    if a[0] % 2 == 0:
        xcoord = x1 + (2 * x2 + 2 * x1) * abs(a[0]) / 2
    else:
        xcoord = x1 + (2 * x2 + 2 * x1) * (abs(a[0]) - 1) / 2 + 2 * x2

    if a[0] < 0:
        xcoord = xcoord + a[0] * (x1 + x2) * 2

    if a[1] % 2 == 0:
        ycoord = y1 + (2 * y2 + 2 * y1) * abs(a[1]) / 2
    else:
        ycoord = y1 + (2 * y2 + 2 * y1) * (abs(a[1]) - 1) / 2 + 2 * y2
        
    if a[1] < 0:
        ycoord = ycoord + a[1] * (y1 + y2) * 2

    return [xcoord, ycoord]

def distance_and_angle(source_xcoord, source_ycoord, res_xcoord, res_ycoord):
    dx = source_xcoord - res_xcoord
    dy = source_ycoord - res_ycoord

    if dx >= 0 and dy >= 0:
        angle = math.atan(dx / dy)

    if dx >= 0 and dy < 0:
        angle = 90 - math.atan(dy / dx)

    if dx < 0 and dy < 0:
        angle = 180 + math.atan(dx / dy)

    if dx < 0 and dy >= 0:
        angle = 270 - math.atan(dy / dx)
    
    distance = math.sqrt(dx ** 2 + dy ** 2)

    return [distance, angle]

# Define rooms parameters and number of reflections
room_width = 7
room_length = 5

reflection_max = 5 #Maximala antalet reflektioner vi utvärderar för

# Define source, reciever and distances between them
source = [2, 1]
reveiver = [5, 3]

x1 = source[0]
x2 = room_width - source[0]

y1 = source[1]
y2 = room_length - source[1]

# generate "room-coordinates"
n = reflection_max  # Rumkoordinater från (-n,-n) till (n,n)
m = ((2 * n + 1) ** 2)  # Antal rum som genereras. 20% sorteras bort
spegelrum = np.zeros((m, 2))  # Tom lista över rumskoordinater

# Fyll listan med "rumskoordinater"
col = 0
for i in range(2 * n + 1):
    for j in range(2 * n + 1):
        spegelrum[col] = [i - n, j - n]
        col = col + 1

# för n = 1 (transponerat):
# -1    -1    -1     0     0     0     1     1     1
# -1     0     1    -1     0     1    -1     0     1

# Klassificerar vaje koordinatpar till ett visst antal reflektioner 
orderlist = abs(spegelrum[:, 0]) + abs(spegelrum[:, 1])

# för n = 1 (transponerat):
# 2     1     2     1     0     1     2     1     2

# Generate source coordinates

no_of_rays = 2 * (reflection_max ** 2 + reflection_max) + 1
no_of_reflections = np.zeros((no_of_rays, 1))

mirror_source_coordinates = np.zeros((no_of_rays, 2)) # Definierar vektor för alla kordinater
mirror_source_coordinates[0,:] = source
no_of_reflections[0] = 0 

ray_number = 0

for reflection in range(reflection_max + 1):
    ind_with_n_number_of_reflections = [i for i, x in enumerate(orderlist) if x == reflection]
    rooms_with_n_number_of_reflections = np.zeros((len(ind_with_n_number_of_reflections) ,2))
    for i in range(len(ind_with_n_number_of_reflections)):
        rooms_with_n_number_of_reflections[i,:] = spegelrum[ind_with_n_number_of_reflections[i],:]
    
    for sourceN in range(reflection * 4):
        ray_number = ray_number + 1
        room = rooms_with_n_number_of_reflections[sourceN,:]
        mirror_source_coordinates[ray_number,:] = room_to_source_coordinates(room,x1,x2,y1,y2)
        no_of_reflections[ray_number] = reflection
