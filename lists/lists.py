class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list) == 0:
            return []

        max_number = input_list[0]

        for number in input_list:
            if number > max_number:
                max_number = number

        return [max_number if num > 0 else num for num in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        left_index = 0
        right_index = len(input_list) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if input_list[mid_index] < query:
                left_index = mid_index + 1
            elif input_list[mid_index] > query:
                right_index = mid_index - 1
            else:
                return mid_index
        return -1
