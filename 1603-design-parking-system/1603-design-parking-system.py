class ParkingSystem:
    # 1-> big, 2-> medium, 3-> large
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.hashmap = {"big":self.big, "medium":self.medium, "small":self.small}
        self.mapping = {1:"big", 2:"medium", 3:"small"}

    def addCar(self, carType: int) -> bool:
        if self.mapping[carType] in self.hashmap and self.hashmap[self.mapping[carType]]!=0:
            if self.hashmap[self.mapping[carType]]==1:
                self.hashmap.pop(self.mapping[carType])
            else:
                self.hashmap[self.mapping[carType]] -=1
            return True
        else:
            return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)