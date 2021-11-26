class QueueList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.kop = None
        self.staart = None

    def empty(self):
        return self.kop is None

    def enqueue(self, data):
        hulp = self.Knoop(data)
        if self.empty():
            self.kop = hulp
            self.staart = hulp
        else:
            self.staart.volgende = hulp
            self.staart = hulp

    def front(self):
        return self.kop.data

    def dequeue(self):
        x = self.kop.data
        if self.kop == self.staart:
            self.kop = None
            self.staart = None
        else:
            self.kop = self.kop.volgende
        return x

    def invert(self):
        if not self.empty():
            ref = self.kop
            vorige = None
            while ref.volgende is not None:
                volgende = ref.volgende
                ref.volgende = vorige
                vorige = ref
                ref = volgende
            ref.volgende = vorige
            hulp = self.kop
            self.kop = self.staart
            self.staart = hulp
            
            
            
            
            