# Template
class Directory:
  def __init__(filename: str, parent_dir: Directory) -> None:
    self.filename = filename
    self.parent_dir = parent_dir
    self.directories = []   #Contains Directory objects only 
    self.files = []   #Contains file sizes only 

content = open("input").read().split('\n')
content_id = 0

root_dir = Directory("/", None)

while(content_id < len(content)):
  