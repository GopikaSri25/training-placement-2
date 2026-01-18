class MyCalendarTwo(object):

    def __init__(self):
        self.overlaping, self.non_overlaping = [], []

    def book(self, start, end):
        for s, e in self.overlaping:
            if start < e and end > s:
                return False

        for s, e in self.non_overlaping:
            if start < e and end > s:
                self.overlaping.append((max(start, s), min(e, end)))
        self.non_overlaping.append((start, end))
        return True
