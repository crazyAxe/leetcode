from urllib import request
import re
res = re.search(r'[0-9]+', '63579')
nums = res.group()
while res:
    nums = res.group()
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nums
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    print('Data:', data)
    res = re.search(r'[0-9]+', data)
