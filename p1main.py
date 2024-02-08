"""
COMPSCI 424 Program 1
Name: Tyler Roob
"""
import time

PCBs = []
PCB = list()
children = list()

def c(parent,children):
  PCBs.append(PCB.append(parent
    
###
#class PCB:
#  def __init__(self,parent, children):
#    self.parent = parent
#    self.children = children
#  def __init__(self,parent):
#    self.parent = parent
#    self.children = None
###
PCBs = list()
PCBs.append(

def create_parentPid(id){
}

def v1(){

}

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

