9/5 To Do
eliminate duplicates in AIS series (1524/1425)- DONE!
eliminate duplicates from symmetrical primeforms in list of all sets for a trichord (048) (048) (048)
Try to generalize the AIS generator for set classes of any cardinality
^umm so about that....

9/21:
Need to work on 5, 7, and 8. you have 3, 4, 6, 9!
9/23:
Cracked 5, need to work on 7 and 8 (then 10 and 11 should be v quick)
get the angels out of the range. just append them at the beginning

10/10:
figure out what __pycache__ is and how to use it
figure out how to organize this thing:
    generate .json files of the angels and rejects (check if all the angels and rejects are right!)
    take what's in RUN, refine the makeAIS functions- 'if ais in angels/rejects'
    RUN becomes 'make dict'- (combine RUN and jsonmake into something makedict.py)
    Then your RUN will become your attempt to call something from the dict (look at the AOC RPS)
        testset = sorted(mylist)- design decision: ordered from interface at the start?    
            for key in calculatordict:
                if testset in values return the key.
