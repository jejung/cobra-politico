# cobra-politico
Scrapy spider to search for undecided brazilian politicians emails at http://mapa.vemprarua.net/

The Brazil's actual moment is very important for all of us. The country is in regression by a very long time and the population wants the president impeachment. The site http://mapa.vemprarua.net/ is maintained by a popular group called #VemPraRua (Come to the street) that is organizing manifestations in all brazilian states. 
The page indentifies all the politicians who will vote in the impeachment process, and shows if it is publically in favor, is undecided or is against it. For each politician the site lists some information about the life, the patrimony and the contacts, so the population can ask for results.
I developed this scrapy spider to help me send emails for all the politicians who are listed as undecided in the site. I decided to share this tool for everyone who wants to send a message.

The usage is very simple, first you need to have Python 2.7 installed and then install [Scrapy](http://scrapy.org/).
With scrapy installed you can clone this repository:

    git clone https://github.com/jejung/cobra-politico.git

Jump in to the created directory cobra-politico:

    cd cobra-politico

And download the emails list with:

    scrapy crawl states

This will create a file emails.txt, which have a list with name=email. 
There is a python script prepared to send a message for all this emails. The message must reside in the text.txt file. The header of the email will contain the message "Senhor(a) <Deputado|Senador> <Nome>,". After writing and saving the message, you can send it with:

    python send.py

The script will ask for your Gmail account and password, note that the password will appear on the screen as you type. If you prefer you can alter the script and put your account and password fixed in the file. Feel free to alter the email headers too.
And now you have sent a lot of messages to all the undecided politicians, congratulations and thank you for helping us in this so important moment.
