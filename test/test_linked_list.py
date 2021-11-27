import sys
sys.path.append("../src/")
import linked_list
import unittest

class LinkedListTesting(unittest.TestCase):
	def test_linked_list_add_to_tail(self):
		ll = linked_list.LinkedList()
		ll.add_to_tail(linked_list.Node("knowledge"))
		self.assertEqual("knowledge", str(ll.head))

	def test_linked_list_remove_from_head(self):
		ll = linked_list.LinkedList()
		ll.add_to_tail(linked_list.Node("knowledge"))
		ll.remove_from_head()
		self.assertEqual("None", str(ll.head))

	def test_linked_list_repr(self):
		ll = get_test_ll()
		expected_result = """knowledge -> wisdom -> understanding -> freedom -> justice -> equality -> food -> clothing -> shelter -> love -> peace -> happiness"""
		self.assertEqual(expected_result, repr(ll))

	def test_linked_list_size(self):
		ll = get_test_ll()
		self.assertEqual(12, ll.size())

def get_test_ll():
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
    return ll

if __name__ == "__main__":
    unittest.main()
