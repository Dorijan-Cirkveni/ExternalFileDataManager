import time


class ProgressTracker:
    def __init__(self, start=0, end=100, timeUpdate=10):
        self.start = start
        self.end = end
        self.timeUpdate = timeUpdate
        self.current = start
        self.t = time.time()
        self.start_time=self.t
        return

    def reset(self):
        self.current = self.start
        self.t = time.time()
        return

    def update(self, delta):
        current = self.current + delta
        t = time.time()
        dt = t - self.t
        if dt > self.timeUpdate:
            b = dt % self.timeUpdate
            a = dt - b
            self.t += a
            self.current = current
            print(self.current, self.t-self.start_time)
        return


def main():
    return


if __name__ == "__main__":
    main()
