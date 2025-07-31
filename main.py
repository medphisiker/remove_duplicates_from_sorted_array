from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Функция удаляет дубликаты на месте так, чтобы каждый
        уникальный элемент встречался только один раз.
        Относительный порядок элементов остается прежним.

        Решение через два указателя паттерн read write, подвид two pointers.

        Временная сложность: O(n) — один проход по массиву.
        Пространственная сложность: O(1) — модификация выполняется на месте
        без использования дополнительной памяти.
        
        write указывает на последний уникальный элемент, поэтому write + 1
        даст количество уникальных элементов.

        Args:
            nums (List[int]): целочисленный массив `nums`, отсортированный
            в неубывающем порядке, из которого мы удаляем дублирующиеся элементы.

        Returns:
            int: возвращает количество уникальных элементов в `nums`.
        """
        # оптимизация тривиальных случаев
        if len(nums) <=1:
            return len(nums)
        
        write = 0
        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    solution = Solution()
    print(f"Входной массив: {nums}")
    k = solution.removeDuplicates(nums)
    print(f"Количество уникальных элементов: {k}")
    print(f"Массив без дубликатов: {nums[:k]}")
