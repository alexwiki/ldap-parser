import re
import json
def ldap_to_json():
   
    dictionary={}
    counter = 0
    dictionary[counter]={}
    with open('./ldap_logfile.log', 'r') as f:
        for line in f:
            if "END" in line:
                counter+=1
                dictionary[counter] = {}
            else:
                if ":" in line:
                    left_variable  = line.split(':')[0]         #take the string, left from the ":"
                    right_variable = line.split(':')[1]        #take the string , right from the ":"
                    right_variable = right_variable.replace("\n","")
                    right_variable = right_variable.replace(" ","")
                    
                    dictionary[counter][left_variable]= right_variable
    print(dictionary)

    #write a dictionary to json file
    with open('./report.json', 'w') as f:
        json.dump(dictionary,indent=4, fp=f)

ldap_to_json()
