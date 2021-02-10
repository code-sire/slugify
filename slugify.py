# Slugify

# "re" is used for string matching operations.
import re

# Defined a process to used when wanting to normalize string data.
def slugify(text):
    # Step 1 - Removes special characters
    #          Removes spaces before and after string
    #          Converts the string to lowercase
    text = re.sub('[^\w\s-]', '', text).strip().lower()

    # Step 2 - Changes spaces and hyphens to underscores.    
    text = re.sub(r'[- ]+', '_', text)
    
    # Step 3 - Provide the modified text out to the requesting process.
    return (text)