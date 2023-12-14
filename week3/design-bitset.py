class Bitset:
    def __init__(self, size: int):
        self.bitset = [0] * size
        self.size = size
        self.ones = 0
        self.is_flipped = False
        
		
    def fix(self, idx: int) -> None:
        if self.is_flipped and self.bitset[idx]:
            self.bitset[idx] = 0
            self.ones += 1
			
        elif not self.is_flipped and not self.bitset[idx]:
            self.bitset[idx] = 1
            self.ones += 1
        
		
    def unfix(self, idx: int) -> None:
        if self.is_flipped and not self.bitset[idx]:
            self.bitset[idx] = 1
            self.ones -= 1
			
        elif not self.is_flipped and self.bitset[idx]:
            self.bitset[idx] = 0
            self.ones -= 1
        
		
    def flip(self) -> None:
        self.is_flipped = not self.is_flipped
        self.ones = self.size - self.ones


    def all(self) -> bool:
        return self.ones == self.size
        

    def one(self) -> bool:
        return self.ones > 0
        
		
    def count(self) -> int:
        return self.ones
        
		
    def toString(self) -> str:
        if self.is_flipped:
            return "".join("0" if i else "1" for i in self.bitset)
        
        return "".join("1" if i else "0" for i in self.bitset)