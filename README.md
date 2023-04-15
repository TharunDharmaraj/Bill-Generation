# Whatsapp Bill Generation Bot

<h3> EXAMPLE:
          
1. TYPE IN THE SPECIFIED FORMAT:
          
![EXAMPLE](https://user-images.githubusercontent.com/83175935/232184999-e901a54e-3e45-46c8-914b-f3d9b12676b9.jpeg)



          
2. OBTAINED BILL: 
          
![EXAMPLE_BILL](https://user-images.githubusercontent.com/83175935/232185004-cebbdb22-ea1a-49a4-8063-a1e8df0d4465.jpeg)


          

# STEPS FOR SETUP

          
1. Get Your Twilio Tokens and Paste in the fields of both flask_app.py & main.py

```
          account_sid = 'YOUR_TWILLIO_ID'
          auth_token = 'TWILLIO_ACCESS_TOKEN'
```

          
2. Get Your Imgur Tokens and Paste in the fields of imgur.py

```
          client_id = "IMGUR_ID"
          client_secret = "IMGUR_SECRET"
          refresh_token = os.environ.get("IMGUR_REFRESH_TOKEN") -> Setup the Refresh Token Obtained in your local environment
```
  
         
          
3. Set the phone number to be used in the field and FROM field is obtained from your TWILIO accout

```
          to='whatsapp:WHATSAPP_NUMBER_TO_BE_USED'
```


          
4. Install the packages in requirements.txt by

```
          pip install requirements.txt
```

          
          
5. Run main.py


          
6. In Whatsapp, Go to the Twilio number and type 

```
          2022, Toyota, Model Name 127XB, 29000, 12 Nov 2022   
          # YEAR, COMPANY , MAKE , PRICE , DATE    is the format separated by commas
```


# Note : 
Deployed in Local and not in the cloud, for cloud deplymnet, use [pythonanywhere](https://www.pythonanywhere.com/) with some modifications in the cloud (Further Updates)

