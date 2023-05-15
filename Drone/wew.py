import smtplib
from email.mime.text import MIMEText

# Set up the SMTP server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()

# Log in to the server using an application-specific password
smtp_server.login('your_email@gmail.com', 'your_application-specific_password')

# Create a message
message = MIMEText('This is the body of the email.')
message['Subject'] = 'Test email'
message['From'] = 'your_email@gmail.com'
message['To'] = 'recipient_email@example.com'

# Send the message
smtp_server.sendmail('your_email@gmail.com', ['recipient_email@example.com'], message.as_string())

# Close the connection
smtp_server.quit()
