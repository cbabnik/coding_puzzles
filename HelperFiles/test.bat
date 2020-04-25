@echo off

echo Testing a%1.py
echo --------------
python a%1.py < test/a%1.in > test/a%1.out 2> test/a%1.err
diff test/a%1.out test/a%1.exp