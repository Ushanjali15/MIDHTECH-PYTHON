READ=1
WRITE=2
EXECUTE=4 
user_permission=READ | WRITE
print("can read:",user_permission & READ == READ)
print("can write:",user_permission & WRITE == WRITE)
print("can execute:",user_permission & EXECUTE == EXECUTE)
