# -*- encoding: utf-8 -*-
from coderunner import test, Perl, LangC, Python, Ruby, Cpp, main


test(Ruby, "module_inheritance.rb", """
hello
hello
""", is_file=True)

test(Ruby, "mixin.rb", """
bar!
""", is_file=True)

test(Perl, "reenter.pl", """
0
""", is_file=True)

test(Python, "oldclass.py", """
base
D2
base
""", is_file=True)

test(Python, "pack.py", """
スズメ: 1匹
スズメ: 2匹
カラス: 1匹
スズメ: 3匹
""", is_file=True)

test(Cpp, "iter.cpp", """
loop with pointer
1
2
3
loop with iterator
1
2
3
""", is_file=True)

main()
