# sliding window technique is a method used to solve problems 
# that involve subarray or substring or window

# sliding window can be fixed & dynamic size


# Given an array and an integer k, we need to calculate the maximum sum
#  of a subarray having size exactly k.
# Consider an array arr[] = {5, 2, -1, 0, 3} and value of k = 3 and n = 5

def slidingWindow(arr, size):
    length = len(arr)

    max_sum  = window_sum = sum(arr[:size])

    for i in range(length - size):
        # window_sum = arr[i] + arr[i+size]
        window_sum = window_sum - arr[i] + arr[i + size]
        max_sum = max(window_sum, max_sum)
    
    print(f""" Array : {arr}, Size: {size}, Max Sum:{max_sum}""")
    return max_sum

#Longest Substring Without Repeating Characters
# Given a string s having lowercase characters, 
# find the length of the longest substring without repeating characters. 

def dynamicSlidingWindow(string):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    print(f""" {string} , {max_len} """)
    return max_len


if __name__ == '__main__':
    slidingWindow([5, 2, -1, 0, 3], 3)
    slidingWindow([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)
    
    dynamicSlidingWindow("abcabcbb")