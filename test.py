from main import Solution

def test():
    # Example 1
    solution = Solution()
    nums = [1,1,2]
    k = solution.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1,2]
    
    # Example 2
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = solution.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0,1,2,3,4]
    
    # Test 1 без дублей
    solution = Solution()
    nums = [0,1,2,3]
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [0,1,2,3]
    
    # Test 2 1 элемент
    solution = Solution()
    nums = [0]
    k = solution.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [0]
    
    # Test 3 отрицательные элементы
    solution = Solution()
    nums = [-3,-3, 0, 2, 2, 3]
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [-3, 0, 2, 3]
    
    # Test 4 все элементы одинаковые
    solution = Solution()
    nums = [2,2,2,2,2,2,2,2]
    k = solution.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [2]
    
    # Test 5 крайние значения
    solution = Solution()
    nums = [-100, -100, -3, 0, 0, 0, 100, 100]
    k = solution.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [-100, -3, 0, 100]

if __name__ == "__main__":
    test()