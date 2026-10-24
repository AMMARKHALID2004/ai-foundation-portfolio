class CountUp_Iterator:
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start>=self.iterable.end:
            raise StopIteration
        current=self.iterable.start
        self.iterable.start+=1
        return current

        