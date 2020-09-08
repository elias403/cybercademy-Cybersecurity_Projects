import hashlib
import sys

try: 
    if sys.argv[1]== '-e':
        val = bytes(sys.argv[2],'utf-8')
        #x = hashlib.new('md5',val)
        x = hashlib.md5(val)
        print(x.hexdigest())
    elif sys.argv[1]== '-h':
        print('-e -> encode')

except IndexError:
    print('-e [string]')
    print('exemplo: python crypt.py -e admin123')
