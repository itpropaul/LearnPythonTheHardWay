class Song(object):
    
    def __init__(self, lyrics='test'):  # the ='test' is a way to give this variable a default value otherwise it errors upon creating an object w/o 2(self is considered the first and automatic argument) arguments, but maybe an error is good for debugging...
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
test = Song()  # I added this after the fact to go along with my first comment

test.sing_me_a_song()
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
