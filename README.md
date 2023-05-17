# Discord reply using AI with your Discord ID

This is a programme to use AI in Discord through bringing API of that AI and bridge it with your Discord ID.


## Discord Authorization
First and foremost you will need you Discord Authorization code for the task. To get Discord Authorization Key you will just need to do some simple tasks. You will need a Windows or Linux to complete that. This [Link](https://www.youtube.com/watch?v=9XJt6EbZWPU) link has guide how to Get your Authorization token. Please dont share it with anyone because with the code anyone can access your account. Make sure to Copy the Header token for each channel. Header url is different for different channel

NB : If you logout or your sessions of discord gets timeout then please check the Authorization token again because it can change. And if it changes the code will not run properly
## OpenAI API 
If you want to give AI generated message you have to Bring the API from OpenAI. To bring it you have to create an account in OpenAI and create an API. Here is the link [Link](https://platform.openai.com/) . From here you first sign up then follow as the video [Link](https://www.youtube.com/watch?v=EIYapGbNRwk) shows. 

NB : 

    1. It has no expiration date
    2. It is charged $0.02 for 1,000 tokens (1 token is roughly 1  word) and we get $20 free credit
    3. Maximum limit of token is around 4,000

    4. No there is no limit of how many times you call

So create new Keys and paste it in the designated place. Remember to not share the keys with anyone else.

## Discord User ID
To get your Discord ID you have to enable Developer Mode First. First go to settinngs then Advance. There you will find your developer Mode. Turn it on. Then go to settings There you will see 3 dot beside your proile name. Click there copy ID. Done.

You can get help from here: [Link](https://www.youtube.com/watch?v=mpbHY71NA7g)
## Final
    1. Copy and paste your discord authorization key in 'Give_your_discord_authorization_key' key word that you will find in line 9
    2. Copy and paste your API key in 'replace with openAI Api' key word that you will find in line 6
    3. Copy and paste your url in 'Give discord header channel link' key word that you will find in line 26 and 30
    4. Copy and paste your Discord user ID in 'Give discord user ID(not name)' key word that you will find in line 51
    5. Make sure to keep it inside ''. example 'Discord headed'. Like this


Run the Code and have fun.
Happy Programming
