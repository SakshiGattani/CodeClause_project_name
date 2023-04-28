import pygame
import os

pygame.init()
pygame.font.init()

# set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# set up font
font_small = pygame.font.SysFont("Arial", 16)
font_medium = pygame.font.SysFont("Arial", 24)
font_large = pygame.font.SysFont("Arial", 32)

# set up colors
color_white = (255, 255, 255)
color_black = (0, 0, 0)

# set up music
music_dir = "C:\\Users\\saksh\\Downloads\\Music Player\\"
music_files = os.listdir(music_dir)
music_files = [file for file in music_files if file.endswith(".mp3")]

# set up current song index
current_song = 0

# set up music player controls
playing = False

# main loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_SPACE:
                playing = not playing
                if playing:
                    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.stop()

            elif event.key == pygame.K_RIGHT:
                if current_song < len(music_files) - 1:
                    current_song += 1
                    if playing:
                        pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))
                        pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                if current_song > 0:
                    current_song -= 1
                    if playing:
                        pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song]))
                        pygame.mixer.music.play()

    # clear screen
    screen.fill(color_black)

    # draw current song name
    song_name_text = font_large.render(music_files[current_song], True, color_white)
    screen.blit(song_name_text, (20, 20))

    # draw play/pause status
    play_pause_text = font_medium.render("Playing" if playing else "Paused", True, color_white)
    screen.blit(play_pause_text, (20, 60))

    # draw instructions
    instructions_text1 = font_small.render("Press SPACE to play/pause.", True, color_white)
    instructions_text2 = font_small.render("Press LEFT/RIGHT arrow keys to switch songs.", True, color_white)
    screen.blit(instructions_text1, (20, 100))
    screen.blit(instructions_text2, (20, 120))

    # update display
    pygame.display.update()

# clean up
pygame.quit()