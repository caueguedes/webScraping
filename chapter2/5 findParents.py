from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

print(bsObj.find('img', {'scr': '../img/gifts/img1.jpg'
                         }).parent.previous_sibling.get_text())

# 1. The image tag where src="../img/gifts/img1.jpg" is first selected
# 2. We select the parent of that tag (in this case, the <td> tag).
# 3. We select the previous_sibling of the <td> tag (in this case, the <td> tag that
# contains the dollar value of the product).
# 4. We select the text within that tag, “$15.00”