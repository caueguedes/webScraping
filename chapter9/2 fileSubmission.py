import requests

files = {'uploadFIle': open('../files/Python-logo.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/processing2.php', files=files)
print(r.text)

## FORM BODIE
## <form action="processing2.php" method="post" enctype="multipart/form-data">
##     Submit a jpg, png, or gif: <input type="file" name="image"><br>
##     <input type="submit" value="Upload File">
## </form>