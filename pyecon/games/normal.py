# -*-coding:utf-8-*-

from __future__ import print_function


class NormalGame(object):
    def __init__(self):
        self.players = ['Player1','Player2','Player3']
        self.actions = {
            'Player1': ['U','D'],
            'Player2': ['L','M','R'],
            'Player3': ['T','B'],
        }
        self.payoffs = [
             [
              [(1,2,5),(0,0,9),(3,-1,10)],
              [(0,0,7),(2,1,13),(3,-2,12)],
             ],
             [
              [(0,0,6),(2,1,8),(-1,0,11)],
              [(1,2,8),(0,0,6),(-2,0,12)],
             ]
            ]



    def __str__(self):
        data = '''
        When Player 3 plays "T":
                             Player 2
                        L        M        R
                   U (1,2,5)  (0,0,9)  (3,-1,10)
          Player 1
                   D (0,0,7)  (2,1,13) (3,-2,12)

        When Player 3 plays "B":
                                     Player 2
                        L        M        R
                   U (0,0,6)  (2,1,8)  (-1,0,11)
          Player 1
                   D (1,2,8)  (0,0,6) (-2,0,12)
        '''
        return data


    def __repr__(self):
        return self.__str__()

    def to_extensive(self):
        pass


if __name__=="__main__":
    game = NormalGame()
    print(game)


