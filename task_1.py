class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Допоміжна функція для побудови дерева."""
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def get_max_value(node):
    """
    Знаходить найбільше значення у BST.
    Логіка: йти вправо до упору.
    """
    current = node
    # Якщо дерево порожнє
    if current is None:
        return None
    
    # Рухаємось вправо, поки є правий нащадок
    while current.right:
        current = current.right
        
    return current.val

if __name__ == "__main__":
    # Створюємо тестове дерево
    root = Node(20)
    insert(root, 10)
    insert(root, 30)
    insert(root, 40)
    insert(root, 25)

    print(f"Максимальне значення в дереві: {get_max_value(root)}")
    # Очікується: 40
