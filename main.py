import os
import sys

import markdown

if len(sys.argv) != 4:
    print("引数は4つ指定してください")
    sys.exit()

if sys.argv[1] != "markdown":
    print("markdownコマンドを指定してください")
    sys.exit()

if not os.path.exists(sys.argv[2]):
    print("存在するファイルパスを指定してください")
    sys.exit()

directory = os.path.dirname(sys.argv[3])

if directory != "" and not os.path.exists(directory):
    print("存在するファルダを指定してください")
    sys.exit()

if sys.argv[3][-4:] != "html":
    print("htmlファイルを指定してください")
    sys.exit()

input_file = sys.argv[2]
output_file = sys.argv[3]

with open(input_file, "r") as file:
        markdown_contents = file.read()
        html_contents = markdown.markdown(markdown_contents, extensions=["tables"])

with open(output_file, "w") as file:
    file.write(html_contents)