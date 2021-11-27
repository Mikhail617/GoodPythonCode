import sys
sys.path.append("../src/")
import linked_list

def test_linked_list():
    ll = linked_list.LinkedList()
    ll.add_to_tail(linked_list.Node("knowledge"))
    ll.add_to_tail(linked_list.Node("wisdom"))
    ll.add_to_tail(linked_list.Node("understanding"))
    ll.add_to_tail(linked_list.Node("freedom"))
    ll.add_to_tail(linked_list.Node("justice"))
    ll.add_to_tail(linked_list.Node("equality"))
    ll.add_to_tail(linked_list.Node("food"))
    ll.add_to_tail(linked_list.Node("clothing"))
    ll.add_to_tail(linked_list.Node("shelter"))
    ll.add_to_tail(linked_list.Node("love"))
    ll.add_to_tail(linked_list.Node("peace"))
    ll.add_to_tail(linked_list.Node("happiness"))
    print(ll)

if __name__ == "__main__":
    test_linked_list()
