import requests


params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)

print(r.text)
## FORM BODIE
## <form action="http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi" id="example_form2" method="POST">
##    <input name="client_token" type="hidden" value="oreilly" />
##     <input name="subscribe" type="hidden" value="optin" />
##     <input name="success_url" type="hidden" value="http://oreilly.com/store/newsletter-thankyou.html" />
##     <input name="error_url" type="hidden" value="http://oreilly.com/store/newsletter-signup-error.html" />
##     <input name="topic_or_dod" type="hidden" value="1" />
##     <input name="source" type="hidden" value="orm-home-t1-dotd" />
##     <fieldset>
##         <input class="email_address long" maxlength="200" name="email_addr" size="25" type="text" value="Enter your email here" />
##         <button alt="Join" class="skinny" name="submit" onclick="return addClickTracking('orm','ebook','rightrail','dod');" value="submit">Join</button>
##     </fieldset>
## </form>


# import requests
#
#
# params = {'firsname': 'Ryan', 'lastname': 'Mitchell'}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
# print(r.text)
## FORM BODIE
## <form method="post" action="processing.php">
##     First name: <input type="text" name="firstname"><br>
##     Last name: <input type="text" name="lastname"><br>
##     <input type="submit" value="Submit">
## </form>