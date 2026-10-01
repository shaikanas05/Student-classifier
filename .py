#Get email from user 

email=input("enter your email message.\n")


#covert email to lowercase 


email= email lower()

#Check for spam words

  for word in email:
      
      spam=true
       break 


   #Display result
 
   if spam:
      print("\nResult:spam mail")
   
   else:
        print("\nresult:Not spam mail")