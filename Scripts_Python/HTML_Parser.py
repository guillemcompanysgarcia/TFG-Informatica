import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# the path to the folder containing the Python files
folder_path = 'C:/Users/Guillem/Desktop/'

# initialize the formatter
#formatter = HtmlFormatter(linenos=True, cssclass="source")
formatter = HtmlFormatter(linenos=True, full = True)

# loop through all files in the folder
for filename in os.listdir(folder_path):
    # check if the file is a Python file
    if filename.endswith('.py'):
        # read the file content
        with open(os.path.join(folder_path, filename)) as file:
            code = file.read()
        # format the code to HTML
        formatted_code = highlight(code, PythonLexer(), formatter)
        # write the formatted code to an HTML file
        with open(os.path.join(folder_path, filename.replace('.py', '.html')), 'w') as file:
            file.write(formatted_code)
