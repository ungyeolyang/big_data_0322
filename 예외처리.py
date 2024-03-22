# 1. 문법오류 수정, 논리적인 문제가 없도록 코딩, 항상 예외사항을 대비하는 코드 작성
# 2. 해결가능 예외 사항이 있고, 해결 불가능한 예외 사항이 있음
try:
    print("나눗셈 계산기 입니다.")
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두번째 숫자 입력 : "))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("에러! 잘못된 값을 입력 하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print("정상 처리 되었습니다.")

finally:
    print("프로그램 실행 완료!")