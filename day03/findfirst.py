class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while( i < len(haystack) and j < len(needle) ) :
            if( haystack[i] == needle[j] ) :
                i+=1
                j+=1
            else :
                i = i - j + 1
                j = 0
        if ( j == len(needle) ) : 
            return i-j
        else :
            return -1
        
        
        
s = Solution()

print(s.strStr("sadbutsad", "sad"))    
