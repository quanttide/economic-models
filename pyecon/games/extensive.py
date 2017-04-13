# -*-coding:utf-8-*-
# reference:
#   http://www.lyon0804.com/shu-xing-jie-gou-shu-ju-ke-shi-hua-zhan-shi.html
#   https://plot.ly/python/tree-plots/
#   http://pycallgraph.slowchop.com/en/master/

class ExtensiveGame(object):
    def __init__(self):
        pass

    def __str__(self):
        data = r"""
                Player 1
              /          \
             Up         Down
            /              \
        Player 2         Player 2
         /   \            /   \
       Left  Right      Left Right
      /       \         /       \
     (10)      (1)     (8)      (7)
     (10)      (8)     (1)      (7)
        """
        return data

    def __repr__(self):
        return self.__str__()

    def to_normal(self):
        pass