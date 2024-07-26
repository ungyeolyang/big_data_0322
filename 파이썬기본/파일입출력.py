# score_file = open("./score.txt", "w", encoding="utf-8")
# #./ 현재위치 ../ 상위 위치 encoding="utf-8" 한글 안꺠지도록
# print("수학 : 55", file=score_file)
# print("영어 : 60", file=score_file)
# score_file.write("과학 : 90\n")
# score_file.write("국어 : 100\n")
# score_file.close() # open하면 close 해야 한다.
# score_file = open("score.txt","r",encoding="utf-8")
# #read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환, 너무큰 파일은 읽는데 문제가 생길수 있다.
# print(score_file.read())
# score_file.close()
# # readline() : 한 라인 씩 읽어 문자열로 반환, 파일의 끝에 도달하면 None값이 반환. 다른 언어는 주로-1, 인덱스 개념으로 봤을때
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line,end="")
# score_file.close()
# # readlines() : 해당 파일의 모든 라인을 순서대로 읽어 들여 리스트 반환
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()
# with 구문을 사용하면 구문이 종료 될 때 자동으로 파일을 닫음, 언어가 길어지면 close를 까먹을 수도 있기에
with open("score.txt", "r", encoding="utf-8") as score_file:
    lines = score_file.readlines()
    for line in lines:
        print(line, end="")

