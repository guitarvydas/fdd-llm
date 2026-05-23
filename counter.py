import sys
import kernel0d as zd


class Counter:
    def __init__ (self):
        self.max = 5
        self.count = 1
        
    def inc (self):
        self.count += 1
        
def handler (eh, mev):
    self = eh.instance_data
    if self.count < self.max:
        zd.send (eh, "<5", mev.datum.v, mev)
    else:
        zd.send (eh, "5th", mev.datum.v, mev)
    self.inc ()
        
def instantiate (reg, owner, name, arg, template_data):
    name_with_id = zd.gensymbol ("counter")
    self = Counter ()
    return zd.make_leaf (name_with_id, owner, self, arg, handler, None)

def install (reg):
    zd.register_component (reg, zd.mkTemplate ("counter", None, instantiate))
    
