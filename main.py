import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder,song_name):
    file_path=os.path.join(folder,song_name)
    if  not os.path.exists(file_path):
        print("File not found")
        return
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"\nNow playing: {song_name}")
    print("commands:[P]ause,[R]esume,[S]top")

    while True:
        command=input("> ").upper()
        if command=='P':
            pygame.mixer.music.pause()
            print("Music paused")
        elif command=='R':
            pygame.mixer.music.unpause()
            print("Music resumed")
        elif command=='S':
            pygame.mixer.music.stop()
            print("Music stopped")
            break
        else:
            print("Invalid command")
def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio intialization failed:", e)
        return 
    folder="songs"
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")
        return
    mp3_files=[file for file in os.listdir(folder) if file.endswith(".mp3")]


    if not mp3_files:
        print("No mp3 files found in the folder.")
    
    while True:
        print("*****MP3 PLAYER*****")
        print("My Song List")

        for index,song in enumerate(mp3_files,start=1):
            print(f"{index}.{song}")
        
        choice_input=input("\nEnter the song # to play(or 'Q'to quiet):")
        if(choice_input.upper()=='Q'):
            print("Exiting the player. Goodbye!")
            break
        if not choice_input.isdigit():
            print("Enter a valid input.") 
            continue

        choice=int(choice_input)-1
        if  0 <= choice < len(mp3_files): 
            play_music(folder,mp3_files[choice])
        else:
            print("invalid choice")
        
if __name__ == "__main__":
    main()
