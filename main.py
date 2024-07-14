from game import Game
import pygame
pygame.init()


# creer une premiere classe qui va representer le joueur

#générer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#importer l'arriere plan du jeu
background = pygame.image.load('PygameAssets-main/bg.jpg')

#charger le jeu
game = Game()

running = True

# boucle tant que cette condition est vraie

while running:

    #appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    #appliquer l image du joueur
    screen.blit(game.player.image, game.player.rect)

    #mettre a jour notre ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")