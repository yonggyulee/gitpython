# 문자열 데이터를 분석전

# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리(Capitalize
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_string(strings):
    results = []
    for string in strings:
        # 처리 01
        string = string.strip()
        # 처리 02
        string = re.sub('[?1#*&$@]', '', string)
        # 처리 03
        string = string.title()

        results.append(string)
    return results

states = clean_string(states)
print(states)


################################################################################################\

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_string(strings, *funcs):
   results = []
   for s in strings:
       for f in funcs:
           s = f(s)

       results.append(s)
   return results

states = clean_string(states, str.strip, lambda  x: re.sub('[?!#*&$@]', '', x))
print(states)