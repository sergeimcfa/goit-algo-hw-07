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

def get_min_value(node):
    """
    Знаходить найменше значення у BST.
    Логіка: йти вліво до упору.
    """
    current = node
    # Якщо дерево порожнє
    if current is None:
        return None

    # Рухаємось вліво, поки є лівий нащадок
    while current.left:
        current = current.left
        
    return current.val

if __name__ == "__main__":
    # Створюємо тестове дерево
    root = Node(20)
    insert(root, 10)
    insert(root, 5)  # Найменше
    insert(root, 30)
    insert(root, 2)  # А ні, ось це найменше

    print(f"Мінімальне значення в дереві: {get_min_value(root)}")
    # Очікується: 2
