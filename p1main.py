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

  def remove_child(self,child_pid):
    if child_pid in self.children:
      self.children.remove(child_pid)

class PCBv2:
  def __init__(self,parent,osib=None):
    self.parent = parent
    self.fchild = None
    self.ysib = None
    self.osib = osib
  def set_y_sib(self):
    if([self.parent].fchild):
      None

def find_OlderSib(PCB,older_sib):
  if PCB[older_sib].ysib == None:
    return older_sib
  else:
    return find_OlderSib(PCB,PCB[older_sib].ysib)

def get_ys(PCBs,pid):
  if PCBs[pid].ysib != None:
    a = [True, PCBs[pid].ysib]
    return a
  else:
    return [False]

def showV2(PCBs):
  for x in PCBs:
    children = []
    t=True
    if PCBs[x].fchild != None:
      children.append(PCBs[x].fchild)
      child = PCBs[x].fchild
      while (t==True):
        result = get_ys(PCBs,child)
        if result[0]:
          child = result[1]
          children.append(child)
        else:
          t = result[0]
      print(f"Process {x}: parent is {PCBs[x].parent}, and has children {children}")
    else:
      print(f"Process {x}: parent is {PCBs[x].parent}, and has no children")
def destroy_v2(PCBs,pid):
  t=1
  while t==1:
    if PCBs[pid].fchild is None:
      parent = PCBs[pid].parent
      if PCBs[parent].fchild == pid:
        if PCBs[pid].ysib is not None:
          PCBs[parent].fchild = PCBs[pid].ysib
          PCBs[PCBs[pid].ysib].osib = None
        else:
          PCBs[parent].fchild = None
      else:
        PCBs[PCBs[pid].osib].ysib = PCBs[pid].ysib
        PCBs[PCBs[pid].ysib].osib = PCBs[pid].osib
      del PCBs[pid]
      break
    else:
      destroy_v2(PCBs,PCBs[pid].fchild)


def v2(command_list):
  print("v2:")
  pid=1
  v2_PCBs = {}
  v2_PCBs[0] = PCBv2(-1)

  for command in command_list:
    if command.command == 'create':
      PID_parent = command.n
      print(f"Trying to Create {pid} with Parent {PID_parent}")
      if PID_parent in v2_PCBs:
        
        #check for Older Sibiling:
        if v2_PCBs[PID_parent].fchild != None:
          osib = find_OlderSib(v2_PCBs,v2_PCBs[PID_parent].fchild)
          v2_PCBs[pid] = PCBv2(PID_parent,osib)
          v2_PCBs[osib].ysib = pid
        else:
          v2_PCBs[PID_parent].fchild = pid
          v2_PCBs[pid] = PCBv2(PID_parent)
        print(f"Created {pid} with Parent {PID_parent}")
        pid+=1
      else:
        print(f"ERROR: Parent {command.n} does not exist")
    elif command.command == 'destroy':
      pid = command.n
      print(f"Trying to destroy {pid}")
      destroy_v2(v2_PCBs,pid)
    showV2(v2_PCBs)


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
      print(f"Process {x}: parent is {PCBs[x].parent} and children are {children_list}")
    else:
      print(f"Process {x}: parent is {PCBs[x].parent}, and has no children")

def destroy(process,PCBs):
  print(f"Destroy {process}:")
  parent_index = PCBs[process].parent

  PCBs[parent_index].children.remove(process)
  print(PCBs[process].children)
  while PCBs[process].children != []:
    for child_index  in PCBs[process].children:
      destroy(child_index,PCBs)
  print(f"Destroying: {PCBs[process]}")
  del PCBs[process]  

def v1(command_list):
  print("v1:")
  p = 1
  v1_PCBs = {}
  v1_PCBs[0] = PCB(-1)
  for command in command_list:
    if command.command == 'create':
      print(f"Trying to Create {p} with Parent {command.n}")
      if command.n in v1_PCBs:
        print(f"Created {p} with Parent {command.n}")
        v1_PCBs[p] = PCB(command.n)
        v1_PCBs[command.n].__set_children__(p)
        p = p + 1
      else:
        print("Parent DNE!")
    elif command.command == 'destroy':
      print(f"Destroy {command.n}:")
      destroy(command.n,v1_PCBs)
    
    showProcessInfo(v1_PCBs)





def main():
  commands_list = list()
  while True:
    c = input("enter commands of the form 'create N', 'destroy N', or 'end', where N is an integer between 0 and 15:")
    c = c.split(" ")
    if c[0] == 'end':
      break
    if len(c) == 2:
      if c[0] == 'create' or c[0] == 'destroy':
        if int(c[1]) in range(0,16):
          commands_list.append(commands(c[0],int(c[1])))
        else:
          ic()
      else:
        ic()
    else:
      ic()
  v1(commands_list)
  v2(commands_list)
  



def ic():
  print("Invalid command")

main()

# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

