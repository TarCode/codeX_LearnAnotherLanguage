import unittest
import readCSV

class TestSpazaFunctions(unittest.TestCase):
  def test_readFile(self):
    s = [['Sunday', '2015-02-01', 'Milk 1l', '3', '10.00'], ['Sunday', '2015-02-01', 'Imasi', '1', '25.00'], ['Sunday', '2015-02-01', 'Bread', '2', '12.00'], ['Sunday', '2015-02-01', 'Chakalaka Can', '3', '10.00'], ['Sunday', '2015-02-01', 'Gold Dish Vegetable Curry Can', '2', '9.00']]
    self.assertEquals(s, readCSV.readFile("saleTest.csv"))
     
if __name__ == '__main__':
    unittest.main()
