# -*-coding:utf-8-*-


class PyEconObject(object):
    pass


class EconModel(PyEconObject):
    def __init__(self, *args, **kargs):
    	pass

    # -----economic environment-----
    def market_extent(self, *args, **kargs):
    	pass

    def institution(self,*args,**kargs):
    	pass

    def actors(self,*args,**kargs):
    	pass

    def information(self,*arg,**kargs):
    	pass

    # -----primitives-----
    def technologies(self,*arg,**kargs):
    	pass

    def preferences(self,*arg,**kargs):
    	pass

    def endowments(self,*arg,**kargs):
    	pass

    # ......


class MicroModel(EconModel):
    pass


class Market(MicroModel):
    pass


class MacroModel(EconModel):
    pass


class GameTheoryModel(MicroModel):
    pass


class NormalGame(GameTheoryModel):
    pass


class ExtensiveGame(GameTheoryModel):
    pass


class EconGrowthModel(MacroModel):
    pass
