
menu='스테이크 pizza 파스타 콜라'
'''
문제)
1)문자열의 문자 갯수는?
2)맨 마지막 문자를 출력하시오.
3)영어와 한글을 구별하여 출력하시오.
'''
import re
print('문제 1')
print(len(menu))
print('문제 2')
print(menu[len(menu)-1])
print('문제 3')
print('영어 출력하세요')
for k in menu:
    if k>='a' and 'z'>=k or k>='A' and k<='Z':
        print(k, end=' ')
print('    ')
print('한글을  출력하세요')
for k in menu:
    if k>='가' and '힣':
        print(k, end=' ')
print('끝')

