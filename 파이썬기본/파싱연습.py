from bs4 import BeautifulSoup

# html = '''
# <html>
#     <table border=1>
#         <tr>
#             <td> 항목 </td>
#             <td> 2013 </td>
#             <td> 2014 </td>
#             <td> 2015 </td>
#         </tr>
#         <tr>
#             <td> 매출액 </td>
#             <td> 100 </td>
#             <td> 200 </td>
#             <td> 300 </td>
#         </tr>
#     </table>
# </html>
# '''
# soup = BeautifulSoup(html, 'html.parser')
# result = soup.select('td')
# print(result)
#
# # 각 태그의 텍스트만 가져오기
# for val in result :
#     print(val.text)

# html = '''
# <ul>
#     <li> 100 </li>
#     <li> 200 </li>
# </ul>
# <ol>
#     <li> 300 </li>
#     <li> 400 </li>
# </ol>
# '''
# soup = BeautifulSoup(html, 'html5lib')
# result = soup.select('ul li')
# for r in result:
#     print(r.text)

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body id = "id">
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p id ="di1">This is a paragraph.</p>
      <p id ="di2">This is another paragraph.</p>
    </div>
    <a href="https://www.example.com">Link</a>
    <a href="https://www.example2.com">Link2</a>
  </body>
</html>
'''

# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')
id = soup.select('div > p')

attr = {"class":"content", "text": "another"}
el = soup.find_all(attrs=attr)
print(el)