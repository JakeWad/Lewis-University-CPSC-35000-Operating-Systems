import sys

# Get filename and text from command line arguments
filename = sys.argv[1]
text = sys.argv[2]

# Remove quotation marks from text
text = text.strip('"')

# Write text to file
with open(filename, 'w') as f:
    f.write(text)

    
    
To run this program, save it in a file named main.py and run the following command in the terminal: python3 main.py file.txt "hello there!"
This will create a file named file.txt in the same directory as main.py and write the text "hello there!" to it.
