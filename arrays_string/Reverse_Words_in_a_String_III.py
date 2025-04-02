'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        last_space_index = -1  # Initialize the last space index
        ch_array = list(s)  # Convert the string into a list of characters
        length = len(s)  # Get the length of the string

        for str_index in range(length + 1):
            if str_index == length or ch_array[str_index] == ' ':
                start_index = last_space_index + 1
                end_index = str_index - 1

                # Reverse the word in place
                while start_index < end_index:
                    ch_array[start_index], ch_array[end_index] = ch_array[end_index], ch_array[start_index]
                    start_index += 1
                    end_index -= 1
                
                last_space_index = str_index  # Update the last space index

        # Return the modified array as a string
        return ''.join(ch_array)

# Example usage
solution = Solution()
s = "hello world"
result = solution.reverseWords(s)
print(result)  # Output: "olleh dlrow"
