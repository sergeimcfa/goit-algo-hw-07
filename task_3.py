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

def get_sum_values(node):
    """
    Знаходить суму всіх значень у дереві.
    Логіка: значення поточного вузла + сума лівого + сума правого.
    """
    # Базовий випадок рекурсії: якщо вузла немає
    if node is None:
        return 0
    
    # Рекурсивний виклик для лівого та правого піддерев
    return node.val + get_sum_values(node.left) + get_sum_values(node.right)

if __name__ == "__main__":
    # Створюємо тестове дерево
    root = Node(20)
    insert(root, 10)
    insert(root, 30)
    insert(root, 5)
    insert(root, 15)
    
    # Розрахунок: 20 + 10 + 30 + 5 + 15 = 80
    print(f"Сума всіх значень у дереві: {get_sum_values(root)}")
