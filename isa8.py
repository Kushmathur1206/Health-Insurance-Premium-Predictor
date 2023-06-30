import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

window=Tk()
window.title('HEALTH INSURANCE PREMIUM PREDICTOR')
label_Heading=Label(window,text='HEALTH INSURANCE \n PREMIUM PREDICTOR')
label_Heading.config(font=('Helvetica bold',40))
label_Heading.grid(row=0,column=1)
#bg = PhotoImage( file = "Screenshot (1).png")
'''label1 = Label( window, image = bg)

label1.place(x = 0,y = 0)
label1.geometry("400x400")

bg = PhotoImage(file = "Your_img.png")
  

background_image = ImageTk.PhotoImage(Image.)
l=tk.Label(image=background_image)
l.grid()'''


#Enter Name 
label_Name=Label(window,text='Your Name').grid(row=1,column=0)
Name = Entry(window,width=50)
Name.grid(row=1,column=1)

#Enter Age
label_Age=Label(window,text="Enter Age").grid(row=3,column=0)
Age = Entry(window,width=50)
Age.grid(row=3,column=1)

#Enter Sex
'''S = StringVar()

Sex = Entry(window,textvariable=S,width=50)
Sex.grid(row=2,column=1)'''

label_Sex=Label(window,text='Enter Sex').grid(row=2,column=0)
clicked1=StringVar()
clicked1.set("Male")
drop =OptionMenu(window,clicked1,"Male","Female","Others")
drop.grid(row=2,column=1)


#Enter BMI
label_BMI=Label(window,text="Enter your BMI").grid(row=4,column=0)
BMI = Entry(window,width=50)
BMI.grid(row=4,column=1)

#Enter your number of children
label_NC=Label(window,text='Number of children you have').grid(row=5,column=0)
NC = Entry(window,width=50)
NC.grid(row=5,column=1)

#Enter If you're a smoker or not
label_Email_id=Label(window,text='Are you a smoker').grid(row=6,column=0)
clicked2=StringVar()
clicked2.set("Yes")
drop = OptionMenu(window,clicked2,"Yes","No")
drop.grid(row=6,column=1)


#Enter Region
label_Email_id=Label(window,text='Select your region').grid(row=7,column=0)
clicked3=StringVar()
clicked3.set("South East")
drop =OptionMenu(window,clicked3,"South East","South West","North East","North West")
drop.grid(row=7,column=1)

label_Email_id=Label(window,text='Your Email Address').grid(row=8,column=0)
Email = Entry(window,width=50)
Email.grid(row=8,column=1)

label_Email_id=Label(window,text=' ').grid(row=9,column=0)

a= Name.get()

def Submit():
    """Data Collection & Analysis"""

    # loading the data from csv file to a Pandas DataFrame
    insurance_dataset = pd.read_csv('insurance.csv')

    # first 5 rows of the dataframe
    insurance_dataset.head()

    # number of rows and columns
    insurance_dataset.shape

    # getting some informations about the dataset
    insurance_dataset.info()

    # checking for missing values
    insurance_dataset.isnull().sum()

    """Data Analysis"""

    # statistical Measures of the dataset
    insurance_dataset.describe()

    # distribution of age value
    sns.set()
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['age'])
    plt.title('Age Distribution')
    #plt.show()

    # Gender column
    plt.figure(figsize=(6,6))
    sns.countplot(x='sex', data=insurance_dataset)
    plt.title('Sex Distribution')
    #plt.show()

    insurance_dataset['sex'].value_counts()

    # bmi distribution
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['bmi'])
    plt.title('BMI Distribution')
    #plt.show()

    """Normal BMI Range --> 18.5 to 24.9"""

    # children column
    plt.figure(figsize=(6,6))
    sns.countplot(x='children', data=insurance_dataset)
    plt.title('Children')
    #plt.show()

    insurance_dataset['children'].value_counts()

    # smoker column
    plt.figure(figsize=(6,6))
    sns.countplot(x='smoker', data=insurance_dataset)
    plt.title('smoker')
    #plt.show()

    insurance_dataset['smoker'].value_counts()

    # region_column
    plt.figure(figsize=(6,6))
    sns.countplot(x='region', data=insurance_dataset)
    plt.title('region')
    #plt.show()

    insurance_dataset['region'].value_counts()

    # distribution of charges value
    plt.figure(figsize=(6,6))
    sns.distplot(insurance_dataset['charges'])
    plt.title('Charges Distribution')
    #plt.show()

    """Data Pre-Processing

    Encoding the categorical features
    """

    # encoding sex column
    insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

    3 # encoding 'smoker' column
    insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

    # encoding 'region' column
    insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

    """Splitting the Features and Target"""

    X = insurance_dataset.drop(columns='charges', axis=1)
    Y = insurance_dataset['charges']

    print(X)

    print(Y)

    """Splitting the data into Training data & Testing Data"""

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    print(X.shape, X_train.shape, X_test.shape)

    """Model Training

    Linear Regression
    """

    # loading the Linear Regression model
    regressor = LinearRegression()

    regressor.fit(X_train, Y_train)

    """Model Evaluation"""

    # prediction on training data
    training_data_prediction = regressor.predict(X_train)

    # R squared value
    r2_train = metrics.r2_score(Y_train, training_data_prediction)
    print('R squared vale : ', r2_train)

    # prediction on test data
    test_data_prediction =regressor.predict(X_test)

    # R squared value
    r2_test = metrics.r2_score(Y_test, test_data_prediction)
    print('R squared vale : ', r2_test)

    """Building a Predictive System"""
    if (clicked1.get()=='Male'):
        sex=0
    else:
        sex=1
    
    if (clicked2.get()=='Yes'):
        smoker=0
    else:
        smoker=1
    
    if (clicked3.get()=='South East'):
        region=0
    elif(clicked3.get()=='South West'):
        region=1
    elif(clicked3.get()=='North East'):
        region=2
    elif(clicked3.get()=='North West'):
        region=3
    input_data = (int(Age.get()),sex,float(BMI.get()),int(NC.get()),smoker,region)

    # changing input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = regressor.predict(input_data_reshaped)
    print(prediction)

    print('The insurance cost is USD ', round(prediction[0],0))
    print(sex)
    print(clicked1.get())
    print(smoker)
    print(region)
    
    Submit_label=Label(window,text='Thank you '+ Name.get() +'The insurance cost is USD '+ str(round(prediction[0],0)))
    Submit_label.grid(row=9,column=1)
    
    def send_mail():

        body = 'Hello {},\n\nYour info:-\n     Age: {}\n     BMI: {}\n     Sex: {}\n     No of children: {}\n     Are you a smoker: {}\n     Region: {}\n\nAs per the details provided above by you, the approximate insurance amount will be around $ {}.'.format(Name.get(),Age.get(),BMI.get(),clicked1.get(),NC.get(),clicked2.get(),clicked3.get(),round(prediction[0],0))

        sender = "kushwork1206@gmail.com"

        password = 'aquuteqiuqbjtdca'
        # put the email of the receiver here
        receiver = Email.get()

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = "kushwork1206@gmail.com"
        message['To'] = Email.get()
        message['Subject'] = 'Quote for insurance policy'

        message.attach(MIMEText(body, 'plain'))

        pdfname = 'HACKATHON PROJECT.pdf'

        # open the file in bynary
        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        #enable security
        session.starttls()

        #login with mail_id and password
        session.login(sender, password)
        

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')    
    send_mail()

button= Button(window,text='Submit',padx=40,command=Submit)
button.grid(row=10,column=1)

window.mainloop()