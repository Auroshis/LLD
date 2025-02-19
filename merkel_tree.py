import hashlib
from typing import List, Optional

"""
In case of merkel tree, we are building the tree from leaf nodes towards the root.
Handle even/odd and empty node cases. 
Data is present only in the leaf nodes.
If a subtree hash is different from it's previous then update only those portions.
"""

# Merkle Node class
class MerkleNode:

    def __init__(self, hash_value: str, left: Optional['MerkleNode'] = None, right: Optional['MerkleNode'] = None):
        self.hash = hash_value
        self.left = left
        self.right = right

# Function to compute SHA-256 hash
def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# Function to build a Merkle Tree
def build_merkle_tree(data_blocks: List[str]) -> Optional[MerkleNode]:
    if not data_blocks:
        return None

    nodes = [MerkleNode(hash_data(data)) for data in data_blocks]

    while len(nodes) > 1:
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left
            combined_hash = hash_data(left.hash + right.hash)
            new_level.append(MerkleNode(combined_hash, left, right))
        nodes = new_level

    return nodes[0]  # Root node

# Function to compare two Merkle Trees
def compare_merkle_trees(root1: Optional[MerkleNode], root2: Optional[MerkleNode]) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.hash != root2.hash:
        return False

    return compare_merkle_trees(root1.left, root2.left) and compare_merkle_trees(root1.right, root2.right)

# Example usage
if __name__ == "__main__":
    data_blocks1 = ["A", "B", "C", "D"]
    data_blocks2 = ["A1", "B", "C", "D"]  # Different data

    tree1 = build_merkle_tree(data_blocks1)
    tree2 = build_merkle_tree(data_blocks2)

    print("Tree 1 Root:", tree1.hash)
    print("Tree 2 Root:", tree2.hash)
    print("Trees are identical:", compare_merkle_trees(tree1, tree2))
