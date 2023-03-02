def software(park_buliding):
    print("""Choose one Option from below
    1.Park the vehicle
    2.Get the vehicle
    3.Available Slots
    4.View all slots
    5.Exit
    """)
    def slotsavailable(prnt):
      cnt=0
      floor=0
      for x in park_buliding:
        floor_count=x.count("A")
        cnt+=floor_count
        floor+=1
        if print==True:
            print(f"floor :{floor} -- AvailableSlots :{floor_count}")
      return cnt
    def park():
      slots=slotsavailable(False)
      if slots>0:
        for indx,x in enumerate(park_buliding):
          if park_buliding[indx].count("A")>0:
              a_indx=park_buliding[indx].index("A")
              park_buliding[indx][a_indx]="O"
              print(f"floor{indx+1} -{x} ")
              prt="{}-{}".format(indx+1,a_indx+1)
              return prt
      else:
        return "slots are not available"
    def leave():
      parktkt=input("Enter your parking ticket")
      tkt=parktkt.split('-')
      floor,slot=int(tkt[0]),int(tkt[1])
      if 1<=floor<=len(park_buliding) and 1<=slot<=len(park_buliding[0]):
        if park_buliding[floor-1][slot-1]=="O":
          park_buliding[floor-1][slot-1]="A"
          return park_buliding[floor-1] 
        else:
          return "Wrong Parking Ticket"
      else:
        return "Enter valid Parking Ticket"
    def save():
      import csv
      with open('my_file.csv',mode='w') as file:
        writer=csv.writer(file)
        writer.writerow(["slot"+str(i+1) for i in range(len(park_buliding[0]))])
        for i in park_buliding:
          writer.writerow(i)  
    def view():
      import pandas as pd
      colum_name,index_labels=["slot"+str(i+1) for i in range(len(park_buliding[0]))],["floor"+str(i+1) for i in range(len(park_buliding))]
      data=pd.DataFrame(park_buliding,columns=colum_name,index=index_labels)
      print(data.head()) 
    option=int(input("You response: "))
    op_dict={1:'print(f"your token :: {park()}")&software(park_buliding)',2:'print(leave())&software(park_buliding)',3:'print("TotalSlots ::",slotsavailable(True))&software(park_buliding)',4:'view()&software(park_buliding)',5:'save()&print("ExitingFromTheSoftware")'}
    for i in op_dict[option].split('&'):
      eval(i)