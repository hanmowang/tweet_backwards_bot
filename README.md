# Tweet Backwards Bot

Steps to use this bot
1. Select a target twitter user and enter their twitter handle (their @) into the config file
2. In the credentials file, you need to enter your twitter api and access token. Find this by going onto https://developer.twitter.com/en/portal/dashboard
also make sure you gave the bot <b>read and write</b> permissions
![image](https://user-images.githubusercontent.com/89413517/177448098-2d2304ca-bfd9-44f9-8b43-28afb3a48b98.png)
3. After step 1 and 2 are done, in command prompt, navigate to the file location and enter "docker build -t tweet-backwards-bot ."
![Screenshot 2022-09-10 191702](https://user-images.githubusercontent.com/89413517/189505122-4ba5cbd4-719c-4433-a8f8-6805e50eaf9c.png)
4. After you have built the docker image, type "docker run tweet-backwards-bot" and your program should start running!
![Screenshot 2022-09-10 192903](https://user-images.githubusercontent.com/89413517/189505134-9f64a5d3-2b5f-4b44-aff2-322deb547b17.png)
5. Your twitter account will look like the target's but completely backwards! 
This bot will also automatically reply under the target's most recent original tweet with the content
backwards, even including the pictures!

Here is a quick example of what your account will look like

# Target
![Screenshot 2022-07-05 205330](https://user-images.githubusercontent.com/89413517/177441001-98dcbe02-ab10-4a05-bd70-f26abf8e707f.png)
![Screenshot 2022-07-05 205401](https://user-images.githubusercontent.com/89413517/177441007-cff0b17f-6911-48a7-b0f2-898237ba03eb.png)
# Your profile
![Screenshot 2022-07-05 211111](https://user-images.githubusercontent.com/89413517/177442566-e6ac18b7-c460-420b-8ec3-5dc89dd266eb.png)
![Screenshot 2022-07-05 210119](https://user-images.githubusercontent.com/89413517/177441013-27da7b38-93d9-46fe-bd0f-4ebcc9b6a8af.png)
![Screenshot 2022-07-05 210104](https://user-images.githubusercontent.com/89413517/177441015-e733f181-311a-4d70-be1b-72e7ca7a09e3.png)



