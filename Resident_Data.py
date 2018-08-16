# Welcome to resident data program, the program has the capacity to store the resident data of up to 999 people in a locality
# The limit can be increased to any limit according to the need of the user.
from __future__ import print_function
# The datetime library is used to get the current date from the computer
import time
from datetime import datetime

now = datetime.now()
ty = now.year
tm = now.month
td = now.day

start = "\t\t\t\t\tWELCOME"
for i in start:
    print (i, end=" ")
    time.sleep(0.1)
dot = "................."
print("\n\t\t\t\t       ", end="")
for i in dot:
    print(i, end="")
    time.sleep(.03)
print("\n")
st = "\n\t\t\t\tThis is a RESIDENT DATA software.\n\t\t\tUsing this you can store up to 999 resident data.\n"
for i in st:
    print (i, end="")
    time.sleep(.08)
star = "************************************************************************************************************************"
for i in star:
    print(i, end="")
    time.sleep(0.01)
# This is where the user is allowed to chose the phase
ch = 'y'
while ch == 'y':
    answer = input("\nAre You Creating A New Resident Data [Press 1]\nOr Are You Searching For A Resident Data [Press 2]")
    if answer == 1:
        # The input is taken here
        # Everything except id and address are asked to input individually for each member
        temp1 = open("resident_data", "a")

        temp1 = open("resident_data", "r")
        id = raw_input("Enter the ID number : ")

        address = raw_input("Enter the resident name : ")

        m = input("How many members?")
        for z in range(1, m + 1):
            print("Member ", z)
            name = raw_input("Enter the person's name : ")
            dob = raw_input("Enter the person's date of birth (dd/mm/yyyy):")
            p = 0
            while p == 0:
                if dob.count("/") != 2:
                    dob = raw_input("Enter in (dd/mm/yyyy) format:")
                else:
                    l = dob.split("/")
                    if len(l[0]) > 2 or len(l[0]) == 0 or len(l[1]) == 0 or len(l[1]) > 2 or len(l[2]) != 4:
                        dob = raw_input("Enter in (dd/mm/yyyy) format:")
                    else:
                        p += 1

            blood_group = raw_input("Enter the person's blood group :")
            d = raw_input("Person with any disabilities?(y/n)")
            if d == "y" or d == "yes":
                disb = raw_input("Enter the disability:")
            else:
                disb = "No"
            phone = raw_input("Enter the person's phone number? ")
            email = raw_input("Enter the person's email address? ")
            y = 0
            while y == 0:
                if email.find("@") == -1:
                    email = raw_input("Enter a valid email ID")
                else:
                    y += 1

            status = raw_input("Enter your Status(Mention your job or course)")
            temp1 = open("resident_data", "a")
            # This is used to set the alloted space for the id depending on the its digit count
            if len(id) == 1:
                temp1.write(id + "$$" + address + "^" + name + "^" + dob + "^" + blood_group + "^" + disb + "^" + phone + "^" + status + "^" + email + "^")
            elif len(id) == 2:
                temp1.write(id + "$" + address + "^" + name + "^" + dob + "^" + blood_group + "^" + disb + "^" + phone + "^" + status + "^" + email + "^")
            elif len(id) == 3:
                temp1.write(id + address + "^" + name + "^" + dob + "^" + blood_group + "^" + disb + "^" + phone + "^" + status + "^" + email + "^")
            temp1.write("\n")
        

    elif answer == 2:
        # This is the phase where the output is viewed
        # This is to update the data once entered
        # The updation has to be performed before viewing the data
        temp1 = open("resident_data", "r")
        for line in temp1:
                s = line[3:]
                list = s.split("^")
                l1 = list[2].split("/")
                bd = int(l1[0])
                bm = int(l1[1])
                by = int(l1[2])
                # The age is calculated once again since it is the only value that varies
                if bm != 2 or bd != 29:
                    if tm == 1 or tm == 2 or tm == 4 or tm == 6 or tm == 8 or tm == 9 or tm == 11:
                        d = 31
                    elif tm == 3:
                        if ty % 4 == 0 and (ty % 100 != 0 and ty % 400 == 0):
                            d = 29
                        else:
                            d = 28
                    else:
                        d = 30
                    if by <= ty:
                        def date():
                            if td > bd:
                                ad = td-bd
                            elif td == bd:
                                ad = 0
                            else:
                                n = bd-td
                                ad = d-n
                            return ad
                        if tm > bm:
                            if td > bd:
                                am = tm-bm
                            else:
                                am = tm-bm-1
                            ay = ty-by
                            date()
                        elif tm == bm:
                            date()
                            if date() == 0:
                                am = 0
                                ay = ty-by
                            else:
                                if bd < td:
                                    am = 0
                                    ay = ty-by
                                else:
                                    am = 11
                                    ay = ty-by-1
                        else:
                            date()
                            ch = bm-tm
                            if bd < td:
                                am = 12-ch
                                ay = ty-by
                            else:
                                am = 11-ch
                                ay = ty-by-1
                age = str(ay)+"?"+str(am)+"?"+str(date())
                if ay >= 18:
                    adlt = "Yes"
                else:
                    adlt = "No"
                # The following are the steps to find the indexes between which age comes
                a = line.find("@")
                f = line[a:]
                x = f.find("^")
                h = a+x+1

                # The line is updated
                line = line[:h]+age + "^" + adlt

                # It is the written to another file called temporary
                temp2 = open("temporary", "a")
                temp2.write(line)
                temp2.write("\n")
        temp2 = open("temporary", "r")
        temp1 = open("resident_data", "w")
        # The updated data from temporary are then stored back to resident_data which replaces the already existing data
        for line in temp2:
            temp1.write(line)
        # The data from temporary is the deleted.
        temp2 = open("temporary", "w")
        temp2.truncate(0)

        # The user is asked to input the ID to access the specific resident data
        id = raw_input("Enter your id number : ")
        temp1 = open("resident_data", "r")
        k = 1
        for line in temp1:
            if id in line[:3]:
                j = line[:3].count("$")
                a = line[:(3-j)]
                if a == id:
                    s = line[3:]
                    # The string s is stored into list word by word for the printing purpose
                    list = s.split("^")
                    # The age part is extracted and is split to separate age in years, months and days.
                    l1 = list[8].split("?")
                    # The following condition is checked so as to print the address only once.
                    address = "\t\t\t\tAddress :"+list[0]
                    member_no = "\tMember\t"+str(k)+"\n"
                    name = "Name          :"+list[1]
                    dob = "Date of birth :"+list[2]
                    blood_group = "Blood Group   :"+list[3]
                    disability = "Disabilities  :"+list[4]
                    phno = "Phone Number  :"+list[5]
                    email = "Email ID      :"+list[7]
                    age = "Age           :"+l1[0]+" years "+l1[1]+" months "+l1[2]+" days"
                    status = "Status        :"+list[6]
                    adult = "Adult         :"+list[9]
                    data_list = [member_no, name, dob, blood_group, disability, phno, email, age, status, adult]
                    if k == 1:
                        print("\n\n")
                        for a in address:
                            print(a, end="")
                            time.sleep(0.05)
                        print("\n")
                        for i in data_list:
                            for j in i:
                                print(j, end="")
                                time.sleep(0.05)
                            print("\b")

                        if l1[1] == "0" and l1[2] == "0":
                            hbd = "\t!!!!!Happy Birthday!!!!!"
                            for i in hbd:
                                print(i, end="")
                                time.sleep(0.05)
                            print("\b")
                        k += 1
                    else:
                        print("\n")
                        for i in data_list:
                            for j in i:
                                print(j, end="")
                                time.sleep(0.05)
                            print("\b")

                        if l1[1] == "0" and l1[2] == "0":
                            hbd = "\t!!!!!Happy Birthday!!!!!"
                            for i in hbd:
                                print(i, end="")
                                time.sleep(0.05)
                            print("\b")
                        k += 1
    else:
        print("Invalid input")

    print("\n")
    ch = raw_input("Do you wish to use resident data once again?(y/n)")
    print("\n\n", end="")
    star = "************************************************************************************************************************"
    for i in star:
        print(i,end="")
        time.sleep(.01)

else:
    end = "\t\t\t\t\tTHANK YOU..."
    for i in end:
        print(i, end=" ")
        time.sleep(0.1)
    time.sleep(1)
# ..............................................................................................................
# ..............................................................................................................





