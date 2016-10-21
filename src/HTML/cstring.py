#!/usr/bin/env python
from sys import argv

# Based on http://stackoverflow.com/questions/14945095/how-to-escape-string-for-generated-c
def enc(s):
   result = ''
   for c in s:
      if not (32 <= ord(c) < 127) or c in ('\\', '"'):
         result += '\\%03o' % ord(c)
      else:
         result += c
   return '"' + result + '"'

if __name__ == "__main__":
    print("char *html = \\")
    for line in map(enc, open(argv[1])):
        print("  " + line + " \\")
    print(";")