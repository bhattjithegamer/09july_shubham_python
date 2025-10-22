f = open("demo.txt", "w")   # "w" → write mode (new file banse / old overwrite thase)
f.write("Hello Bhatt ji!\nKem cho?")
f.close()
print("File created and written successfully.")

import os 

os.remove("bhattji.txt") #remove file delete thase
