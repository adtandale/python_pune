def print_msg(msg, error="No Error", **kwargs):
    print("Log:"+error+"\t" +msg+ str(kwargs))
    print(kwargs)
          

print_msg("this will tak e as parameter and print","file not found",key="1,2,3,4,5")
