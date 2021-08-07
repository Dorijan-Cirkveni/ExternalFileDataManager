import os
import re
from typing import List
from Entity import Entity


class Domain:
    def __init__(self, directory, entityList=None, depthLimit: int = 5):
        self.directory = directory
        self.indexCounter = 0
        self.root = None
        self.entityList = entityList
        if entityList is not None:
            self.rootEntity = entityList[0]
            return
        self.entityList = dict()
        if type(depthLimit) != int:
            raise Exception("Depth limit must be a non-negative integer for a determined depth limit"
                            " or a negative integer for a non-existent one.")
        while depthLimit!=0:
        X = os.listdir(directory)
        self.entityList = {e: Entity({"name": e}) for e in X}
    def import_data(self,filename):



    def raw_display(self, filter_crit: callable = None, sort_crit: callable = None, depth=0):
        if filter_crit is None:
            filter_crit = lambda e, v: True
        if sort_crit is None:
            sort_crit = lambda x: 0
        L: List[Entity] = [(e, v) for (e, v) in self.entityList.items() if filter_crit(e, v)]
        L.sort(key=sort_crit)
        return "\n".join([e[0] for e in L])


def main():
    path = "C:\DDLC\my_mods\TMIWNHANDANHHTHTYVM\game"
    X = Domain(path)
    print(X.raw_display())
    return


if __name__ == "__main__":
    main()
