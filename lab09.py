# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.


    # loop through each number and add each number with it, if it adds up return the indices
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


def max_profit(prices):
    # Outline:
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    max_profit = 0
    minimum_price = prices[0]

    # check if profit bigger than current max profit
    # check if minimum price is smaller today

    for price in prices:
        if price - minimum_price > max_profit:
            max_profit = price - minimum_price

        if price < minimum_price:
            minimum_price = price

    return max_profit


def max_subarray(nums):
    # Outline:
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.

    # initialize current sum and max to the first index
    # loop through the list starting at second index
    # add that number to the sum, if the sum is less than the next index, 
    # just change the current sum to that number.
    # otherwise, keep adding. keep going until list is done.
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum += num

        if current_sum < num:
            current_sum = num

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([2, 7, 11, 15], 9))   # returns [0, 1]   (2 + 7)
    print(two_sum([3, 2, 4], 6))        # returns [1, 2]   (2 + 4)
    print(max_profit([7, 1, 5, 3, 6, 4]))   # returns 5   (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))      # returns 0   (prices only fall)
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]))                  # returns 23  (the whole list)


if __name__ == "__main__":
    main()

