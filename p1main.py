"""
COMPSCI 424 Program 1
Name: Tyler Roob
"""
import time

#Initialize Process Classes
class V1_Process:
  def __init__(self,parent):
    self.parent = parent
    self.children =[]

  def add_children(self,children):
      self.children.append(children)

  def remove_child(self,child_pid):
    if child_pid in self.children:
      self.children.remove(child_pid)
class V2_Process:
  def __init__(self,Parent,osib=None):
    self.Parent = Parent
    self.First_Child = None
    self.Younger_Sibiling = None
    self.Older_Sibiling = osib

  def set_y_sib(self):
    if([self.parent].fchild):
      None

#***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***V1***#
def v1(Commands,show_output):
  PCB = create_V1_PCB()
  for command in Commands:
    Action=command[0]
    match Action:
      case 'c':
        parent = command[1]
        process = First_Available_Process(PCB)
        #print(f"Creating Process {process} with parent {parent}")
        v1_create(PCB,process,parent)
      case 'd':
        process = command[1]
        #print(f"Deleting Process {process}, and all children")
        v1_destroy(PCB,process)
    if show_output:
      v1_showProcessInfo(PCB)

def v1_create(PCB,process,parent):
  try:
    #Link to Parent
    PCB[parent].add_children(process)
    #Create Process
    PCB[process] = V1_Process(parent)
  except:
    print(f"Error, Parent doesn't exist")

def v1_destroy(PCB,process):
  parent = PCB[process].parent
  PCB[parent].remove_child(process)
  while PCB[process].children != []:
    for child_index  in PCB[process].children:
      v1_destroy(PCB,child_index)
  #print(f"Destroying: {process}")
  del PCB[process]  

def v1_showProcessInfo(PCBs):
  for x in PCBs:
    if PCBs[x].children!=[]:
      children_list = ""
      for c in PCBs[x].children:
        children_list= children_list + " "
        c=str(c)
        children_list= children_list + c
      print(f"Process {x}: parent is {PCBs[x].parent} and children are {children_list}")
    else:
      print(f"Process {x}: parent is {PCBs[x].parent} and has no children")
  print("")

#***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***V2***#
def v2(commands,show_output):
  PCB = create_V2_PCB()
  command_num = 0
  for command in commands:
    command_num+=1
    #print(f"\nCommand #{command_num}\n")
    Action=command[0]
    if command[1] not in PCB:
      print(f"Error | Object Does Not exist in PCB")
    else:
      match Action:
        case 'c':
          parent = command[1]
          #print(f"\nRunning command 'Create' with Parent {parent}")
          process = First_Available_Process(PCB)
          #print(f"Creating Process {process} with parent {parent}")
          v2_create(PCB,process,parent)
        case 'd':
          process = command[1]
          #print(f"\nRunning command 'Destroy' process {process}")
          #print(f"Deleting Process {process}, and all children")
          v2_destroy(PCB,process)
      if show_output:
        v2_showProcessInfo(PCB)
  
def v2_showProcessInfo(PCB):
  #print("\nCurrent Processes:")
  for process in PCB:
    parent = PCB[process].Parent
    children = None
    if PCB[process].First_Child is not None:
      First_Child = PCB[process].First_Child
      child = First_Child
      children = str(First_Child)
      while True:
        if PCB[child].Younger_Sibiling is not None:
          Younger_Sibiling = PCB[child].Younger_Sibiling
          children+=f" {Younger_Sibiling}"
          child = Younger_Sibiling
        else:
          break
      print(f"Process {process}: Parent is {parent} Children are {children}")
    else:
      print(f"Process {process}: Parent is {parent} and has no children.")
  print("")

    


def v2_destroy(PCB,process):
  #print(f"Destroy {process}")
  while True:
    if PCB[process].First_Child != None: v2_destroy(PCB,PCB[process].First_Child)
    if PCB[process].First_Child == None: break
  Parent = PCB[process].Parent
  if PCB[Parent].First_Child == process:
    if PCB[process].Younger_Sibiling == None:
      PCB[Parent].First_Child = None
    else:
      PCB[Parent].First_Child = PCB[process].Younger_Sibiling
  else:
    Older_Sibiling = PCB[process].Older_Sibiling
    Younger_Sibiling = PCB[process].Younger_Sibiling
    if PCB[Younger_Sibiling] == None:
      PCB[Older_Sibiling].Younger_Sibiling = None
    else:
      PCB[Older_Sibiling].Younger_Sibiling = Younger_Sibiling
      PCB[Younger_Sibiling].Older_Sibiling = Older_Sibiling
  del PCB[process]
  #print(f"Process {process} has been deleted")


def find_Older_Sibiling(PCB,Parent):
  Older_Sibiling = PCB[Parent].First_Child
  while True:
    if PCB[Older_Sibiling].Younger_Sibiling is not None: Older_Sibiling = PCB[Older_Sibiling].Younger_Sibiling
    else:
      return Older_Sibiling
    
def v2_create(PCB,process,Parent):
  try:
    #Link to Parent
    #Check First_Child
    if Parent not in PCB:
      print(f"ERROR | Parent {Parent} does not exist!")
      return
    if PCB[Parent].First_Child is None: #No Sibilings
      PCB[Parent].First_Child = process
      PCB[process] = V2_Process(Parent)
      return
    else:
      Older_Sibiling = find_Older_Sibiling(PCB,Parent)
      PCB[Older_Sibiling].Younger_Sibiling = process
      PCB[process] = V2_Process(Parent,Older_Sibiling)
  except:
    print(f"Error, Parent doesn't exist")

#***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***MAIN***#
#                                              #Initialize PCBs and initial Processes
def create_V1_PCB():
  PCBs_V1 = {}
  PCBs_V1[0] = V1_Process(-1)
  return PCBs_V1
def create_V2_PCB():
  PCBs_V2 = {}
  PCBs_V2[0] = V2_Process(-1)
  return PCBs_V2
#                                                     For Both V1 and V2
def First_Available_Process(PCB):
  for process_id in range (1,16):
    if process_id not in PCB:
      return process_id
  print("No Available Space")
  return False
#                                                     #Initial Functions
def get_commands():
  Commands = []
  while True:
    New_input = Request_Input()
    Action = New_input[0]
    process = New_input[1]
    if Action == 'e': break
    if Action == False: 
      print(f"Error: {process}")
    else:
      Commands.append(New_input)
  return Commands
def Request_Input():
  try:
    new_input = input("Enter commands of the form 'create N', 'destroy N', or 'end', where N is an integer between 0 and 15:")
    if new_input == "end": return ['e',None]
    new_input = new_input.split(" ")
    action = new_input[0]
    item = int(new_input[1])
    if action != "create" and action != "destroy" and action != "end": return [False, "Invalid action item"]
    if item not in range(0,16): return [False, "Invalid Process"]
    match action:
      case "create":
        return ['c',item]
      case "destroy":
        if item == 0: return [False,"Invalid Argument"]
        return ['d',item]
        
  except:
    print("Invalid Argument")
    return [False,"Invalid Argument"]

def main():
  Commands=get_commands()
  print("Beginning V1:\n`")
  v1(Commands,True)
  print("\nEnd of V1\n")
  print("Beginning of V2:\n")
  v2(Commands,True)
  print("\nEnd of V2")
  input("Press Enter to start timings")
  print("Running V1 200 Times")
  v1_start = time.process_time_ns()
  for _ in range(200):
    v1(Commands,False)
  v1_end = time.process_time_ns()
  print("Running V1 200 Times")
  v2_start = time.process_time_ns()
  for _ in range(200):
    v1(Commands,False)
  v2_end = time.process_time_ns()
  v1_running = v1_end-v1_start
  v2_running = v2_end-v1_start
  print(f"V1 start time: {v1_start}")
  print(f"V1 end time: {v1_end}")
  print(f"V1 Running Time: {v1_running}")
  print(f"V2 start time: {v2_start}")
  print(f"V2 end time: {v2_end}")
  print(f"V2 Running Time: {v2_running}")  

main()

# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

