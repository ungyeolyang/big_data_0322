import numpy as np

data =[1,2,3,4] #리스트 생성, 리스트는 데이터형에 제한이 없음

a1 = np.array(data)
print(a1)
print(data)

data2 = [1,1.2,0.5,2]
a2 = np.array(data2) #배열은 데이터형에 제한이 있음으로 자동 형변환이 일어남
print(a2)

x = np.array([0.1, 0.2, 0.3, 4])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 배열 요소의 데이터 타입을 반환 합니다.

a3 = np.arange(0,10) #0 <= x <10
print(f'a3 {a3}')

a4 = np.arange(12).reshape(4,3)
print (f'a4 {a4}')

a5 = np.linspace(0, np.pi, 20) # 0부터 pi 까지 20등분
print(f'a5 {a5}')

a6 = np.zeros((3, 4))
print(f'a6 {a6}')

a7 = np.ones(5)
print(f'a7 {a7}')

a8 = np.eye(4)
print(f'a8 {a8}')

a9 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(f'a9 {a9}')
print(a9.dtype)
num_a9 = a9.astype(float)
print(num_a9)

a10 = np.random.rand(2, 3, 4)
print(f'a10 {a10}')

a11 = np.random.randint(10,size=(2,3))
print(f'a11 {a11}')

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# 요소별 덧셈
result = arr1 + arr2
print(f'덧셈 {result}')

# 요소별 곱셈
result = arr1 * arr2
print(f'곱셈 {result}')

# 요소별 거듭제곱
result = arr1 ** 2
print(f'거듭제곱 {result}')

# 요소별 비교 연산 : true, flase 반환
arr3 = np.array([10, 20, 30, 40])
print(f'4보다큰 {arr2>4}')

arr4 = np.array([1, 2, 1, 5, 4])
print(f"합계 : {arr4.sum()}, 평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}, 분산 : {arr4.var()}")
print(f"최솟값 : {arr4.min()}, 최댓값 : {arr4.max()}")
#인덱싱
print(arr4[0])
print(arr4[2])

# 슬라이싱
print(arr4[1:4])

# 2*3 크기의 2차원 배열 생성
matrix1 = np.array([[1,2], [4,5]])

matrix2 = np.array([[5,6], [7,8]])

# 행렬 덧셈
result = np.add(matrix1, matrix2)
print(f'행렬 덧셈 {result}')

# 행렬 뺄셈
result = np.subtract(matrix1, matrix2)
print(f'행렬 뺄셈 {result}')

#행렬 곱셈
result = np.dot(matrix1, matrix2)
print(f'행렬 곱샘 {result}')

#전치 행렬 : 행과 열을 교환하여 얻는 행렬이다.
matrix = np.array([[1,2,3], [4,5,6]])
result = np.transpose(matrix)
print(f'전치 행렬 {result}')

# 역행렬 : 정방행렬 A에 대해 A와 곱했을 때 항등행렬이 되는 행렬 입니다.
matrix3 = np.array([[1,2],[3,4]])
inverse_matrix = np.linalg.inv(matrix3)
print(f'역행렬 {inverse_matrix}')

# 크기가 다른 배열 생성
a = np.array([1, 2, 3]) # 1차원 배열
b = np.array([[4], [5], [6]]) # 2차원 배열 (3 X 1)

# 브로드캐스팅을 사용한 배열 연산
c = a + b

print(f'브로드캐스팅 a+b {c}')
