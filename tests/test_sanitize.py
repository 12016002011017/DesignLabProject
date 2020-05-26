import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
sys.path.append('../')
from src import sanitize,ServerAPI

url = 'application.csv'
class TestSanitize(unittest.TestCase):
  
  def test_getapplication(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication(url)
    self.assertEqual(type(df),pd.DataFrame,"Invalid Type")
    
  def test_columns(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication(url)
    columns = list(df.columns)
    try:
      df_req = df[['reports', 'expenditure', 'active', 'income']]
    except e:
      print("Invalid! All necessary columns not found :")
      print(e)
      
  def test_uniqueapplicationID(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication(url)
    boolean = not df["Student"].is_unique 
    self.assertFalse(boolean, "Application ID not unique")
    
  def test_validAgeRange(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication(url)
    booleam = df["age"].between(20, 65, inclusive = True).all()
    self.assertTrue(boolean, "invalid age")
    
    
  
    
  
    


if __name__ == '__main__':
  unittest.main()
