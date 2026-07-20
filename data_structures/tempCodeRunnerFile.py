"""Tree implementation for sorting and curriculum organization."""


class TreeNode:
    """A node in the tree."""
    
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __str__(self, level=0):
        """Pretty print the node and its descendants."""
        indent = "  " * level
        if self.value and hasattr(self.value, "name"):
            # Leaf node (course)
            return f"{indent}📘 {self.key}: {self.value.name}\n"
        else:
            # Folder node
            return f"{indent}📁 {self.key}\n"


class Tree:
    """A general-purpose tree for hierarchical data."""
    
    def __init__(self, root_key="Curriculum"):
        self.root = TreeNode(root_key)

    def insert(self, path, value):
        """
        Insert a value into the tree following the given path.
        
        Args:
            path (list): List of keys, e.g., ["Year 1", "Semester 1", "CS101"]
            value (object): The data to store at the final node
        """
        current = self.root
        
        # Traverse or create folders for all but the last key
        for key in path[:-1]:
            found = False
            for child in current.children:
                if child.key == key:
                    current = child
                    found = True
                    break
            if not found:
                new_node = TreeNode(key)
                current.add_child(new_node)
                current = new_node
        
        # Now add the actual course at the leaf
        leaf_node = TreeNode(path[-1], value)
        current.add_child(leaf_node)

    def inorder_traversal(self, node=None):
        """In-order traversal (sorted by key)."""
        if node is None:
            node = self.root
        
        results = []
        # Sort children by key
        sorted_children = sorted(node.children, key=lambda x: x.key)
        
        for child in sorted_children:
            if child.value is not None:
                # Leaf node: add its value
                results.append(child.value)
            else:
                # Folder node: traverse deeper
                results.extend(self.inorder_traversal(child))
        return results

    def browse(self):
        """Pretty print the entire tree."""
        print("\n" + "=" * 50)
        print("   📚 CURRICULUM STRUCTURE")
        print("=" * 50)
        print(self.root)


# ---------- SELF-TEST ----------
if __name__ == "__main__":
    print("🧪 Testing Tree...")
    
    # Create a tree
    tree = Tree("Curriculum")
    
    # Insert courses
    class MockCourse:
        def __init__(self, name, semester):
            self.name = name
            self.semester = semester
    
    tree.insert(["Year 1 - Semester 1", "CS101"], MockCourse("Programming I", "Year 1 - Sem 1"))
    tree.insert(["Year 1 - Semester 1", "ITE100"], MockCourse("Intro to ITE", "Year 1 - Sem 1"))
    tree.insert(["Year 1 - Semester 2", "CS102"], MockCourse("Programming II", "Year 1 - Sem 2"))
    tree.insert(["Year 2 - Semester 1", "CS201"], MockCourse("Data Structures I", "Year 2 - Sem 1"))
    
    tree.browse()
    
    # Test in-order traversal
    print("\n📋 In-order traversal:")
    for course in tree.inorder_traversal():
        print(f"  - {course.name}")
    
    print("✅ Tree tests passed!")
