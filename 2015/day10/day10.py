import re


re_d = re.compile(r'((\d)\2*)')


def replace(match_obj):
    s = match_obj.group(1)
    print('> ' + s)
    return str(len(s)) + s[0]


s = '1'
for i in range(5):
    print(s)
    s = re_d.sub(replace, s)
    print(s)
    print('###########')
print len(s)
