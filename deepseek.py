import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Rotating Triangle")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Triangle parameters (local coordinates, centered at origin)
local_vertices = [
    (0, -100),
    (86.6, 50),
    (-86.6, 50)
]
screen_center = (WIDTH // 2, HEIGHT // 2)

# Rotation variables
angle = 0
rotation_speed = math.radians(1)  # 1 degree per frame

# Ball parameters
ball_radius = 10
ball_color = RED
ball_pos = [screen_center[0], screen_center[1]]
ball_velocity = [3, 3]  # Initial velocity

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rotation angle
    angle += rotation_speed
    angle %= 2 * math.pi  # Keep angle within 0-2π

    # Rotate and translate triangle vertices
    rotated_vertices = []
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    for x, y in local_vertices:
        rx = x * cos_angle - y * sin_angle + screen_center[0]
        ry = x * sin_angle + y * cos_angle + screen_center[1]
        rotated_vertices.append((rx, ry))

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check collisions with each edge
    for i in range(3):
        p1 = rotated_vertices[i]
        p2 = rotated_vertices[(i + 1) % 3]

        # Edge vector components
        edge_x = p2[0] - p1[0]
        edge_y = p2[1] - p1[1]

        # Calculate outward normal vector
        normal_x = edge_y
        normal_y = -edge_x
        length = math.hypot(normal_x, normal_y)
        if length == 0:
            continue
        normal_x /= length
        normal_y /= length

        # Calculate signed distance from ball to edge
        vec_x = ball_pos[0] - p1[0]
        vec_y = ball_pos[1] - p1[1]
        distance = vec_x * normal_x + vec_y * normal_y

        # Handle collision
        if distance < ball_radius:
            # Reflect velocity vector
            dot_product = ball_velocity[0] * normal_x + ball_velocity[1] * normal_y
            ball_velocity[0] -= 2 * dot_product * normal_x
            ball_velocity[1] -= 2 * dot_product * normal_y

            # Reposition ball to prevent sticking
            penetration = ball_radius - distance
            ball_pos[0] += penetration * normal_x
            ball_pos[1] += penetration * normal_y

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.polygon(screen, WHITE, rotated_vertices, 2)
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()