import sys

# Get filename and text from command line arguments
filename = sys.argv[1]
text = sys.argv[2]

# Remove quotation marks from text
text = text.strip('"')

# Write text to file
with open(filename, 'w') as f:
    f.write(text)
