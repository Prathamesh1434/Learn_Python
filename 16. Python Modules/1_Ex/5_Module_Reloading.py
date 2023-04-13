# Module Reloading
from imp import reload
import module1 # It will get loaded once in PVM. 
import time

module1.add(10,30)
time.sleep(10)

print('Wake up ... Trying to use module again ...')
import module1 # Loaded copy will get considered.
# Therefore only old copy will be avaliable.
module1.product(2,3) # AttributeError: module 'module1' has no attribute 'product'

time.sleep(30)

reload(module1)
module1.sub(5,4)