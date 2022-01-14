#word_count_game_project
n=input("tell me what do you feel today ")
leng=len(n.split())
print("the number of words are ",leng)
#biography_info_game_projects
name=input("Name: ")
if(name.isalpha()==True):
    Name=name
else:
    print("invalid entry for namae give me your real name ")
DOB=input("dob:")
if(DOB.isspace()==True):
    if(DOB.isalpha()==True or DOB.isdigit()==True ):
        my=DOB    
    else:
        print("invalid entry ")
date=DOB    
print("\n\nBIOGRAPHY INFO\n")
print("NAME:",Name,"\n")
print("DATE OF BIRTH ",date,"\n"
