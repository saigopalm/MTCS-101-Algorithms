'''
100 Prisoners' problem:
The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. 
A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. 
The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. 
The drawers are closed again afterwards. If, during this search, every prisoner finds their number in one of the drawers,
all prisoners are pardoned. If even one prisoner does not find their number, all prisoners die. 
Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the 
first prisoner enters to look in the drawers. What is the prisoners' best strategy?

Author: Mantha Sai Gopal
Reg.no: 23358
'''
import random

boxes = list(range(1,101))
random.shuffle(boxes)
count = 0

for prisoner in range(1,101):
    current_box = prisoner

    for _ in range(50):
        if boxes[current_box - 1] == prisoner:
            count +=1
            break
        else:
            current_box = boxes[current_box - 1]

if count == 100:
    print("1")
else:
    print("0")
