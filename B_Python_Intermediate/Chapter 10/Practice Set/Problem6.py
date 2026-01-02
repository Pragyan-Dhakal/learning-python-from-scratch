#Can you change the self-parameter inside a class to something else (say "harry").Try changing self to "slf" or "harry" and see the effects.
#No changing self to anything else won't effect anything unless all the self are changed to same name


import random

class train:
    def __init__(sel, trainNo):
        sel.trainNo=trainNo
    
    def book (sel, fro, to):
        print(f"Ticket is booked in train no {sel.trainNo} from {fro} to {to}")
    
    def getstatus (sel):
        print(f"Train no {sel.trainNo} is runnnig on time.")
    
    def fare (sel, fro, to):
        print(f"Ticket fare in train no {sel.trainNo} is {random.randint(250, 1050)}")

t =train(12345)
t.book ("Nepal", "India")
t.getstatus()