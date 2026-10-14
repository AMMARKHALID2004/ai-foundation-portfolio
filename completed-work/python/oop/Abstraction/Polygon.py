from abc import abstractmethod, ABC
class Polygon(ABC):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    @abstractmethod
    def calculate_area(self):
        pass


