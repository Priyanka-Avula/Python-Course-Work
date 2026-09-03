import logic
logic.add(10,5)
logic.sub(10,5)
logic.mul(10,5)
logic.div(10,5)
logic.mod(10,5)
logic.pow(10,5)

#We can create alias name for a module
import logic as lg
lg.add(10,5)
lg.sub(10,5)
lg.mul(10,5)
lg.div(10,5)
lg.mod(10,5)
lg.pow(10,5) 

#We can import only few methods out of all the methods 
#Using from and import 
from logic import add,sub
add(10,20)
sub(20,30)

#If we want to import all the methods
from logic import *
add(10,5)
sub(10,5)
mul(10,5)
div(10,5)
mod(10,5) 
pow(10,5)