import numpy as np
class Complex:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def display(self):
    if self.b>=0:
      print('{}+{}i'.format(self.a,self.b))
    if self.b<0:
      print('{}{}i'.format(self.a,self.b))

  def add(self,obj):
    return Complex(self.a+obj.a,self.b+obj.b)
  
  def subtract(self,obj):
    return Complex(self.a-obj.a,self.b-obj.b)
  def modulus(self):
    return math.sqrt(self.a*self.a+self.b*self.b)
  def conjugate(self):
    return Complex(self.a,-self.b)
  def inverse(self):
    return Complex(self.a/(self.a*self.a+self.b*self.b),-self.b/(self.a*self.a+self.b*self.b))
  def multiplication(self,obj):
    return Complex(self.a*obj.a -self.b*obj.b,self.a*obj.b+self.b*obj.a)

 