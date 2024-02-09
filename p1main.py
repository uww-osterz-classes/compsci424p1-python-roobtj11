"""
COMPSCI 424 Program 1
Name: Tyler Roob
"""
import time



class PCB:
  def __init__(self,parent):
    self.parent = parent
    self.children = [None]

  def __set_children__(self,children):
      self.children.append(children)
      if(self.children[0]==None):
        self.children.pop(0)

class commands:
  def __init__(self, command, n):
    self.command = command
    self.n = n

def showProcessInfo(PCBs):
  for x in range(0,len(PCBs)):
    if PCBs[x].children[0]!=None:
      children_list = ""
      for c in PCBs[x].children:
        children_list= children_list + " "
        c=str(c)
        children_list= children_list + c
      print("Process ",x,": parent is ",PCBs[x].parent," and children are",children_list)
    else:
      print("Process ",x,": parent is ",PCBs[x].parent," and has no children")

def v1(command_list):
  print("v1:")
  v1_PCBs = list()
  for command in command_list:
    if command.command == 'create':
      if command.n in range (0, len(v1_PCBs)) or command.n == -1: 
        if command.n == -1 or v1_PCBs[command.n] != None: 
          v1_PCBs.append(PCB(command.n))
          if command.n != -1:
            v1_PCBs[command.n].__set_children__(len(v1_PCBs)-1)
      else:
        print("Parent is out of range!")
    elif command.command == 'destroy':
      v1_PCBs.remove(command.n)
    
    showProcessInfo(v1_PCBs)




def create(parent):
  PCBs.append(PCB(parent))
  PCBs[parent].__set_children__(len(PCBs)-1)

def destroy(p):
  for x in PCBs[p].children:
    PCBs.pop(x)
  PCBs.pop(p)



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

