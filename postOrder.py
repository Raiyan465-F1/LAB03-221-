def build_postorder(inorder: list, preorder):
    if not preorder or not inorder:
        return []
    
    root = preorder[0]
    root_index = inorder.index(root)  # Find the root in inorder
    
    left_inorder = inorder[:root_index]  # Left subtree in inorder
    right_inorder = inorder[root_index + 1:]  # Right subtree in inorder

    left_preorder = preorder[1:1 + len(left_inorder)]  # Left subtree in preorder
    right_preorder = preorder[1 + len(left_inorder):]  # Right subtree in preorder

    # Recursively compute post-order
    left_postorder = build_postorder(left_inorder, left_preorder)
    right_postorder = build_postorder(right_inorder, right_preorder)
    
    return left_postorder + right_postorder + [root]


n = int(input())  # Number of nodes
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

postorder = build_postorder(inorder, preorder)


print(*postorder)
