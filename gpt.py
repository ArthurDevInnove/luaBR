import pygame
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Triangle settings
triangle_center = (WIDTH // 2, HEIGHT // 2)
triangle_radius = 200
triangle_angle = 0
triangle_speed = 0.01  # Rotation speed

# Ball settings
ball_radius = 10
ball_pos = [WIDTH // 2, HEIGHT // 2 - 50]
ball_velocity = [2, -2]

# Function to get triangle vertices
def get_triangle_vertices(center, radius, angle):
    return [
        (
            center[0] + radius * math.cos(angle + i * 2 * math.pi / 3),
            center[1] + radius * math.sin(angle + i * 2 * math.pi / 3),
        )
        for i in range(3)
    ]

# Function to check if point is inside the triangle
def point_in_triangle(p, a, b, c):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    b1 = sign(p, a, b) < 0.0
    b2 = sign(p, b, c) < 0.0
    b3 = sign(p, c, a) < 0.0
    
    return (b1 == b2) and (b2 == b3)

running = True
while running:
    screen.fill((0, 0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rotate triangle
    triangle_angle += triangle_speed
    triangle_vertices = get_triangle_vertices(triangle_center, triangle_radius, triangle_angle)
    
    # Move ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]
    
    # Collision detection
    if not point_in_triangle(ball_pos, *triangle_vertices):
        ball_velocity[0] = -ball_velocity[0]
        ball_velocity[1] = -ball_velocity[1]
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]
    
    # Draw triangle
    pygame.draw.polygon(screen, (0, 255, 0), triangle_vertices, 2)
    
    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
