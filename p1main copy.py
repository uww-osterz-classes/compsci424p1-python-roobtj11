
"""
COMPSCI 424 Program 1
Name: Tyler Roob
"""
import time



PCBs = []

class PCB:
  def __init__(self,pid):
    self.pid = pid
    self.parent = -1
    self.children = [None]
  def __init__(self,parent, children):
    self.parent = parent
    self.children = [children]

  def __init__(self,parent):
    self.parent = parent
    self.children = [None]

  def __set_children__(self,children):
      self.children.append(children)
      if(self.children[0]==None):
        self.children.pop(0)
      
def showProcessInfo():
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

def first():
  PCBs.append(PCB(-1))
  print("Creating New Root")

def create(parent):
  PCBs.append(PCB(parent))
  PCBs[parent].__set_children__(len(PCBs)-1)

def destroy(p):
  for x in PCBs[p].children:
    PCBs.pop(x)
  PCBs.pop(p)

class commands:
  def __init__(self, command, n):
    self.command = command
    self.n = n

def main():
  commands = list()
  while True:
    c = input("enter commands of the form 'create N', 'destroy N', or 'end', where N is an integer between 0 and 15:")
    c = c.split(" ")
    if c[0] == 'end':
      break
    if len(c) == 2:
      if c[0] == 'create' or c[0] == 'destroy':
        if int(c[1]) in range(0,16):
          commands.append(commands(c[0],int(c[1])))
        else:
          ic()
      else:
        ic()
    else:
      ic()
  



def ic():
  print("Invalid command")

main()


first(PCBs)
create(0,PCBs)
create(1,PCBs)
create(1,PCBs)
create(1,PCBs)
create(3,PCBs)
showProcessInfo(PCBs)
"""
Version 1
Version 1 of the process creation hierarchy uses linked lists to keep track of child processes. In Version 1, each process's control block (PCB) contains

a pointer to its parent process and
a linked list of pointers to 0 or more child processes.
For the purposes of performance evaluation, the PCBs are simplified as follows:

All PCBs are implemented as an array of size n.
Each process is referred to by the PCB index, 0 through (n - 1).
Each PCB is a structure consisting of only two fields:
parent: a PCB index corresponding to the process's creator
children: a pointer to a linked list, where each list element contains the PCB index of one child process
The necessary functions are simplified as follows:

create(p) represents the create function executed by process PCB[p]. The function creates a new child process PCB[q] of process PCB[p] by performing the following tasks:
allocate a free PCB[q]
record the parent's index, p, in PCB[q]
initialize the list of children of PCB[q] as empty
create a new link containing the child's index q and appends the link to the linked list of PCB[p]
destroy(p) represents the destroy function executed by process PCB[p]. The function recursively destroys all descendant processes (child, grandchild, etc.) of process PCB[p] by performing the following tasks:
for each element q on the linked list of children of PCB[p]:
destroy(q) /* recursively destroy all descendants */
free PCB[q]
deallocate the element q from the linked list
"""

# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

