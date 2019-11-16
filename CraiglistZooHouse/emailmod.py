import smtplib
import pandas as pd
import numpy as np

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from time import gmtime, strftime
import datetime
# me == my email address
# you == recipient's email address
me = "PEPPER_AI_EMAIL@gmail.com"

def sendSingleEmailOnePage(recipients, df, source, ver, masterlist, totalcount):




    #for index, row in df.iterrows():
    msg = MIMEMultipart('alternative')
        #msg['Subject'] = "(RICHMOND) " + row['Price'] + ' - ' + row['Title']
    msg['Subject'] = "(Japan) " + "ZOO " + datetime.datetime.now().strftime("%B %d, %H:%M")
    msg['From'] = me
    msg['To'] = ", ".join(recipients)
    #msg['To'] = recipients
        # Create the body of the message (a plain-text and an HTML version).
    text = "Your new pillows in Japan Zoo!\n{0} - {1}\nLink:{2}"
    html = """\
	        <!DOCTYPE html>
            <html>
            <head>
            <style>
            #customers {
            font-family: Arial;
            border-collapse: collapse;
            width: 100%;
            }

            #customers td, #customers th {
            border: 1px solid #ddd;
            padding: 8px;
            }

            tr:nth-child(6n+5){background-color: #f2f2f2;}
            tr:nth-child(6n+6){background-color: #f2f2f2;}
            tr:nth-child(6n+7){background-color: #f2f2f2;}

            #customers th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #0057e7;
            color: white;
            }
            </style>
            </head>
            <body>
            <font face="Arial">
            <font size="3">
            <p>Your new Pillows in <b>Japan</b> Zoo:<br>

            <table id="customers">
            <tr>
            <th>Title</th>
            <th>Price</th>
            <th>Area</th>
            </tr>
            """
    table = ''
    oddeven = False;
    i = 0;
    for index, row in df.iterrows():
        i += 1
        if oddeven == True:
            table = table + "<tr style='background-color:#f2f2f2;'>" + """ <td colspan="3"><b>""" + "#" + str(i) + " - " +  row['Title'] + "</b></tr>" + \
            "<tr style='background-color:#f2f2f2;'>" + \
            "<td>" + row['Address'] + "</td>" + \
            "<td>" + row['Price'] + "</td>" + \
            "<td>" + row['Area'] + "</td>" + \
            "</tr>" + \
            "<tr style='background-color:#f2f2f2;'>" + \
            """<td colspan="3"><a href=""" +  row['Url'] + ">" + row['Url'] + "</a>" + \
            "</tr>"
            oddeven = False
        else:
            table = table + "<tr>" + """ <td colspan="3"><b>""" + "#" + str(i) + " - " +  row['Title'] + "</b></tr>" + \
            "<tr>" + \
            "<td>" + row['Address'] + "</td>" + \
            "<td>" + row['Price'] + "</td>" + \
            "<td>" + row['Area'] + "</td>" + \
            "</tr>" + \
            "<tr>" + \
            """<td colspan="3"><a href=""" +  row['Url'] + ">" + row['Url'] + "</a>" + \
            "</tr>"
            oddeven = True

           
           
        
        
    bottom = "</table><br>" + """
        Hoping we will find our perfect home!
                <br>
                <br>
                pepper <sub>{0}</sub><br>
                <br>
                <br>
                <hr>
                Log file:
                <br>
                <br>
                Source: <a href={1}>{1}</a><br>
                {2}<br>
                {3}
    </body>
    </html>
    """
    total = html + table + bottom.format(ver, source, masterlist.to_html(), totalcount)


# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text.format(row['Price'], row['Title'], row['Url']), 'plain')
    part2 = MIMEText(total, 'html')
    
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    # Send the message via local SMTP server.
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('PEPPER_EMAIL@gmail.com', 'PASSWORD')
        mail.sendmail(me, recipients, msg.as_string())
        
    except:
        return False
        print('Failure to send email')
    mail.quit()


    print('email sent')
    return True
    # Create message container - the correct MIME type is multipart/alternative.
        

def changeLastseenEmail(lastlastseen, currentlastseen):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'CHANGE OF Lastseen Variable [Debug]'
    msg['From'] = me
    msg['To'] = 'admin@gmail.com'

# Create the body of the message (a plain-text and an HTML version).
    text = "Last Seen Variable: {0}\nChange To: {1}"
    html = """\
		<html>
        <head></head>
        <body>
        <font face="Arial">
        <font size="3">
            <p>Last Seen Variable: {0}<br>
            <br>
            Change To: {1}
            <br>
            pepper
            <br>
        </p>
        </body>
        </html>
        """

# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text.format(lastlastseen, currentlastseen), 'plain')
    part2 = MIMEText(html.format(lastlastseen, currentlastseen), 'html')
    # Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    # Send the message via local SMTP server.
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('PEPPER_GMAIL@gmail.com', 'PEPPER PASSWORD')
        mail.sendmail(me, 'admin@gmail.com', msg.as_string())
    except:
        return False

    mail.quit()
    print('email sent Change of last SEEN [DEBUG]')
    # Create message container - the correct MIME type is multipart/alternative.