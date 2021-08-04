class Entity:
    def __init__(self, tags):
        self.tags: dict = tags
        return

    def raw_display(self):
        return self.tags.get("name", "Unnamed file???")


class Folder(Entity):
    def __init__(self, tags):
        super().__init__(tags)
        self.subfolders = dict()
        self.files = dict()
        if "folder_content" in tags:
            X = tags["folder_content"]
            self.subfolders = X[0]
            self.files = X[1]

    def raw_display(self):
        return self.tags.get("name", "Unnamed folder???")


def main():
    return


if __name__ == "__main__":
    main()
