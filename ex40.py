class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

day_o_lyrics = "Day-o, is a day-ay-ay-o, daylight come and me want to go home."
day_o_lyric_list = day_o_lyrics.split(',')
day_o = Song(day_o_lyric_list)

happy_bday = Song([ "Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally round the family",
                        "With pockets full of shells."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

day_o.sing_me_a_song()
