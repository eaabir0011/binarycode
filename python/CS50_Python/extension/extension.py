fle_name=input("File Name:")
fle_name=fle_name.lstrip().rstrip().lower()
if(fle_name.endswith(".gif") is True):
    print("image/gif")
elif(fle_name.endswith(".jpg") is True):
    print("image/jpeg")
elif(fle_name.endswith(".jpeg") is True):
    print("image/jpeg")
elif(fle_name.endswith(".png") is True):
    print("image/png")
elif(fle_name.endswith(".pdf")is True ):
    print("application/pdf")
elif(fle_name.endswith(".txt") is True):
    print("text/plain")
elif(fle_name.endswith(".zip") is True):
    print("application/zip")
else:
    print("application/octet-stream")