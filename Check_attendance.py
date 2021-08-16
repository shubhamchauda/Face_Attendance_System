import pandas as pd
import smtplib
from email.message import EmailMessage
import smtplib
from datetime import datetime

def absentStudents():
    attendance_data = pd.read_csv('Attendance.csv')
    students_data =  pd.read_csv('Class_Student_Data.csv')
    absent_students_list = students_data[~students_data['Roll_no'].isin(attendance_data.Roll_no.values)].reset_index()
    return absent_students_list
def sendMail(absent_students_list):
    # creates SMTP session  
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    send_from = ""
    password = ''
    SUBJECT = 'Attendance Info'
    s.login(send_from, password)
    with open('textfile.txt','r') as f:
        TEXT = f.read()  
        current_date = datetime.now()
        current_date = str(current_date.strftime("%d,%m,%y")).replace(',','-')
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S') 
        print(TEXT + ' '+current_date+" Time:"+dtString)
             
    # message to be sent
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT + ' '+dtString)    
    for mail_id in absent_students_list.Email.values:
         
        # sending the mail
        s.sendmail(send_from, mail_id, message)
        # terminating the session
        s.quit()
if __name__ == '__main__':
  absent_students = absentStudents()
  sendMail(absent_students_list= absent_students)
