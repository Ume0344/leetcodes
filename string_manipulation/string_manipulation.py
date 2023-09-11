class StringManipulation:
    def reverse_string(self, string: str) -> str:
        """
        Reverses a string.
        param string: String to be reversed.
        retrun reversed string.

        It is solved using slice concept. first colon represent start of string, middle one end of string and last one is the step size.
        Slices :
        arr = [1,2,3,4,5,6,7,8,9,10]
        if len(arr) = 10
        [2:10:2] = array[3,5,7,9]
        if arr = [0,1,2,3,4,5,6,7,8,9,10]
        [2:11:2] = [2,4,6,8]
        """

        return string[::-1]
