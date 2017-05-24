
def lengthOfLongestSubstring(s):

  visited = []
  position = 0
  max = ''
  current = ''

  if s == '':
      return 0
  while position < len(s):
      for i in range(position,len(s)):
          if s[i] not in visited:
              visited.append(s[i])
              current = current + s[i]
              if len(current) > len(max):
                  max = current

          else:
              current = ''
              break



      visited = []
      current = ''
      position += 1


  return len(max)




print lengthOfLongestSubstring("pwwkew")

