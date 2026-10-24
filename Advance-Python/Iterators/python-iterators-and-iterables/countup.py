from countup_iterator import CountUp_Iterator
class CountUp:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return CountUp_Iterator(self)

counter=CountUp(1,10)

for i in counter:
    print(i)