#참고 자료 https://wikidocs.net/4308
import re
p = re.compile('a')
#match(): 문자열의 처음부터 정규식과 매치되는지 조사한다
m1 = p.match("ab") #match 객체 생성
m2 = p.match("ba") #none
#match는 결괏값이 있을 때만 다음 작업을 수행함

#search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사한다
m = p.search("aabbb") #객체 생성
m = p.search("bba") #객체 생성
#문자열의 시작과 상관없이 전부 찾아서 결과로 반환

#findall(): 정규식과 매치되는 모든 문자열을 리스트로 돌려준다
p = re.compile('[a-z]+')
result = p.findall("life is too short")
print(result) #[life, is, too, short] 리스트로 반환

#finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다
result = p.finditer("life is too short")
for r in result: print(r)

#match 객체의 메서드
m = p.match("python")
m.group() #매치된 문자열을 돌려준다
m.start() #매치된 문자열의 시작 위치를 돌려준다
m.end #매치된 문자열의 끝 위치를 돌려준다
m.span() #매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다

#컴파일 옵션

#DOTALL, s : .이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
p = re.compile('a.b')
m = p.match('a\nb') #None
p = re.compile('a.b',re.S)
m = p.match('a\nb')

#IGNORECASE, I : 대소문자에 관계없이 매치할 수 있도록 한다
p = re.compile('[a-z]+', re.I)
p.match('Python')

#MULTILINE, M : 여러줄과 매치할 수 있도록 한다 (^,$ 메타문자 관련 옵션)
re.compile("^python\s\w+") #python으로 시작 + 빈칸 + 단어

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) #['python one']

re.compile("^python\s\w+",re.M) #python으로 시작 + 빈칸 + 단어
print(p.findall(data)) #['python one', 'python two', 'python three']

#VERBOSE, X : 정규식을 보기 편하게 만들 수 있고 주석 사용 가능
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
#정규식이 RawSting인지 알려주는 방법
p = re.compile(r'\\section')
data = r"\section \abcdef"
print(p.findall(data))


###확장###

#그룹핑
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1)) #park
#group(0) 전체 그룹

#그루핑된 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group() #the the
#\1은 정규식의 그룹 중 첫 번째 그룹을 가리킴

#그루핑 이름 붙히기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)") #(?P<그룹명>)

#전방탐색
p = re.compile(".+(?=:)") # 긍정형 전방 탐색(?=...)
m= p.search("http://google.com")
print(m.group()) #http

p = re.compile(".*[.](?!bat$).*$") #부정형 전방탐색 (?!...) bat이 아닌 경우만 통

#문자열 바꾸기
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
p.sub('colour', 'blue socks and red shoes', count = 1) #바뀌는 갯수를 정하고 싶은 경우

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

#매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')

