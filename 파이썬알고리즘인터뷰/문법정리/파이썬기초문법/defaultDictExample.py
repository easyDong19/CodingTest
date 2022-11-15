from collections import defaultdict
#그냥 dictionary는 키값이 없을 경우 keyError를 발생
#defaultdict은 키값이 없을 경우 초기값을 지정할 수 있다

int_dict = defaultdict(int)
normal_dict = {}

print(int_dict['key1']) #0
# print(normal_dict['key1']) #error

#그냥 dict을 사용하면 get함수나 in 구문을 사용해서 key가 존재하는지 확인하고 존재하지 ㅇ낳는다면 키를 넣는 과정을 거쳐야함
if not 'key1' in normal_dict:
    normal_dict['key1'] = 0

print(normal_dict['key1'])


