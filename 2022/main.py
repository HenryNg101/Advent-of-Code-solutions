# Template
class Directory:
  def __init__(filename: str, parent_dir: Directory) -> None:
    self.filename = filename
    self.parent_dir = parent_dir
    self.directories = []
    self.files = []

content = open("input").read().split('\n')
