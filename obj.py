
class Square:
    def __init__(self):
        self.index = None
        self.chiefs = None
        self.eagles = None
        self.owner = None
        self.note = None

    def set_index(self, index):
        self.index = index

    def set_chiefs(self,c):
        self.chiefs = c

    def set_eagles(self,e):
        self.eagles = e

    def set_owner(self,o):
        self.owner = o

    def set_note(self,n):
        self.note = n

    def get_chiefs(self):
        return self.chiefs

    def get_eagles(self):
        return self.eagles


    def __str__(self):
        print(f"{self.index:5}\t{self.chiefs:5}\t{self.eagles:5}\t{self.owner:20}\t{self.note}",end="")
        return ""

class Board:
    def __init__(self):
        self.board = []
        for s in range(0,101):
            square = Square()
            square.set_index(s)

            self.board.append(square)

    def __str__(self):
        print(f"i\tc\te\towner")
        for s in range(0,11):
            print(self.board[s])
        return ""

    def set_square(self,i,c,e,o):
        s = self.board[i]
        s.set_chiefs(c)
        s.set_eagles(e)
        s.set_owner(o)

    def get_square(self,c,e):
        if c > 9:
            c = c % 10
        if e > 9:
            e = e % 10
        for s in self.board:
            if (s.get_chiefs()) == c and (s.get_eagles() == e):
                return s

    def get_score(self,chiefs,eagles,note):
        for s in self.board:
            if (s.get_chiefs()) == chiefs%10 and (s.get_eagles() == eagles%10):
                s.set_note(note)
                return s



