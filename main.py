import pygame
from binary_tree import Node

pygame.init()
window = pygame.display.set_mode((800, 600))

# Need to update this to take users input
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

def draw_tree(node, x, y):
    if node:
        pygame.draw.circle(window, (0,128,128), (x, y), 30)
        font = pygame.font.Font(None, 20)
        text = font.render(str(node.root), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        window.blit(text, text_rect)
        if node.left:
            pygame.draw.line(window, (0,128,128), (x, y-15), (x-50, y+50))
            draw_tree(node.left, x-50, y+50)
        if node.right:
            pygame.draw.line(window, (0,128,128), (x, y-15), (x+50, y+50))
            draw_tree(node.right, x+50, y+50)



def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((0, 0, 0))
        draw_tree(root, 400, 50)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
