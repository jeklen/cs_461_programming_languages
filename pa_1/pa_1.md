Programming Assignment 1 - The Rosetta Stone

Instructions

The Rosetta Stone aided linguistic understanding by providing the same text in three different languages. In this project you will implement the same simple program in seven separate languages. Each of your seven implementations will have exactly the same interface, will otherwise adhere to the same specification, and should behave exactly the same way.
The seven possible languages are Ruby, OCaml, Haskell, JavaScript, Python, C and Cool (you will write in all seven of them). You will use Ruby, Haskell, JavaScript, OCaml and Python for PA2 through PA5 (and you must use at least four different languages for PA2-PA5), In PA2 through PA5 you will write an interpreter for Cool, so it is important that you understand how Cool works now. The C (not C++) implementation is so that you can gain a better appreciation for time-saving features of higher-level languages (e.g., automatic memory management, first-class higher-order functions, object-oriented programming), as well as multi-language projects and linking (covered later in the course).

You can find tutorials, manuals and other resources for these languages on the main project webpage.

For this assignment, you must work alone. Subsequent assignments will allow you to work in pairs.

The Specification

Your program must take in a list of dependent tasks and either output a valid order in which to perform them or the single word cycle.
Your program will accept a number of lines of textual input (via standard input). There are no command-line arguments — you must always read from standard input. Do not open a named file. Instead, always read from standard input.

That text input will contain a non-zero but even number of lines. Every two lines represent a pair of tasks. The first line gives the name of a task, the second line gives the name of a task that it depends on. This text input is also called the task list.

The task list will contain only standard ASCII characters (no UTF/8 Unicode or special accents). The goal is to test programming and program language concepts, not your internationalization abilities.

Each task name starts at the beginning of the line and extends all the way up to (but not including) the end of that line. So the newline or carriage return characters \r or \n are not part of the task name. Each task name is at most 60 characters long. (This limit is to make the C implementation easier; if you can support longer strings natively, feel free to do so.)

Example task list:

learn C
read the C tutorial
do PA1
learn C
The interpretation is that in order to learn C one must first read the C tutorial and that in order to do PA1 one must first learn C. Desired output for this example:
read the C tutorial
learn C
do PA1
If the task list containts a cycle of any size, your program should output exactly and only the word cycle. Example cyclic input:
get a job
have experience
have experience
work on a job
work on a job
get a job
Even if the task list contains a few non-cyclic parts, any single cycle forces you to output only the word cycle.
Always output to standard output only. Do not write anything to stderr.

There is no fixed limit on the number of lines in the task list (although it is not zero and it is even).

Two tasks with the same name are really just the same task. Use standard string equality.

Duplicated pairs of tasks are not allowed. For example:

learn C
read the C tutorial
do PA1
learn C
learn C
read the C tutorial
... that task list is not valid input because the pair learn C/read the C tutorial appears twice. Program behavior if the task list contains a duplicate pair is undefined. You will not be tested on it.
Your program may not cause any other file I/O to be performed, such as creating a temporary file to keep track of some intermediate sorting results or writing to stderr (or even causing the interpreter to write a warning to stderr). You do not need any such temporary files or stderr-printing to solve this problem.

Choosing Among Unconstrained Tasks

If there are multiple outstanding unconstrained tasks, your program should output them in ascending ASCII alphabetical order. That is, if you ever have two or more tasks, each of which has no remaining dependencies, output the one that comes first ASCII-alphabetically. (This constraint makes your program deterministic; for any given input there is only one correct output.) Example:
learn C
understand C pointers
learn C
read the C tutorial
do PA1
learn C
Because r comes before u, your output should be:
read the C tutorial
understand C pointers 
learn C
do PA1
To put it another way, consider this task list:
B
A
C
D
C
E
Which yields a dependency graph like this:
A  D E
|  \ /
B   C
The proper ordering for this set of tasks is A B D E C. Note that B comes before D and E, even though B depends on A. This is because, once A is finished, B is free to go and it comes first alphabetically. You may want to consider this requirement when you pick your sorting algorithm. Given this requirement the answer A D E B C is incorrect and will receive no credit.
Commentary

This problem is just topological sort not-so-cleverly disguised. Feel free to look up how to do toposort on the internet (but remember that you must turn in your own work; you may not copy someone else's code and claim it as your own).
Take a look at the files in pa1-hint.zip. You could do worse than using them as starting points.

If you're having trouble writing anything reasonable in Cool, don't forget to look at the example Cool programs that are distributed near the compiler.

Building and maintaining an explicit graph structure is probably overkill.

Since you do not know the number of tasks in advance you will need some sort of dynamic memory allocation.

I recommend solving the problem in the Python, Ruby or OCaml first (depending on where you are most comfortable) and then just translating your solution into the others. Translating into Cool, Haskell, JavaScript and C will not be as easy, however.

Use this as an opportunity to see what you like about various languages. What do you think of Python's enforced tabbing? How about ML's abysmal error reporting? Ruby's below-par execution speed? Haskell's IO Monad? JavaScript's more asynchronous I/O model? C's general hideousness?

For bonus brownie points, try to make your OCaml, Haskell, JavaScript, Ruby and Python implementations as functional as possible (e.g., eschew side effects).

Don't know which languages to pick for the PA1c checkpoint? Look at the pa1-hint.zip file and pick languages that look like they would be easy to debug. Your first attempt (for PA1c) will probably contain the most algorithmic errors. After that it's more of a matter of translating it into other languages.

What To Turn In For PA1c

PA1c is a checkpoint to make sure that you do not fall behind on PA1. You have about two weeks to complete all of PA1, but if you try to do it all at the last minute you're probably doomed to failure.
For the one-week PA1c checkpoint, you must have at least four of the implementations done. This separates the project into two phases: (0) Can I write this program at all? and (1) Can I write this program in all of the other languages?

For PA1c you must turn in a zip file containing four source files. Use the following names:

rosetta.c -- C implementation
rosetta.cl -- Cool implementation
rosetta.hs -- Haskell implementation
rosetta.js -- JavaScript implementation
rosetta.ml -- OCaml implementation
rosetta.py -- Python implementation 
and/or
rosetta.rb -- Ruby implementation
Each of your source files should have one of those names (e.g., rosetta.whatever). Submit a single zipfile containing exactly those three files.
What To Turn In For PA1

You must turn in a zip file containing exactly these seven files:
rosetta.c -- C implementation
rosetta.cl -- Cool implementation
rosetta.hs -- Haskell implementation
rosetta.js -- JavaScript implementation
rosetta.ml -- OCaml implementation
rosetta.py -- Python implementation
rosetta.rb -- Ruby implementation
Plus these two files:
testcase.list -- A valid task list that you made up.
readme.txt -- your README file
You may name your ZIP file anything you like — when you submit it, it will be renamed on our servers to your_UVA_id.zip.
The testcase.list file should contain a valid task list (it may or may not contain a cycle -- your choice). It may be used as one of the test cases to grade all of the submissions, so you have the chance to be certain of getting at least one right.

The readme.txt file should be a plain ASCII text file (not a Word file, not an RTF file, not an HTML file) describing your design decisions. Which language did you start with? How did you store the (implicit) graph? Which language was the hardest? One or two English paragraphs should suffice. Spelling, grammar, capitalization and punctuation count.

Autograding

We will use scripts to run your program on various testcases. The testcases will come from the testcase.list files you and your classsmates submit as well as held-out testcases used only for grading. Your programs cannot use any special libraries (aside from the OCaml unix and str libraries, which are not necessary for this assignment). We will use (loosely) the following commands to execute them:
cool rosetta.cl < testcase.list > testcase.out
gcc -o rosetta rosetta.c && ./rosetta < testcase.list > testcase.out
ghc --make -o rosetta *.hs ; ./rosetta < testcase.list > testcase.out
node rosetta.js < testcase.list > testcase.out
ocaml unix.cma str.cma rosetta.ml < testcase.list > testcase.out
python rosetta.py < testcase.list > testcase.out
ruby rosetta.rb < testcase.list > testcase.out
In each case we will then compare your output to the correct answer:
diff -b -B -E -w testcase.out correct.answer
If your answer is not the same as the reference answer you get 0 points for that testcase. Otherwise you get 1 point for that testcase.
We will perform the autograding on some unspecified test system. It is likely to be Solaris/UltraSPARC, Cygwin/x86 or Linux/x86. However, your submissions must officially be platform-independent (not that hard with a scripting language). You cannot depend on running on any particular platform.

There is more to your grade than autograder results. See the Programming Assignment page for a point breakdown.

Your submission may not create any temporary files. Your submission may not read or write any files beyond its input and output. We may test your submission in a special "jail" or "sandbox".

Notes

There was going to be an option to use lolcode as a final language, but none of the available lolcode interpreters or compilers are both stable enough to be used in a classroom setting and also sufficiently-featured to handle this assignment. Oh noes!
Similarly, a strong argument could be made for The Shakespeare Programming Language, but it is not clear that it supports lexical analyzer generators or parser generators.
