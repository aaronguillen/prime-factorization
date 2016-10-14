# prime-factorization
I think, at least, a pretty clever prime factorization algorithm.

I was working on a program for Diffie-Hellman and I needed to find the primitive root for a given value. Finding the primitive root of a value involves knowing that value's prime factors. My solution was ineligant, to say the least, but functional. It was later that I thought of this algorithm and decided to test its speed.

I thought of the algorithm independently, though I'm sure it already exists. Either way, I felt pretty good when I thought of it and decided to code it. Of course, I used Python. I plan to implement it in Ruby, as well.

I originally started writing it in Python v3.5.2 but I finished it in Python v2.7.6. It works as-is for both versions of Python (I'm assuming it works with other versions as well, though I have not tested it).

Pretty simple to use I think. Command line, navigate to the directory where you have the script. run

$ python primeFactorization.py [value] [value]

or

$ python primeFactorization.py [value]

where value is an integer or hexadecimal number in the form 0xhexNum (e.g., 0xDEADBEEF)

If you give it one number, it will give you prime factors of that number. If you give it two numbers, it will give you the prime factors of all number in the range between the two numbers. So inputting

$ python primeFactorization.py 1 10

will give you the prime factorization for one through nine.

The output is of the following form (for each factored value):

integerRepresentation : hexadecimalRepresentation : [prime factors] : time elapsed during computation

---------------

So the files included in this repository. This readme.md, obviously, and the license file (GPL, feel free to change use, whatever).

I also have an output_analysis.txt where I basically just talk more, but, if you're into this stuff you may find it mildly interesting.

The script, of course, primeFactorization.py.

Now, I tend to get a little comment-heavy in my code. I know commenting is good practice, I know too much of a good thing is not a good thing, and I know I tend to go a little overboard. So I also included primeFactorization_clean.py which is the same script without comments. I know sometimes it's nice to just look at the code.
