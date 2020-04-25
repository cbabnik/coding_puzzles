@echo off

echo Testing a%1.py
echo --------------

python interactive_runner.py python testing_tool.py 0 -- python a%1.py 2> test/a%1.err
python interactive_runner.py python testing_tool.py 1 -- python a%1.py 2> test/a%1.err
python interactive_runner.py python testing_tool.py 2 -- python a%1.py 2> test/a%1.err