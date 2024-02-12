"""
COMPSCI 424 Program 1
Name: Tyler Roob
"""
import time

class PCB:
  def __init__(self,parent):
    self.parent = parent
    self.children = []

  def __set_children__(self,children):
      self.children.append(children)
      if(self.children[0]==None):
        self.children.pop(0)

class commands:
  def __init__(self, command, n):
    self.command = command
    self.n = n

def showProcessInfo(PCBs):
  for x in PCBs:
    if PCBs[x].children!=[]:
      children_list = ""
      for c in PCBs[x].children:
        children_list= children_list + " "
        c=str(c)
        children_list= children_list + c
      print("Process ",x,": parent is ",PCBs[x].parent," and children are",children_list)
    else:
      print("Process ",x,": parent is ",PCBs[x].parent," and has no children")

def v1(command_list):
#  print("v1:")
  p = 0
  v1_PCBs = {}
  for command in command_list:
    if command.command == 'create':
#      print(f"Trying to Create {p} with Parent {command.n}")
      if command.n == -1 or command.n in v1_PCBs:
#        print(f"Created {p} with Parent {command.n}")
        v1_PCBs[p] = PCB(command.n)
        
        if command.n != -1:
          v1_PCBs[command.n].__set_children__(p)
        p = p + 1
#      else:
#        print("Parent DNE!")
    elif command.command == 'destroy':
#      print(f"Destroy {command.n}:")
      destroy(command.n,v1_PCBs)
    
  showProcessInfo(v1_PCBs)




def create(parent):
  PCBs.append(PCB(parent))
  PCBs[parent].__set_children__(len(PCBs)-1)

def destroy(process,PCBs):
#  print(f"Destroy {process}:")
  parent_index = PCBs[process].parent

  PCBs[parent_index].children.remove(process)
#  print(PCBs[process].children)
  while PCBs[process].children != []:
    for child_index  in PCBs[process].children:
      destroy(child_index,PCBs)
#  print(f"Destroying: {PCBs[process]}")
  del PCBs[process]  



def main():
  commands_list = list()
  while True:
    c = input("enter commands of the form 'create N', 'destroy N', or 'end', where N is an integer between 0 and 15:")
    c = c.split(" ")
    if c[0] == 'end':
      break
    if len(c) == 2:
      if c[0] == 'create' or c[0] == 'destroy':
        if int(c[1]) in range(0,16) or (len(commands_list) == 0 and int(c[1]) == -1 and c[0] != 'destroy'):
          commands_list.append(commands(c[0],int(c[1])))
        else:
          ic()
      else:
        ic()
    else:
      ic()
  v1(commands_list)
  



def ic():
  print("Invalid command")

main()

# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

