
def combination(s, final_list=[], start_position=0):
    initial_list = list(s)
    new_position = len(final_list)
    if len(initial_list) > 0 and len(final_list) > 0 and start_position == len(final_list):
        return final_list

    if final_list == []:
        final_list = list(initial_list)
        return combination(initial_list, final_list, 0)

    for i in range(start_position, new_position):
        for letter in initial_list:
            if letter not in final_list[i]:
                final_list.append(final_list[i] + letter)

    return combination(initial_list, final_list, new_position)


print(combination('abc'))

class Solution():
    def combinations(self, n, list, combos=[]):
        # initialize combos during the first pass through
        if combos is None:
            combos = []

        if len(list) == n:
            # when list has been dwindeled down to size n
            # check to see if the combo has already been found
            # if not, add it to our list
            if combos.count(list) == 0:
                combos.append(list)
                combos.sort()
            return combos
        else:
            # for each item in our list, make a recursive
            # call to find all possible combos of it and
            # the remaining items
            for i in range(len(list)):
                refined_list = list[:i] + list[i+1:]
                combos = self.combinations(n, refined_list, combos)
            return combos


print(Solution().combinations(2, "abc"))


