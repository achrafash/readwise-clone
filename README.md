# readwise-clone

The purpose of this project is to retrieve one's higlights from kindle (read.amazon) and send an email composed of these highlights

I'm using python, with the selenium library to search within chrome browser automatically. I then use the SMP library to send the email.

It works fine, but the goal is to check the highlights and send an email regularly.
To do so I should either run the python script and the program emails in advance, or somehow run the current script regularly somehow from a remote server so that it can send an email without having me doing anything. (I think readwise is using a chrome extension to do that)
