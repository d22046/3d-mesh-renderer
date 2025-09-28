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
unit_movement = 0

def initiatiate_tesseract():
    global unit_movement
    unit_movement = 0.1
    # For the tesseract.
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
    return [ a , b , c , d , e , f , g , h, i, j, k, l, m, n, o, p ]

def initiatiate_vertex_logo():
    global unit_movement
    unit_movement = 0.01
    # For VERTEX.
    v0 = Vertex(-1, -0.5, 0)  # 0
    v1 = Vertex(-0.8, -0.5, 0)  # 1
    v2 = Vertex(-0.7, -0.04, 0)  # 2
    v3 = Vertex(-0.6, -0.5, 0)  # 3
    v4 = Vertex(-0.4, -0.5, 0)  # 4
    v5 = Vertex(-0.6, 0.2, 0)  # 5
    v6 = Vertex(-0.8, 0.2, 0)  # 6
    v7 = Vertex(-1, -0.5, 0.2)  # 7
    v8 = Vertex(-0.8, -0.5, 0.2)  # 8
    v9 = Vertex(-0.7, -0.04, 0.2)  # 9
    v10 = Vertex(-0.6, -0.5, 0.2)  # 10
    v11 = Vertex(-0.4, -0.5, 0.2)  # 11
    v12 = Vertex(-0.6, 0.2, 0.2)  # 12
    v13 = Vertex(-0.8, 0.2, 0.2)  # 13
    e0 = Vertex(-0.25, -0.5, 0)  # 14
    e1 = Vertex(0.35, -0.5, 0)  # 15
    e2 = Vertex(0.35, -0.35, 0)  # 16
    e3 = Vertex(-0.05, -0.35, 0)  # 17
    e4 = Vertex(-0.05, -0.22, 0)  # 18
    e5 = Vertex(0.25, -0.22, 0)  # 19
    e6 = Vertex(0.25, -0.08, 0)  # 20
    e7 = Vertex(-0.05, -0.08, 0)  # 21
    e8 = Vertex(-0.05, 0.05, 0)  # 22
    e9 = Vertex(0.35, 0.05, 0)  # 23
    e10 = Vertex(0.35, 0.2, 0)  # 24
    e11 = Vertex(-0.25, 0.2, 0)  # 25
    e12 = Vertex(-0.25, -0.5, 0.2)  # 26
    e13 = Vertex(0.35, -0.5, 0.2)  # 27
    e14 = Vertex(0.35, -0.35, 0.2)  # 28
    e15 = Vertex(-0.05, -0.35, 0.2)  # 29
    e16 = Vertex(-0.05, -0.22, 0.2)  # 30
    e17 = Vertex(0.25, -0.22, 0.2)  # 31
    e18 = Vertex(0.25, -0.08, 0.2)  # 32
    e19 = Vertex(-0.05, -0.08, 0.2)  # 33
    e20 = Vertex(-0.05, 0.05, 0.2)  # 34
    e21 = Vertex(0.35, 0.05, 0.2)  # 35
    e22 = Vertex(0.35, 0.2, 0.2)  # 36
    e23 = Vertex(-0.25, 0.2, 0.2)  # 37
    r0 = Vertex(0.5, -0.5, 0)  # 38
    r1 = Vertex(0.9, -0.5, 0)  # 39
    r2 = Vertex(1.1, -0.35, 0)  # 40
    r3 = Vertex(1.1, -0.08, 0)  # 41
    r4 = Vertex(0.88, -0.08, 0)  # 42
    r5 = Vertex(1.1, 0.2, 0)  # 43
    r6 = Vertex(0.9, 0.2, 0)  # 44
    r7 = Vertex(0.7, -0.08, 0)  # 45
    r8 = Vertex(0.7, 0.2, 0)  # 46
    r9 = Vertex(0.5, 0.2, 0)  # 47
    r10 = Vertex(0.7, -0.35, 0)  # 48
    r11 = Vertex(0.85, -0.35, 0)  # 49
    r12 = Vertex(0.95, -0.27, 0)  # 50
    r13 = Vertex(0.95, -0.22, 0)  # 51
    r14 = Vertex(0.7, -0.22, 0)  # 52
    r15 = Vertex(0.5, -0.5, 0.2)  # 53
    r16 = Vertex(0.9, -0.5, 0.2)  # 54
    r17 = Vertex(1.1, -0.35, 0.2)  # 55
    r18 = Vertex(1.1, -0.08, 0.2)  # 56
    r19 = Vertex(0.88, -0.08, 0.2)  # 57
    r20 = Vertex(1.1, 0.2, 0.2)  # 58
    r21 = Vertex(0.9, 0.2, 0.2)  # 59
    r22 = Vertex(0.7, -0.08, 0.2)  # 60
    r23 = Vertex(0.7, 0.2, 0.2)  # 61
    r24 = Vertex(0.5, 0.2, 0.2)  # 62
    r25 = Vertex(0.7, -0.35, 0.2)  # 63
    r26 = Vertex(0.85, -0.35, 0.2)  # 64
    r27 = Vertex(0.95, -0.27, 0.2)  # 65
    r28 = Vertex(0.95, -0.22, 0.2)  # 66
    r29 = Vertex(0.7, -0.22, 0.2)  # 67
    t0 = Vertex(1.25, -0.5, 0)  # 68
    t1 = Vertex(1.85, -0.5, 0)  # 69
    t2 = Vertex(1.85, -0.35, 0)  # 70
    t3 = Vertex(1.65, -0.35, 0)  # 71
    t4 = Vertex(1.65, 0.2, 0)  # 72
    t5 = Vertex(1.45, 0.2, 0)  # 73
    t6 = Vertex(1.45, -0.35, 0)  # 74
    t7 = Vertex(1.25, -0.35, 0)  # 75
    t8 = Vertex(1.25, -0.5, 0.2)  # 76
    t9 = Vertex(1.85, -0.5, 0.2)  # 77
    t10 = Vertex(1.85, -0.35, 0.2)  # 78
    t11 = Vertex(1.65, -0.35, 0.2)  # 79
    t12 = Vertex(1.65, 0.2, 0.2)  # 80
    t13 = Vertex(1.45, 0.2, 0.2)  # 81
    t14 = Vertex(1.45, -0.35, 0.2)  # 82
    t15 = Vertex(1.25, -0.35, 0.2)  # 83
    _e0 = Vertex(2, -0.5, 0)  # 84
    _e1 = Vertex(2.6, -0.5, 0)  # 85
    _e2 = Vertex(2.6, -0.35, 0)  # 86
    _e3 = Vertex(2.2, -0.35, 0)  # 87
    _e4 = Vertex(2.2, -0.22, 0)  # 88
    _e5 = Vertex(2.5, -0.22, 0)  # 89
    _e6 = Vertex(2.5, -0.08, 0)  # 90
    _e7 = Vertex(2.2, -0.08, 0)  # 91
    _e8 = Vertex(2.2, 0.05, 0)  # 92
    _e9 = Vertex(2.6, 0.05, 0)  # 93
    _e10 = Vertex(2.6, 0.2, 0)  # 94
    _e11 = Vertex(2, 0.2, 0)  # 95
    _e12 = Vertex(2, -0.5, 0.2)  # 96
    _e13 = Vertex(2.6, -0.5, 0.2)  # 97
    _e14 = Vertex(2.6, -0.35, 0.2)  # 98
    _e15 = Vertex(2.2, -0.35, 0.2)  # 99
    _e16 = Vertex(2.2, -0.22, 0.2)  # 100
    _e17 = Vertex(2.5, -0.22, 0.2)  # 101
    _e18 = Vertex(2.5, -0.08, 0.2)  # 102
    _e19 = Vertex(2.2, -0.08, 0.2)  # 103
    _e20 = Vertex(2.2, 0.05, 0.2)  # 104
    _e21 = Vertex(2.6, 0.05, 0.2)  # 105
    _e22 = Vertex(2.6, 0.2, 0.2)  # 106
    _e23 = Vertex(2, 0.2, 0.2)  # 107

    x0 = Vertex(2.75, -0.5, 0)  # 108
    x1 = Vertex(2.95, -0.5, 0)  # 109
    x2 = Vertex(3.05, -0.22, 0)  # 110
    x3 = Vertex(3.15, -0.5, 0)  # 111
    x4 = Vertex(3.35, -0.5, 0)  # 112
    x5 = Vertex(3.22, -0.15, 0)  # 113
    x6 = Vertex(3.35, 0.2, 0)  # 114
    x7 = Vertex(3.15, 0.2, 0)  # 115
    x8 = Vertex(3.05, -0.08, 0)  # 116
    x9 = Vertex(2.95, 0.2, 0)  # 117
    x10 = Vertex(2.75, 0.2, 0)  # 118
    x11 = Vertex(2.88, -0.15, 0)  # 119

    x12 = Vertex(2.75, -0.5, 0.2)  # 120
    x13 = Vertex(2.95, -0.5, 0.2)  # 121
    x14 = Vertex(3.05, -0.22, 0.2)  # 122
    x15 = Vertex(3.15, -0.5, 0.2)  # 123
    x16 = Vertex(3.35, -0.5, 0.2)  # 124
    x17 = Vertex(3.22, -0.15, 0.2)  # 125
    x18 = Vertex(3.35, 0.2, 0.2)  # 126
    x19 = Vertex(3.15, 0.2, 0.2)  # 127
    x20 = Vertex(3.05, -0.08, 0.2)  # 128
    x21 = Vertex(2.95, 0.2, 0.2)  # 129
    x22 = Vertex(2.75, 0.2, 0.2)  # 130
    x23 = Vertex(2.88, -0.15, 0.2)  # 131

    return [
        v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13,
        e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23,
        r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14,
        r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29,
        t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,
        _e0, _e1, _e2, _e3, _e4, _e5, _e6, _e7, _e8, _e9, _e10, _e11, _e12, _e13, _e14, _e15, _e16, _e17, _e18, _e19, _e20, _e21, _e22, _e23,
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23
    ]

#Configure the mesh here. Vertex(x_pos, y_pos, z_pos)
def initiate():
    global vertices
    # NOTE: ALSO CHANGE DRAW...().
    # vertices = initiatiate_tesseract()
    vertices = initiatiate_vertex_logo()

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

def draw_tesseract():
    # For the tesseract.
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

def draw_vertex_logo():
    # For VERTEX.
    draw_line(0, 1)
    draw_line(1, 2)
    draw_line(2, 3)
    draw_line(3, 4)
    draw_line(4, 5)
    draw_line(5, 6)
    draw_line(6, 0)
    draw_line(7, 8)
    draw_line(8, 9)
    draw_line(9, 10)
    draw_line(10, 11)
    draw_line(11, 12)
    draw_line(12, 13)
    draw_line(13, 7)
    draw_line(0, 7)
    draw_line(1, 8)
    draw_line(2, 9)
    draw_line(3, 10)
    draw_line(4, 11)
    draw_line(5, 12)
    draw_line(6, 13)
    draw_line(14, 15)
    draw_line(15, 16)
    draw_line(16, 17)
    draw_line(17, 18)
    draw_line(18, 19)
    draw_line(19, 20)
    draw_line(20, 21)
    draw_line(21, 22)
    draw_line(22, 23)
    draw_line(23, 24)
    draw_line(24, 25)
    draw_line(14, 25)
    draw_line(26, 27)
    draw_line(27, 28)
    draw_line(28, 29)
    draw_line(29, 30)
    draw_line(30, 31)
    draw_line(31, 32)
    draw_line(32, 33)
    draw_line(33, 34)
    draw_line(34, 35)
    draw_line(35, 36)
    draw_line(36, 37)
    draw_line(37, 26)
    draw_line(14, 26)
    draw_line(15, 27)
    draw_line(16, 28)
    draw_line(17, 29)
    draw_line(18, 30)
    draw_line(19, 31)
    draw_line(20, 32)
    draw_line(21, 33)
    draw_line(22, 34)
    draw_line(23, 35)
    draw_line(24, 36)
    draw_line(25, 37)
    draw_line(38, 39)
    draw_line(39, 40)
    draw_line(40, 41)
    draw_line(41, 42)
    draw_line(42, 43)
    draw_line(43, 44)
    draw_line(44, 45)
    draw_line(45, 46)
    draw_line(46, 47)
    draw_line(38, 47)
    draw_line(48, 49)
    draw_line(49, 50)
    draw_line(50, 51)
    draw_line(51, 52)
    draw_line(52, 48)
    draw_line(53, 54)
    draw_line(54, 55)
    draw_line(55, 56)
    draw_line(56, 57)
    draw_line(57, 58)
    draw_line(58, 59)
    draw_line(59, 60)
    draw_line(60, 61)
    draw_line(61, 62)
    draw_line(62, 53)
    draw_line(63, 64)
    draw_line(64, 65)
    draw_line(65, 66)
    draw_line(66, 67)
    draw_line(67, 63)
    draw_line(38, 53)
    draw_line(39, 54)
    draw_line(40, 55)
    draw_line(41, 56)
    draw_line(42, 57)
    draw_line(43, 58)
    draw_line(44, 59)
    draw_line(45, 60)
    draw_line(46, 61)
    draw_line(47, 62)
    draw_line(48, 63)
    draw_line(49, 64)
    draw_line(50, 65)
    draw_line(51, 66)
    draw_line(52, 67)
    draw_line(68, 69)
    draw_line(69, 70)
    draw_line(70, 71)
    draw_line(71, 72)
    draw_line(72, 73)
    draw_line(73, 74)
    draw_line(74, 75)
    draw_line(75, 68)
    draw_line(76, 77)
    draw_line(77, 78)
    draw_line(78, 79)
    draw_line(79, 80)
    draw_line(80, 81)
    draw_line(81, 82)
    draw_line(82, 83)
    draw_line(83, 76)
    draw_line(68, 76)
    draw_line(69, 77)
    draw_line(70, 78)
    draw_line(71, 79)
    draw_line(72, 80)
    draw_line(73, 81)
    draw_line(74, 82)
    draw_line(75, 83)
    draw_line(84, 85)
    draw_line(85, 86)
    draw_line(86, 87)
    draw_line(87, 88)
    draw_line(88, 89)
    draw_line(89, 90)
    draw_line(90, 91)
    draw_line(91, 92)
    draw_line(92, 93)
    draw_line(93, 94)
    draw_line(94, 95)
    draw_line(95, 84)
    draw_line(96, 97)
    draw_line(97, 98)
    draw_line(98, 99)
    draw_line(99, 100)
    draw_line(100, 101)
    draw_line(101, 102)
    draw_line(102, 103)
    draw_line(103, 104)
    draw_line(104, 105)
    draw_line(105, 106)
    draw_line(106, 107)
    draw_line(107, 96)
    draw_line(84, 96)
    draw_line(85, 97)
    draw_line(86, 98)
    draw_line(87, 99)
    draw_line(88, 100)
    draw_line(89, 101)
    draw_line(90, 102)
    draw_line(91, 103)
    draw_line(92, 104)
    draw_line(93, 105)
    draw_line(94, 106)
    draw_line(95, 107)
    draw_line(108, 109)
    draw_line(109, 110)
    draw_line(110, 111)
    draw_line(111, 112)
    draw_line(112, 113)
    draw_line(113, 114)
    draw_line(114, 115)
    draw_line(115, 116)
    draw_line(116, 117)
    draw_line(117, 118)
    draw_line(118, 119)
    draw_line(119, 108)
    draw_line(120, 121)
    draw_line(121, 122)
    draw_line(122, 123)
    draw_line(123, 124)
    draw_line(124, 125)
    draw_line(125, 126)
    draw_line(126, 127)
    draw_line(127, 128)
    draw_line(128, 129)
    draw_line(129, 130)
    draw_line(130, 131)
    draw_line(131, 120)
    draw_line(108, 120)
    draw_line(109, 121)
    draw_line(110, 122)
    draw_line(111, 123)
    draw_line(112, 124)
    draw_line(113, 125)
    draw_line(114, 126)
    draw_line(115, 127)
    draw_line(116, 128)
    draw_line(117, 129)
    draw_line(118, 130)
    draw_line(119, 131)

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

    # draw_tesseract()
    draw_vertex_logo()

    #------------------------

    pygame.display.update ()
    clock.tick ( 60 )
