import random

# Playlists
emotion = {
    "happy": ["Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors"],
    "sad": ["Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato"],
    "bad biatch": ["good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA"]
}
genre = {
    "US-UK Pop": ["Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore"],
    "Kpop": ["I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG"],
    "Vpop": ["Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE"]
}
anime = ["LOST IN PARADISE (Jujutsu Kaisen Ending Theme Song)","Guren no Yumiya - Linked Horizon","Kyouran Hey Kids!- Noragami","Moonlight Densetsu","Shinzo wo Sasageyo! by Linked Horizon","Suzume by RADWIMPS ft Toaka"]
games = ["Baba Yetu - Christopher Tin", "One-Winged Angel - Nobuo Uematsu", "The Last of Us - Gustavo Santaolalla", "Zelda's Lullaby - Koji Kondo", "Snake Eater - Cynthia Harrell"]
occasion = {
    "birthday": ["Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng"],
    "love anniversary": ["Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande"],
    "road trip": ["Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause"]
}
random_list = [
    "Mr. Blue Sky - Electric Light Orchestra", "New Light - John Mayer", "Party In The U.S.A - Miley Cyrus", "Mariposa - Peach Tree Rascals", "Best Day of My Life - American Authors",
    "Summertime Sadness - Lana Del Rey", "Slow Dancing In The Dark - Joji", "Before You Go - Lewis Capaldi", "The Night We Met - Lord Huron", "Stone Cold - Demi Lovato",
    "good 4 u - Olivia Rodrigo", "Better Than Revenge - Taylor Swift", "Fuck You - Lily Allen", "Sorry Not Sorry - Demi Lovato", "Primadona - MARINA",
    "Shape of You - Ed Sheeran", "Starboy - The Weekend", "Sucker - Jonas Brothers", "FRIENDS - Marshmallow, Anne-Marie", "Still Into You - Paramore",
    "I Got A Boy - Girls' Generation", "Fire - BTS", "Psycho - Red Velvet", "Power - EXO", "BANG BANG BANG - BIGBANG",
    "Muộn rồi mà sao còn - Sơn Tùng M-TP", "Trốn Tìm - Đen", "Gác Lại Âu Lo - Da LAB, Miu Lê", "Nàng Thơ - Hoàng Dũng", "Tình Bạn Diệu Kỳ - Ricky Star, AMEE",
    "Birthday - Katy Perry", "Birthday - Anne-Marie", "BIRTHDAY - SOMI", "Any song - ZICO", "Khúc hát mừng sinh nhật - Phan Đình Tùng",
    "Best Of You - Andy Grammer, Elle King", "LOVE - AILEE, CHEN", "You & Me - James TW", "Electric Love - BØRNS", "Dance To This - Troye Sivan, Ariana Grande",
    "Summer - Calvin Harris", "YOUTH - Troye Sivan", "Riptide - Vance Joy", "Shut Up and Dance - WALK UP THE MOON", "I'm on Top of The World - The World's Cause",
    "Unravel - TK from Ling tosite sigure", "Gurenge - LiSA", "Blue Bird - Ikimono Gakari", "Silhouette - Kana-Boon", "My Dearest - Supercell",
    "Baba Yetu - Christopher Tin", "One-Winged Angel - Nobuo Uematsu", "The Last of Us - Gustavo Santaolalla", "Zelda's Lullaby - Koji Kondo", "Snake Eater - Cynthia Harrell"
]

def main():
    '''Receive input from user to generate songs'''
    print("Welcome to the music recommender tool!")
    while True:
        try:
            num_song = int(input("(Enter 0 to stop) Number of songs to receive (1, 2, or 3): "))
            if num_song == 0:
                break
            if num_song not in range(1, 4):
                print("Number must be from 1 to 3. Please try again!")
                continue

            mode = get_mode()
            if mode:
                random_song(mode, num_song)
            print("")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
def get_mode():
    '''Ask user to choose a mode and validate input'''
    try:
        mode = int(input("There are 6 modes of song recommendation: 1 - Emotion, 2 - Genre, 3 - Occasion, 4 - Random, 5 - Anime, 6 - Games. Enter number of your choice: "))
        if mode not in range(1, 7):
            print("Number must be from 1 to 6. Please try again!")
            return None
        return mode
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def random_song(mode, num_song):
    '''Select song from chosen mode'''
    if mode == 4:
        print("Please enjoy the music:")
        for song in get_random_songs(random_list, num_song):
            print(song)
    elif mode == 5:
        print("Please enjoy music from the Anime playlist:")
        for song in get_random_songs(anime, num_song):
            print(song)
    elif mode == 6:
        print("Please enjoy music from the Games playlist:")
        for song in get_random_songs(games, num_song):
            print(song)
    else:
        sub_category = get_sub_category(mode)
        if sub_category:
            mode_dict = {
                1: emotion,
                2: genre,
                3: occasion
            }.get(mode)
            if sub_category in mode_dict:
                print(f"Please enjoy music from the {sub_category} playlist:")
                for song in get_random_songs(mode_dict[sub_category], num_song):
                    print(song)
            else:
                print(f"{sub_category} is not a valid sub-category. Please try again!")

def get_sub_category(mode):
    '''Get sub-category from user based on the selected mode'''
    sub_category_prompt = {
        1: 'There are "happy", "sad", and "bad biatch" songs. Enter one category: ',
        2: 'There are "US-UK Pop", "Kpop", and "Vpop" songs. Enter one category: ',
        3: 'There are "birthday", "love anniversary", and "road trip" songs. Enter one category: '
    }
    return input(sub_category_prompt[mode]).strip().lower()

def get_random_songs(song_list, num_song):
    '''Return a list of random songs without duplication'''
    return random.sample(song_list, num_song)

if __name__ == '__main__':
    main()
