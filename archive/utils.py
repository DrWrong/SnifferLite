from scapy.all import load_protocols, ConditionalField, Emph, Packet

def show_in_dict(instance, indent=3, lvl="", label_lvl=""):
    showdict = {}
    """Prints a hierarchical view of the packet. "indent" gives the size of indentation for each layer."""
    for f in instance.fields_desc:
        if isinstance(f, ConditionalField) and not f._evalcond(instance):
            continue
        fvalue = instance.getfieldval(f.name)
        if isinstance(fvalue, Packet) or (f.islist and f.holds_packets and type(fvalue) is list):
            pass
#            print "%s  \\%-10s\\" % (label_lvl+lvl, ncol(f.name))
#            fvalue_gen = SetGen(fvalue,_iterpacket=0)
#            for fvalue in fvalue_gen:
#                fvalue.show(indent=indent, label_lvl=label_lvl+lvl+"   |")
        else:
            showdict[f.name] = f.i2repr(instance, fvalue)

    return showdict
