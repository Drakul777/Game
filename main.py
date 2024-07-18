from player import Player
from game import Game
from monster import Monster
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

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #recuperer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l ensemble des images des groupes de monstres
    game.all_monsters.draw(screen)


    #vérifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    #mettre a jour l' ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            #détecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()