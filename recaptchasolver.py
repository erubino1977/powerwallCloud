import requests
from time import sleep
import base64

# You will need pip install svglib

# It goes to say this work takes effort so please use my referral to support my work
# https://2captcha.com?from=11874928 
# The link above allows you to create a acount with 2captcha which is what we use
# If you know me we can share API key, just reach out to me  thanks
# Appreciate donations to keep 2captcha going, anything helps
API_KEY = 'ac34930cbcce1a11a86dac1a68dafb63'
CAPTCHA_ENABLE = True

def main(sitekey, pageurl):

    if(CAPTCHA_ENABLE): 
        # Captcha is session based so use the same headers
        print 'Getting captcha'
        #catpcha = session.get('https://auth.tesla.com/captcha', headers=headers)


        # Now use the image file saved locally to post to captcha service and wait for response
        # here we post site key to 2captcha to get captcha ID (and we parse it here too)
        current_url = "http://2captcha.com/in.php"

        data = {
            "key": API_KEY,
            "method": "userrecaptcha",
            "googlekey": sitekey,
            "pageurl": pageurl      
        }
           
        resp = requests.post(current_url,
                    data=data)

        captcha_id = resp.text.split('|')[1]

        # Change data to be getting the answer from 2captcha
        data = {
            "key": API_KEY,
            "action": "get",
            "id": captcha_id
        }
        answer_url = "http://2captcha.com/res.php"
        resp = requests.get(answer_url,
                    params=data)

        captcha_answer = resp.text
        while 'CAPCHA_NOT_READY' in captcha_answer:
            sleep(15)
            captcha_answer = requests.get(answer_url,
                    params=data)
            print captcha_answer.text

        captcha_answer = captcha_answer.text.split('|')[1]
        print captcha_answer
        return captcha_answer
    # if captcha not enabled just return empty string
    else:
        print "Skipping captcha"
        return ""


if __name__ == "__main__":
    main()
