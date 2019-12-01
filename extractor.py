import os
import PyPDF2 # PDF -> text
import re # regex
import json # print dictionary nicely
# import csv # save dictionary to .csv

rootdir = r"path" # location of folder with PDFs

# email_list = [] # create a list
email_addresses = {} # create a dictionary
# print(len(email_list)) # debug: check list's size

print("Finding and extracting email addresses from", rootdir, "and its subdirs - hold tight for a minute...")

counter = 0

for subdir, dirs, files in os.walk(rootdir): # FIX: it'll take anything, not only PDFs - if it finds a not-PDF program will crash
    for file in files:
        
        counter +=1 

        # print("File path:", os.path.join(subdir, file))  # debug: output path name of the file

        full_file_path = os.path.join(subdir, file) # full path of the file

        pdfFileObj = open(full_file_path, "rb")  # read in binary mode
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # store PdfFileReader object in pdfReader

        # print("# of pages:", pdfReader.numPages) # debug: output number of file's pages

        pageObj = pdfReader.getPage(0)  # look only at page 1 of the file

        full_text = pageObj.extractText() # extract text from the PDF

        find_email = re.search("[._+a-zA-z0-9]+@[a-zA-z0-9]+\.[a-zA-z]+", full_text) # regex to get only the email address

        # counter +=1 
        # print("Counter:", counter)

        if find_email is not None:
            found_email = find_email.group(0) # if we found an email let's save it
            
            # print("success", found_email) # debug
            # email_list.append(found_email) # add email address to list
            email_addresses[file] = found_email # add email address to dictionary
            
            # print(len(email_list)) # debug: check list's size
            
        else:
            # print("fail - email not found") # debug
            # email_list.append("-") # if email not found then add "-" so we know something went wrong
            email_addresses[file] = "-" # if email not found then add "-" so we know something went wrong

            # print(len(email_list)) # debug: check list's size

# === print list === 
# print(email_list) # 0; not nice
# print('\n'.join(email_list)) # 1; nice
# print(*email_list, sep='\n') # 2; nice 

# === print dict in JSON and save to .json ===
# print(json.dumps(email_addresses, indent=4, sort_keys=True))
with open('emails.json', 'w', encoding='utf-8') as file:
    json.dump(email_addresses,file,ensure_ascii=False, indent=4)

distinct_email_addresses = [] # create empty list to count number of distinct email addresses
for email_address in email_addresses.values(): 
  if email_address in distinct_email_addresses: 
    continue 
  else:
    distinct_email_addresses.append(email_address)

print("Done! File 'emails.json' saved. Script went through", counter, "files to find", len(distinct_email_addresses), "email addresses. Success rate: %.2f%% :)" % (100*float(len(distinct_email_addresses)/counter)))

# === in order to complete: convert JSON -> CSV online, upload to Excel, transpose = profit ✅ ===