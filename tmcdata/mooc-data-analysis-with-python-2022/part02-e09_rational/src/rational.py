#!/usr/bin/env python3

class Rational(object):
    def __init__(self, x, y)->None:
        self.x = x 
        self.y = y

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def __mul__(self, r):
        return Rational(self.x * r.x , self.y * r.y)
        

    def __truediv__(self, r):
        # multiply other side by recipicol of other fraction
        return Rational(self.x * r.y, self.y * r.x)

    def __add__(self, r):
        # just like fraction multiplication, must have common denominator
        return Rational(self.x * r.y + r.x * self.y, self.y * r.y)
       
    
    def __sub__(self, r):

        # just like fraction multiplication, must have common denominator
        return Rational(self.x * r.y - r.x * self.y, self.y * r.y)
    
    def __eq__(self, r):
        return (self.x, self.y) == (r.x, r.y)
    
    def __gt__(self, r):
        return (self.x, self.y) > (r.x, r.y)

    def __lt__(self, r):
        return (self.x, self.y) < (r.x, r.y)
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
