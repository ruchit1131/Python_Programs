class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday=Song(["Happy birthday to you","May god bless you","You live in a zoo"])
jhonny_jhonny=Song(["Jhonny Jhoony","Yes papa", "Eating sugar","No papa","Telling lies","No papa","Open your mouth","HA HA HA"])

happy_bday.sing_me_a_song()
jhonny_jhonny.sing_me_a_song()
