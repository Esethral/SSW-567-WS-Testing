#I pledge my honor that I have abided by the Stevens Honor System
#Evan Abel

import unittest

def classifyTriangle(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)

    if ((a*a)+(b*b) == c*c):
        return "Right"

    elif (a == b and b == c):
        return "Equilateral"

    elif (a == b and b != c):
        return "Isoceles"

    elif (a == c and c != b):
        return "Isoceles"

    elif (c == b and b != a):
        return "Isoceles"

    elif (a != b and a != c and b != c):
        return "Scalene"

    else:
        return "Failed"

def runClassifyTriangle():
    a = input("Enter length of side a: ")
    b = input("Enter length of side b: ")
    c = input("Enter length of side c: ")
    print(classifyTriangle(a,b,c))

class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral Triangle')
        self.assertEqual(classifyTriangle(4,4,9),'Isoceles','4,4,9 is an Isoceles triangle')
        self.assertEqual(classifyTriangle(1,3,5),'Scalene','1,3,5 is a Scalene triangle')
        
    def testMyTestSet2(self): 
        self.assertNotEqual(classifyTriangle(3,4,5),'Scalene','3,4,5 is a Right triangle but should also be a Scalene triangle')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    runClassifyTriangle()
    unittest.main(exit=False)