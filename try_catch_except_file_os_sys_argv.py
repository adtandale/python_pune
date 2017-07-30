import sys
import os

a=len(sys.argv)

try:
  if a==1:
    raise Exception()

except Exception as e:
   print("Insuffitient argument 12345")
   sys.exit(1)


try:
  if len(sys.argv)>1:
     raise Exception()

except Exception:
   file_name=sys.argv[1]
   option=sys.argv[2]
   message=sys.argv[3]
   try:
     if not os.path.isfile(file_name):
       raise Exception()
     else:
       raise Exception()
       
   except Exception:
     f=open(file_name,'w') 
     if option=='a':
       f.write(message)
       f.close()
     elif option=='p':
       print("message is := ",message)  


# -a for add
# -d delete the task
# -l for display
# -u update a task
# -t time track
# -h help
# -v version
# -tag to the task like [office, Home, Sport]
# http://etherpad.openstack.org/p/python_todo
