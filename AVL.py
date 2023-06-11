import sys


# tree node class
# reference: Programiz https://www.programiz.com/dsa/avl-tree
class TreeNode(object):
    # initialiser with class objects
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class
# reference: Programiz https://www.programiz.com/dsa/avl-tree
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # delete node function
    def delete_node(self, root, key):

        # search for inputted node to delete
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes after deleting node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

        # rotate AVL tree left function
        # reference: Programiz https://www.programiz.com/dsa/avl-tree

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # rotate AVL tree right function
    # reference: Programiz https://www.programiz.com/dsa/avl-tree
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # return height of node function
    # reference: Programiz https://www.programiz.com/dsa/avl-tree
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    # reference: Programiz https://www.programiz.com/dsa/avl-tree
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # get a nodes smallest node value function
    # reference: Programiz https://www.programiz.com/dsa/avl-tree
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # pre order traversal function
    def preOrder(self, root):
        if not root:
            return
        msg = " "
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
        return msg

    # in order traversal function
    def inOrder(self, root):
        if not root:
            return
        msg = " "
        self.inOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.inOrder(root.right)
        return msg

    # post order traversal function
    def postOrder(self, root):
        if not root:
            return
        msg = " "
        self.postOrder(root.left)
        self.postOrder(root.right)
        print("{0} ".format(root.key), end="")
        return msg

    # Print the tree
    def printTreeNoHB(self,
                      root):  ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        def display(root):  ##  AUTHOR: Original: J.V.     Edit: BcK
            #   No child.
            if root.right is None and root.left is None:
                line = str(root.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            #   Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                nodeOutput = (str(root.key))
                keyLength = len(nodeOutput)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput
                second_line = x * ' ' + '/' + (n - x - 1 + keyLength) * ' '
                shifted_lines = [line + keyLength * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, n + keyLength // 2

            #   Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                nodeOutput = str(root.key)
                keyLength = len(nodeOutput)
                first_line = nodeOutput + x * '_' + (n - x) * ' '
                second_line = (keyLength + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [keyLength * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, keyLength // 2

            #   Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            nodeOutput = str(root.key)
            keyLength = len(nodeOutput)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + keyLength + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + keyLength * ' ' + b for a, b in zipped_lines]
            return lines, n + m + keyLength, max(p, q) + 2, n + keyLength // 2

        lines = []
        if root != None:
            lines, *_ = display(root)
            print("\t\t== AVL Tree ==")
            print()
        if lines == []:
            print("No tree found, please rebuild a new Tree.\n")
            return -1
        for line in lines:
            print(line)
        print()

    # function to display height and balance of all nodes
    def display(self, root, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''

        if (root != None):
            print(root.key, "[" + str(self.getHeight(root)) + ":" + str(self.getBalance(root)) + "]")
            if root.left != None:
                self.display(root.left, level + 1, '<')
            if root.left != None:
                self.display(root.right, level + 1, '>')

    # count number children a node has
    # reference: cppsecrets     Author: P Avinash Rao https://cppsecrets.com/users/21597118105110971151049510511664121971041111114699111109/Python-program-to-count-non-leaf-nodes-in-a-binary-tree.php
    def children_count(self, root):
        # return number of children
        cnt = 0
        if root.left:
            cnt += 1
        if root.right:
            cnt += 1
        return cnt

    # display the non-leaf nodes of AVL tree
    # reference: cppsecrets     Author: P Avinash Rao https://cppsecrets.com/users/21597118105110971151049510511664121971041111114699111109/Python-program-to-count-non-leaf-nodes-in-a-binary-tree.php
    def printNonLeafNodes(self, root):
        # prints non-leaf nodes in inorder traversal order
        if self.children_count(root) != 0:
            print(root.key, end=" ")
            if root.left:
                self.printNonLeafNodes(root.left)
            if root.right:
                self.printNonLeafNodes(root.right)
        else:
            return


# prints the leaf nodes of AVL tree
def printLeafNodes(root):
    # If node is null, return
    if (not root):
        return

    # If node is leaf node,
    # print its data
    if (not root.left and
            not root.right):
        print(root.key,
              end=" ")
        return

    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)

    # If right child exists,
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)


# menu UI function
def MainMenu():
    print("\n")
    print("1. Display the AVL tree, showing the height and balance factor for each node")
    print("2. Print the pre-order, in-order, and post-order traversal sequences of the AVL tree ")
    print("3. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately) ")
    print("4. Insert a new integer key into the AVL tree ")
    print("5. Delete an integer key from the AVL tree")
    print("6. Exit ")


# Usage example
if __name__ == "__main__":

    print("1). Pre-load a sequence of integers to build a AVL")
    print("2). Manually enter integer values/keys, one by one, to build a AVL")
    print("3). exit ")

    # get user to pre-load, manually load an AVL tree or exit code.
    while True:
        try:
            optionInput = int(input("\n Type in 1 or 2.\n"))
            if optionInput == 1:
                nums = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
                break;
            elif optionInput == 2:
                nums = []
                while True:
                    try:
                        numberInput = int(input("Input the integers for BST.\n"))
                        print("Once complete. please enter 0 to continue.\n")
                        nums.append(numberInput)
                        if numberInput == 0:
                            nums.pop()
                            break

                    except ValueError:
                        print("Invalid input. Please try again.\n")
                break

            elif optionInput == 3:
                print("BYE BYE")
                quit()
                break
            else:
                print("Invalid input. Please try again.\n")

        except ValueError:
            print("Invalid input. Please try again.\n")

    myTree = AVLTree()
    root = None

    print(nums)

    # insert list values into tree
    for num in nums:
        root = myTree.insert_node(root, num)

    MainMenu()

    # test user input is correct
    while True:
        try:
            mainInput = int(input("\nType in an integer from 1 to 6.\n"))
            # display AVL tree with heights and balance factors
            if mainInput == 1:
                myTree.printTreeNoHB(root)
                print("\n == Heights & balance factors (in pre-order traversal order) ==\n")
                myTree.display(root)
                MainMenu()

            # display order of traversals
            if mainInput == 2:
                print("\nPre-order Traversal: ")
                print(myTree.preOrder(root))
                print("\nIn-order Traversal: ")
                print(myTree.inOrder(root))
                print("\nPost-order Traveral: ")
                print(myTree.postOrder(root))
                MainMenu()

            # display leaf and non-leaf nodes
            if mainInput == 3:
                print("\nThese are all the leaf nodes: ")
                printLeafNodes(root)
                print("\n")
                print("\nThese are all the non-leaf nodes: ")
                myTree.printNonLeafNodes(root)
                MainMenu()

            # insert a value to AVL tree
            if mainInput == 4:

                print("Enter an integer to be added to the AVl tree\n")

                while True:
                    try:
                        userInput = int(input("Input an integer: "))
                        if userInput in nums:
                            print("ERROR: node key already exists in the AVL\n")
                        else:
                            nums.append(userInput)
                            root = myTree.insert_node(root, userInput)
                            print(userInput, "was successfully added to the AVL.\n")
                            break
                    except ValueError:
                        print("Invalid Input. Please try again.\n")

                print("\n == AVL tree (in BFS traversal order, without hights & balance factors) ==\n")
                myTree.printTreeNoHB(root)

                MainMenu()

            # delete a value from the AVL tree
            if mainInput == 5:
                while True:
                    try:
                        userInput = int(input("Input an integer: "))
                        if userInput not in nums:
                            print("ERROR: node doesnt exist in the AVL\n")
                        else:
                            root = myTree.delete_node(root, userInput)
                            print("After Deletion: ")
                            myTree.printTreeNoHB(root)
                            print(userInput, "was successfully deleted from the AVL.\n")
                            nums.remove(userInput)
                            break
                    except ValueError:
                        print("Invalid Input. Please try again.\n")
                MainMenu()

            # exit program
            if mainInput == 6:
                print("\nBYE BYE")
                break
        except ValueError:
            print("Invalid Input. Please try again.\n")