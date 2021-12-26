import os

from ProgressTracker import ProgressTracker


class Entity:
    def __init__(self, tags):
        self.tags: dict = tags
        return

    def read(self, path, tracker: ProgressTracker = None):
        self.tags['size'] = os.path.getsize(path)
        self.tags['modified'] = os.path.getmtime(path)
        self.tags['created'] = os.path.getctime(path)
        self.tags['accessed'] = os.path.getatime(path)  # Thank you, DDLC modding interest
        for e in ['size', 'modified', 'created', 'accessed']:
            self.tags['content_' + e] = self.tags[e]
        if tracker is not None:
            tracker.update(self.tags['size']/10**6)
        else:
            print('???')
        return

    def raw_display(self, L, offset=0):
        L.append(' |' * offset + self.tags.get('name', 'file ???')) + '|' + self.tags.get('content_size', 'unknown')
        return


class Folder(Entity):
    def __init__(self, tags):
        super().__init__(tags)
        self.subfolders = dict()
        self.files = dict()
        if "folder_content" in tags:
            X = tags["folder_content"]
            self.subfolders = X[0]
            self.files = X[1]
        return

    def read(self, path, tracker: ProgressTracker = None):
        if not os.path.exists(path):
            for e in ['size', 'modified', 'created', 'accessed']:
                self.tags[e] = 0
                self.tags['content_' + e] = 0
            return
        super(Folder, self).read(path, tracker)
        try:
            X = os.listdir(path)
            for e in X:
                p = path + '/' + e
                isFile = os.path.isfile(p)
                if isFile:
                    newE = Entity({'name': e})
                    self.files[e] = newE
                else:
                    newE = Folder({'name': e})
                    self.subfolders[e] = newE
                newE.read(p,tracker)
                for f in ['size', 'modified', 'created', 'accessed']:
                    f2 = 'content_' + f
                    self.tags[f2] = max(self.tags[f2], newE.tags[f2])
        except PermissionError:
            pass
        return

    def raw_display(self, L, offset=0):
        s = ' |' * offset
        s2 = self.tags.get('name', 'folder ???')
        s3 = str(self.tags.get('content_size', 'unknown'))
        L.append(s + s2 + '|' + s3)
        for e in self.subfolders:
            E: Entity = self.subfolders[e]
            E.raw_display(L, offset + 1)
        return


def main():
    return


if __name__ == "__main__":
    main()
