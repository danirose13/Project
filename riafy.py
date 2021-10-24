import re
def functions(str):
  valid = ("^(?=.*[a-z])(?=.*[A-Z](?=.*\\d)"+"(?=.*[-+_!@#$%^&*.,?])")
  g=re.compile(valid)
  if(str==null)
    print ("enter string")
    return
  if(re.search(g,str)):
    print ("True")
  else
    print ("False")
str= "W$fskdjfs@4429"
functions(str)
