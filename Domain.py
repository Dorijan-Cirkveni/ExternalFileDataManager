import re
from typing import List
from Entity import Entity


class Domain:
    def __init__(self, directory, entityList=None, depthLimit: int = 5):
        self.directory = directory
        self.indexCounter = 0
        self.root=None
        self.entityList = entityList
        if entityList is not None:
            self.rootEntity=entityList[0]
            return
        self.entityList = dict()
        if type(depthLimit) != int:
            raise Exception("Depth limit must be a non-negative integer for a determined depth limit"
                            " or a negative integer for a non-existent one.")


    def raw_display(self, filter_crit: callable, sort_crit: callable):
        L:List[Entity]=[e for e in self.entityList if filter_crit(e)]
        L.sort(key=sort_crit)
        return str(e)


def main():
    A = "12" \
        "34"
    print(A)
    return


if __name__ == "__main__":
    main()
