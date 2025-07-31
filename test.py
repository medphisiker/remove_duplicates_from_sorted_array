from main import Solution

def test():
    # Example 1
    solution = Solution()
    nums = [1,1,2]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1,2]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Example 2
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0,1,2,3,4]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Test 1 без дублей
    solution = Solution()
    nums = [0,1,2,3]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [0,1,2,3]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Test 2 1 элемент
    solution = Solution()
    nums = [0]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [0]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Test 3 отрицательные элементы
    solution = Solution()
    nums = [-3,-3, 0, 2, 2, 3]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [-3, 0, 2, 3]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Test 4 все элементы одинаковые
    solution = Solution()
    nums = [2,2,2,2,2,2,2,2]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [2]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")
    
    # Test 5 крайние значения
    solution = Solution()
    nums = [-100, -100, -3, 0, 0, 0, 100, 100]
    print(f"\nВходной массив: {nums}")
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [-100, -3, 0, 100]
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}\n")

if __name__ == "__main__":
    test()