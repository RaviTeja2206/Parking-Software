import os
import csv
from operations import software

if os.path.exists("my_file.csv"):

  with open("my_file.csv",mode='r') as file:
    reader=csv.reader(file)
    cnt=0
    park_buliding=[]
    for row in reader:
      if cnt==0:
        cnt+=1
        continue
      else:
        park_buliding.append(row)
    software(park_buliding)
else:
  print("Running the Software First Time")
  floors=int(input("configure total floors available for parking "))
  per_floor_slots=int(input("configure parking slots per floor "))
  # A -> Available
  # O -> Occupied
  park_buliding=[["A" for i in range(per_floor_slots)] for j in range(floors)]
  
  print(f"floors={floors},per_floor_slots={per_floor_slots}")
  print()
  print("Configured the parking building")
  software(park_buliding)
  