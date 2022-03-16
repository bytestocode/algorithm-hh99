class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 빈 문자열인 경우 0
        if len(s) == 0:
            return 0
        # 문자인 경우 1
        elif len(s) == 1:
            return 1

        # 리스트 <<= list(문자열)
        # ex. ['a', 'b', 'c'] <<= 'abc'
        char_list = list(s)

        # set으로 바꿔서 최대 길이 범위 축소
        # ex. 'abcb'에서 중복없는 문자가 a, b, c 3개이므로 최대길이는 3이하로 판단
        max_length = len(set(char_list))

        # 주어진 길이로 쪼갠 이중 배열을 반환
        def create_sub_list(input_list, input_length):
            result = list()
            for i in range(len(input_list) - input_length + 1):
                result.append(input_list[i:i + input_length])
            return result

        # 중복된 문자가 있는지 판단
        # 중복 문자 있으면 True, 없으면 False
        def has_repeating_char(input_list):
            # 당초 리스트의 길이와 set 자료형으로 바꾼 길이를 비교
            if len(input_list) == len(set(input_list)):
                # 같으면 중복 없는것
                return False
            # 다르면 중복 있는 것
            return True

        while max_length > 1:
            # 리스트의 부분 리스트를 중첩 리스트를 반환
            # ex. char_list = ['a', 'b', 'c'] / max_length = 2
            #     return [['a', 'b'], ['b', 'c']]
            sub_list = create_sub_list(char_list, max_length)
            # 이중 배열을 하나씩 돌면서
            for li in sub_list:
                # 반복 문자가 없으면 최대 길이로 판단
                if not has_repeating_char(li):
                    return max_length
                # 있으면 계속 진행
                else:
                    continue
            # 부분리스트의 길이를 1 줄임
            max_length -= 1
