# pip install pygame

import pygame


class Circle:

    def __init__(self, x, y, radius, color, alpha=255):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.alpha = alpha

    def draw(self, screen: pygame.Surface):

        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        pygame.draw.circle(surface, (*self.color, self.alpha), (self.radius, self.radius), self.radius)

        screen.blit(surface, (self.x - self.radius, self.y - self.radius))


    def move(self, dx, dy):
        self.x += dx
        self.y += dy


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    player =  Circle(50, 50, 20, (255, 0, 0), 120)
    target =  Circle(width//2, height//2, 30, (0, 255, 0), 120)

    running = True
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('Arial', 30)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        speed = 5
        dx, dy = 0, 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx = -speed
        if keys[pygame.K_RIGHT]:
            dx = speed
        if keys[pygame.K_UP]:
            dy = -speed
        if keys[pygame.K_DOWN]:
            dy = speed

        player.move(dx, dy)
        screen.fill((255, 255, 255))
        player.draw(screen)
        target.draw(screen)

        if player == target:
            text = font.render("IDEALNIE", True, (0, 255, 0))
            text_rect = text.get_rect(center=(width//2, 50))
            screen.blit(text, text_rect)


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

main()