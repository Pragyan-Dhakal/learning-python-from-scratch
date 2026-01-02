#Write a class train which has methods to book a ticket, get status (no. of seats) and
# get fare information of train running under indian railway.

import random

class train:
    def __init__(self, trainNo):
        self.trainNo=trainNo
    
    def book (self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")
    
    def getstatus (self):
        print(f"Train no {self.trainNo} is runnnig on time.")
    
    def fare (self, fro, to):
        print(f"Ticket fare in train no {self.trainNo} is {random.randint(250, 1050)}")

t =train(12345)
t.book ("Nepal", "India")
t.getstatus()
t.fare("Nepal","India")

    