
import re

s = 'Taguwa_0_1'

result = re.search('[A-z]+', s).group()
print(result.group())