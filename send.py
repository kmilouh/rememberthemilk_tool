#!/usr/bin/env python

import sys
import smtplib
import subprocess

# Use 
# you must have installed gnome-keyring libsecret-tools
#
# $:-  sudo apt install gnome-keyring libsecret-tools 
#
# Then store your email password using secret-store like this:
#
# $:-  secret-tool store --label='milki gmail password' pass1 value1
#
# Then replace your email, your remember the milk email, and the key-values used to store your password.
#
#
#
# Create in your ~/.bash_aliases this function
#
# todo(){
#  todo_python_file=/your/send.py_file_path
#  python3 $todo_python "$1" "$2"
# 
# }
#
#
  
arguments_len = len(sys.argv)

if arguments_len == 1 :
    print('You must set al least 1 argument \n')
    print("python3 send.py 'Make the grocerys list' ")
    print('You must set the TODO argument and as optional the description ')
    exit()

email = 'Youremail@gmail.com'
milk_user = 'YourMilkId@rmilk.com'
store_password_query = 'pass1 value1'

todo = sys.argv[1]
if len(todo)==0 :
    print("You must set the TODO argument")
    exit()

todo_description = sys.argv[2] if arguments_len==3 else ''

command = "secret-tool lookup %s" % store_password_query  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#Launch the shell command:
password = process.communicate()[0].decode("utf-8") 


class Gmail(object):
    def __init__(self, email, password,re_milk_user):
        self.email = email
        self.password = password
        self.re_milk_user = re_milk_user
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.re_milk_user,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.re_milk_user,
            headers + "\r\n\r\n" + body)

gm = Gmail(email, password, milk_user)

gm.send_message(todo, todo_description)


