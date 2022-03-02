import os
import re
from typing import List
from Entity import Entity, Folder
from ProgressTracker import ProgressTracker


class Location:
    def __init__(self, current, trace=None):
        trace: List[Folder]
        if trace is None:
            trace = []
        self.current: Folder = current
        self.trace: List[Folder] = trace
        return

    def print_current(self, filter=3, tags=None):
        if tags is None:
            tags = {'size'}
        if filter & 1 != 0:
            for e in self.current.files:
                e: Entity
                print(e, {f: e.tags[f] for f in tags})
        if filter & 1 != 0:
            for e in self.current.files:
                e: Folder
                print(e, {f: e.tags[f] for f in tags})

    def outer(self):
        if len(self.trace)==0:
            return None
        ret = self.current
        self.current = self.trace.pop()
        return ret

    def inner(self, nxt: Folder):
        self.trace.append(self.current)
        self.current = nxt
        return

    def open_folder(self, name):
        X = self.current.subfolders
        if name not in X:
            raise FileNotFoundError
        self.inner(X[name])
        return


class Domain:
    def __init__(self, directory, tracker=None):
        self.directory = directory
        self.root = Folder({})
        self.root.read(directory,tracker)
        return

    def import_data(self, filename):
        return

    def raw_display(self, filter_crit: callable = None, sort_crit: callable = None):
        L = []
        self.root.raw_display(L)
        return "\n".join(L)


def main():
    path = "C:/Projects"  # "Projects/ExternalFileDataManager/TEST"
    # TODO implement subdirectory metadata storage
    X = Domain(path, ProgressTracker(0,10**6,1))
    C = Location(X.root)
    while True:
        order=input('>>>').split(' ')
        if order[0]=='end':
            break
        elif order[0]=='return':
            res=C.outer()
            print(res)
        elif order[0]=='open_folder':
            C.open_folder(order[1])
        else:
            print('Not a valid command.')
            pass
    return


if __name__ == "__main__":
    main()
