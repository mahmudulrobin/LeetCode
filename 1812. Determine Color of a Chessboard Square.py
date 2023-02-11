class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ["a","c","e","g"]
        y = ["b","d","f","h"]
        if coordinates[0] in x:
            if int(coordinates[1])%2!=0:
                return False
            else:
                return True
        else:
            if int(coordinates[1])%2!=0:
                return True
            else:
                return False