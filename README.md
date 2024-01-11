# magicSquares



# How to use


1. First download the code (in the terminal of your choice).

`
git clone https://github.com/Robotboy26/magicSquares.git
`

2. Next enter the directory with the main python file.

`
cd magicSquares/src
`

3. Now run the python file with the side length you want (it must be odd).

`
python3 main.py 3
`

4. Now enter the newly create directory "squares" and you should see a text file with the side lenth of your input squared. Print that file to the terminal.

`
cd squares
cat 9.txt
`

# compile into one executable file

1. Download pyinstaller.

`
pip install pyinstaller
`

2. In the src folder create the file.

`
pyinstaller main.py
`

3. Move the executable file out of its dir and into the project root

`
mv dist/main ../
`

4. You can now run the executable from the project root

`
cd ..
./main 3
`

# Examples

Input:

`
python3 main.py 3
`

Output:

```
8|1|6|
------
3|5|7|
------
4|9|2|
```

Input:

`
python3 main.py 5
`

Output:

```
17|24| 1| 8|15|
---------------
23| 5| 7|14|16|
---------------
 4| 6|13|20|22|
---------------
10|12|19|21| 3|
---------------
11|18|25| 2| 9|
```

Input:

`
python3 main.py 7
`

Output:

```
30|39|48| 1|10|19|28|
---------------------
38|47| 7| 9|18|27|29|
---------------------
46| 6| 8|17|26|35|37|
---------------------
 5|14|16|25|34|36|45|
---------------------
13|15|24|33|42|44| 4|
---------------------
21|23|32|41|43| 3|12|
---------------------
22|31|40|49| 2|11|20|
```
