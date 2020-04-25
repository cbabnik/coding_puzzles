if "%~1"=="" ( 
    goto error 
) else ( 
    goto program 
)

:error

echo "Need to include a directory, relative to coding_puzzles"
goto end

:program

pushd "%~dp0"

mkdir "../%~1"
cp template.py "../%~1/a1.py"
cp template.py "../%~1/a2.py"
cp template.py "../%~1/a3.py"
cp template.py "../%~1/a4.py"

cp ref.py "../%~1/"
cp algorithms.py "../%~1/"
cp test.bat "../%~1/"
cp interactive_runner.py "../%~1/"
cp test_interactive.bat "../%~1/"

mkdir "../%~1/test"
touch "../%~1/test/a1.in"
touch "../%~1/test/a1.exp"
touch "../%~1/test/a1.out"
touch "../%~1/test/a2.in"
touch "../%~1/test/a2.exp"
touch "../%~1/test/a2.out"
touch "../%~1/test/a3.in"
touch "../%~1/test/a3.exp"
touch "../%~1/test/a3.out"
touch "../%~1/test/a4.in"
touch "../%~1/test/a4.exp"
touch "../%~1/test/a4.out"

popd

:end