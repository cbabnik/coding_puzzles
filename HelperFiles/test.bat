@echo off

echo Testing a%1.py
echo --------------
py a%1.py < test/a%1.in > test/a%1.out
diff test/a%1.out test/a%1.exp