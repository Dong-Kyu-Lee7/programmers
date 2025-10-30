def solution(s):
    # 결과 문자열을 저장할 변수
    result = ""
    # 이전 문자가 공백이었는지 추적하는 플래그.
    # 문자열의 시작은 '가상의 공백 다음'으로 간주합니다.
    is_new_word = True 

    # 문자열을 한 글자씩 순회
    for char in s:
        if char == ' ':
            # 1. 공백일 경우: 공백을 추가하고, is_new_word를 True로 설정
            result += char
            is_new_word = True
        elif is_new_word:
            # 2. 새로운 단어의 첫 글자일 경우:
            #    첫 글자는 무조건 대문자로 변환 (숫자, 알파벳 모두 해당)
            result += char.upper()
            is_new_word = False # 다음 글자는 첫 글자가 아님
        else:
            # 3. 단어의 두 번째 이후 글자일 경우:
            #    무조건 소문자로 변환
            result += char.lower()
    return result