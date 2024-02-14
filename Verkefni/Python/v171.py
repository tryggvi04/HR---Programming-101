class WaterBottle:
    def __init__(self, max_capacity=2) -> None:
        self.max_capacity = max_capacity
        self.current_contents = 0

    def fill(self) -> None:
        self.current_contents = self.max_capacity
         

    def drink(self, amount: float) -> float:
        if amount >= self.current_contents:
            extracted_amount = self.current_contents
            self.current_contents = 0
        elif amount > 0:
            self.current_contents -= amount
            extracted_amount = amount
        elif amount <= 0:
            extracted_amount = 0
        return extracted_amount 

    def __str__(self) -> str:
        return "The bottle currently holds {:.1f}L of water.".format(self.current_contents)