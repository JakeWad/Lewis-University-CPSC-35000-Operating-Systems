import sys

# Get filename and text from command line arguments
filename = sys.argv[1]
text = sys.argv[2]

# Remove quotation marks from text
text = text.strip('"')

# Write text to file
with open(filename, 'w') as f:
    f.write(text)

**********************************************************************************    
    
To run this Python code:

Open a text editor (Notepad or Visual Studio Code) and paste the code into a new file.

Save the file with a .py extension, such as "main.py".

Open a command prompt or terminal window.

Navigate to the directory where you saved the "main.py" file.

Type the following command:

python3 main.py file.txt "extra credit"
(Replace "file.txt" with the filename you want to write to, and "extra credit" with the text you want to write.)

Press Enter to run the command.

The program should create a new file named "file.txt" in the same directory as the "main.py" file, and write the text "extra credit" to that file.
