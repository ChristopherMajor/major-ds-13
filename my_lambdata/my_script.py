
import pandas

from my_lambdata.my_mod import enlarge


print('Hello world uWu')

df = pandas.DataFrame({"state": ['CT', 'CO', 'CA', 'TX']})
print(df.head())

print(enlarge(9))
