def fibo(n):
   if n < 2:
      return n
   else:
      return fibo(n-1) + fibo(n-2)
      
def test_ac05_01():
    assert fibo(3) == 2     
def test_ac05_02():
    assert fibo(3) == 100  
    
def test_ac05_03():
    assert fibo(3) == 20000  