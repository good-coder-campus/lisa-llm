# 뛰어쓰기 단위로 분리
input_text = "나는 최근 상해 여행을 다녀왔다."
input_text_list = input_text.split()
print("input_text_list: ", input_text_list)

# 토큰 -> 아이디 딕셔너리와 아이디 -> 토큰 딕셔너리 만들기
str2dix = {word: idx for idx, word in enumerate(input_text_list)}
idx2str = {idx: word for idx, word in enumerate(input_text_list)}
print("str2dix: ", str2dix)
print("idx2str: ", idx2str)

# 토큰을 아이디로 변환
input_ids = [str2dix[word] for word in input_text_list]
print("input_ids: ", input_ids)
