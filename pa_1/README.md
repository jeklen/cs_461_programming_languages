## algorithm:topological sort(not-so-cleverly disguised)

```
L <-- Empty list that will contain the sorted elements
S <-- Set of all nodes with no incoming edge 
while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error(graph has at lest one cycle
else return L(a topologically sorted order)
```

## implement in severn languages
- how to store the (implicit) tree
- can't use any special libraries(aside from the OCaml unix and str libraries, which are not necessary for this assignment)
- test example

```
cool rosetta.cl < testcase.list > testcase.out
gcc -o rosetta rosetta.c && ./rosetta < testcase.list > testcase.out
ghc --make -o rosetta *.hs ; ./rosetta < testcase.list > testcase.out
node rosetta.js < testcase.list > testcase.out
ocaml unix.cma str.cma rosetta.ml < testcase.list > testcase.out
python rosetta.py < testcase.list > testcase.out
ruby rosetta.rb < testcase.list > testcase.out

# In each case we will then compare your output to the correct answer:
diff -b -B -E -w testcase.out correct.answer
```
