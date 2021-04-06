from objects import *

vertices = [] #A list to store all the vertices
focal_point = [0, 0, 1] #3D x, y, z pos for camera

turn_left = False
turn_right = False
turn_up = False
turn_down = False
forward = False
backward = False
upward = False
downward = False
leftward = False
rightward = False
unit_movement = 0.1

#Configure the mesh here. Vertex(x_pos, y_pos, z_pos)
def initiate():

    a = Vertex ( 3 , 3 , -9 )
    b = Vertex ( 3 , -3 , -9 )
    c = Vertex ( -3 , 3 , -9 )
    d = Vertex ( -3 , -3 , -9 )
    e = Vertex ( 3 , 3 , -3 )
    f = Vertex ( 3 , -3 , -3 )
    g = Vertex ( -3 , 3 , -3 )
    h = Vertex ( -3 , -3 , -3 )
    i = Vertex ( 1 , 1 , -7 )
    j = Vertex ( 1 , -1 , -7 )
    k = Vertex ( -1 , 1 , -7 )
    l = Vertex ( -1 , -1 , -7 )
    m = Vertex ( 1 , 1 , -5 )
    n = Vertex ( 1 , -1 , -5 )
    o = Vertex ( -1 , 1 , -5 )
    p = Vertex ( -1 , -1 , -5 )

    global vertices
    vertices = [ a , b , c , d , e , f , g , h, i, j, k, l, m, n, o, p ]

def draw_vertex(vertex, color):
    if -(vertex.z) == focal_point[2]:
        pygame.draw.circle(dis, color, [middle_x + vertex.x * 0.5 * scaler, middle_y + vertex.y * 0.5 * scaler], 1)

    elif vertex.z <= 0:
        proportion = 1 - vertex.z/(vertex.z - focal_point[2])   #calculate how much to shrink both the 3D x and y to fit on a 2D screen
        vertex.flat_x = vertex.x * proportion
        vertex.flat_y = vertex.y * proportion
        pygame.draw.circle(dis, color, [middle_x + vertex.flat_x * scaler, middle_y + vertex.flat_y * scaler], 1)


def draw_line(v1, v2):  #taking in two ints, the index of vertex 1 & vertex 2 in vertices

    #case 1: both vertices are visible with camera.
    if vertices[v1].z <= 0 and vertices[v2].z <= 0:
        pygame.draw.line(dis, green, [middle_x + vertices[v1].flat_x * scaler, middle_y + vertices[v1].flat_y * scaler],
                                     [middle_x + vertices[v2].flat_x * scaler, middle_y + vertices[v2].flat_y * scaler], 1)

    #case 2: vertex 1 is not visible.
    elif vertices[v1].z > 0 and vertices[v2].z <= 0:
        ratio = -vertices[v2].z / (vertices[v1].z - vertices[v2].z)
        dx = vertices[v2].x + (vertices[v1].x - vertices[v2].x) * ratio
        dy = vertices[v2].y + (vertices[v1].y - vertices[v2].y) * ratio
        temp = Vertex(dx, dy, 0)
        draw_vertex(temp, yellow)
        pygame.draw.line(dis, green, [middle_x + temp.flat_x * scaler, middle_y + temp.flat_y * scaler],
                                     [middle_x + vertices[v2].flat_x * scaler, middle_y + vertices[v2].flat_y * scaler], 1)

    #case 3: vertex 2 is not visible. Identical to case 2, only v1 and v2 swapped positions.
    elif vertices[v1].z <= 0 and vertices[v2].z > 0:
        ratio = -vertices[v1].z / (vertices[v1].z - vertices[v2].z)
        dx = vertices[v1].x + (vertices[v1].x - vertices[v2].x) * ratio
        dy = vertices[v1].y + (vertices[v1].y - vertices[v2].y) * ratio
        temp = Vertex(dx, dy, 0)
        draw_vertex(temp, yellow)
        pygame.draw.line(dis, green, [middle_x + temp.flat_x * scaler, middle_y + temp.flat_y * scaler ] ,
                                     [middle_x + vertices[v1].flat_x * scaler, middle_y + vertices[v1].flat_y * scaler], 1)

    #case 4: both vertex not visible, simply do nothing.
    else:
        pass


initiate()
while True:
    dis.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                initiate()
            if event.key == pygame.K_LEFT:
                turn_left = 1
            elif event.key == pygame.K_RIGHT:
                turn_right = 1
            if event.key == pygame.K_UP:
                turn_up = 1
            elif event.key == pygame.K_DOWN:
                turn_down = 1
            if event.key == pygame.K_w:
                forward = 1
            elif event.key == pygame.K_s:
                backward = 1
            if event.key == pygame.K_a:
                leftward = 1
            elif event.key == pygame.K_d:
                rightward = 1
            if event.key == pygame.K_SPACE:
                upward = 1
            elif event.key == pygame.K_f:
                downward = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                turn_left = 0
            if event.key == pygame.K_RIGHT:
                turn_right = 0
            if event.key == pygame.K_UP:
                turn_up = 0
            if event.key == pygame.K_DOWN:
                turn_down = 0
            if event.key == pygame.K_w:
                forward = 0
            elif event.key == pygame.K_s:
                backward = 0
            if event.key == pygame.K_a:
                leftward = 0
            elif event.key == pygame.K_d:
                rightward = 0
            if event.key == pygame.K_SPACE:
                upward = 0
            elif event.key == pygame.K_f:
                downward = 0

    if backward and not forward:
        for v in vertices:
            v.z -= unit_movement
    elif forward and not backward:
        for v in vertices:
            v.z += unit_movement
    if downward and not upward:
        for v in vertices:
            v.y -= unit_movement
    elif upward and not downward:
        for v in vertices:
            v.y += unit_movement
    if leftward and not rightward:
        for v in vertices:
            v.x += unit_movement
    elif rightward and not leftward:
        for v in vertices:
            v.x -= unit_movement

    # x' = x * cos(Θ) - y * sin(Θ)
    # y' = x * sin(Θ) + y * cos(Θ)
    if turn_left and not turn_right:
        for v in vertices:
            v.x = v.x * pCos_x - v.z * pSin_x
            v.z = v.x * pSin_x + v.z * pCos_y
    elif turn_right and not turn_left:
        for v in vertices:
            v.x = v.x * nCos_x - v.z * nSin_x
            v.z = v.x * nSin_x + v.z * nCos_x
    if turn_up and not turn_down:
        for v in vertices:
            v.y = v.y * pCos_y - v.z * pSin_y
            v.z = v.y * pSin_y + v.z * pCos_y
    elif turn_down and not turn_up:
        for v in vertices:
            v.y = v.y * nCos_y - v.z * nSin_y
            v.z = v.y * nSin_y + v.z * nCos_y

    for vertex in vertices:
        draw_vertex(vertex, red)

    #connect the vertexs here.
    draw_line ( 0 , 1 )
    draw_line ( 0 , 2 )
    draw_line ( 3 , 1 )
    draw_line ( 3 , 2 )
    draw_line ( 4 , 5 )
    draw_line ( 4 , 6 )
    draw_line ( 7 , 5 )
    draw_line ( 7 , 6 )
    draw_line ( 0 , 4 )
    draw_line ( 1 , 5 )
    draw_line ( 2 , 6 )
    draw_line ( 3 , 7 )

    draw_line ( 8 , 9 )
    draw_line ( 8 , 10 )
    draw_line ( 11 , 9 )
    draw_line ( 11 , 10 )
    draw_line ( 12 , 13 )
    draw_line ( 12 , 14 )
    draw_line ( 15 , 13 )
    draw_line ( 15 , 14 )
    draw_line ( 8 , 12 )
    draw_line ( 9 , 13 )
    draw_line ( 10 , 14 )
    draw_line ( 11 , 15 )

    draw_line(0, 8)
    draw_line(1, 9)
    draw_line(2, 10)
    draw_line(3, 11)
    draw_line(4, 12)
    draw_line(5, 13)
    draw_line(6, 14)
    draw_line(7, 15)
    #------------------------

    pygame.display.update ()
    clock.tick ( 60 )