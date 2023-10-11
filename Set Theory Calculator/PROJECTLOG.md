### 8/28
-trying to make some sense of this shit again lol


# so these are the AIS's I need to generate in order to make the trichords
-setfromAIS([1, 1, 10])  
-setfromAIS([1, 2, 9])  
-setfromAIS([1, 3, 8])  
-setfromAIS([1, 4, 7])  
-setfromAIS([1, 5, 6])  
-setfromAIS([2, 2, 8])  
-setfromAIS([2, 3, 7])  
-setfromAIS([2, 4, 6])  
-setfromAIS([2, 5, 5])  
-setfromAIS([3, 3, 6])  
-setfromAIS([3, 4, 5])  
-setfromAIS([4, 4, 4])  
-1 1 10 
-1 2 9  
-1 3 8  
-1 4 7  
-1 5 6   
-2 2 8  
-2 3 7  
-2 4 6  
-2 5 5  
-3 3 6  
-3 4 5  
-4 4 4  

### 9/5
Working out tetrachord AIS's, there are some that are excluded from the function I came up with- the ones that are excluded happened before in the series, but are read backwards
  -1119
  -1128
  -1137
  -...
  -1425
  -e.g. after 1515 you're expecting 1524
  -but it moves onto 2127
  This is because the prime form system is not entirely systematic- there are some decisions here that are human made. And what it looks like is that something like 1524 doesn't get expressed because 1425 is already there. How are they related? 1524 is 1425 read backwards but starting from position 0. Every time there's an AIS you're expecting from the pattern that's not included, it can be found previously in the list of AIS's as a previous member read backwards from position 0. This means as I'm generating prime forms from AIS's and appending them to a list, I'll also need to be creating a list that takes the AIS and rotates/reverses it.

  # need to make a function that takes a list/array and converts to the string representation for prime form
  -def primeformformat(mylist):
      return f"({''.join(str(x) for x in mylist)})"
  # So what I'm looking to put in main(): is a dictionary generator with this format
  -trichorddictmake(aislist):  
  --trichorddictlist = {}  
  --for ais in aislist:
  ---primeform = setfromais(ais)
  ---trichorddict.update({primeformformat(primeform): generatetrichordsets(primeform)})
  ---return trichorddict

eliminate duplicates in AIS series (1524/1425)- DONE!
eliminate duplicates from symmetrical primeforms in list of all sets for a trichord (048) (048) (048)
i'm trying to write "if trichord in trichords" but there's something going on with arrays and dimensions that I don't yet have right. I feel like I'm close though!

9/6:
stole some "if trichord in trichords" stuff from SO that didn't really work
what I found out thinking it through is that these repeats aren't terribly common. They happen in unique cases where the prime form symmetrically divides the octave. That means that out of the ~140 prime forms that I hope to outline in the dictionaries that make up the calculator:
https://www.donaldregnier.com/2016/08/23/the-symmetric-scales/#:~:text=There%20are%205%20ways%20of,which%20relative%20definition%20is%20111111111111. shouts out
These sets will have repeats when you transpose them to all twelve values to store in the values of the big dictionary.
(048) for trichords (augmented triad)
(0167) (Bartok z-cell)
(0268) 
(0369) for tetrachords (diminished 7 chord)
(014589) (two augmented triads a half step apart) (symmetrical augmented scale)
(012678)
(013679)
(02468T) for hexachords (whole-tone scale)
(01236789)
(0124678T)
(0134679T) for octachords (octatonic scale) (prime form accounts for all forms of the octatonic scale as prime form is not pitches, but characterizing their interval pattern)
(01245689T) for 9-note chords (Messiaen M3)
(012346789T) for 10-note chords
(0123456789TE) for 12-note chords (chromatic scale)

These ones need allowances for the symmetry. But where does this go in the flow?

(048) yields [0, 4, 8] then 4, 8, 0
0167 transposed up a tritone is 6710
0268 transposed up a tritone is 6802
0369 + 3 3690
014589 + 4 458901
012678 + 6 012678
013679 + 6 679013
02468T + 2 2468T0
01236789 + 6 67890123
0124678T + 6 678T0124
0134679T + 6
01245689T + 4
012346789T + 6

How do I account for these symmetrical ones in my code? comparing arrays appropriately is kicking my ASS.

## 9/7 WOOHOO!
-np.unique is the answer along with converting the lists of values into one big array to use what np has. Create the values list and add the duplicates as they come, no big deal. Then right before you return the set list, just convert with unique!
ok wow, so this is a lot of the work done. If I can figure out how to generate the aislists, then I'm good to go. I can generate them all individually, but I want to see if I can make a big AISgenerator function that does the work. Need to split this stuff apart and try it somewhere else.

Need to expand rotatereverse function so that it spits out ALL rotations, not just the ones that start with the first index number

## 9/20
got a rough working version of the makeAIShexachords function. gnarly because it has the most unique ones. Worked out the basic idea of using the loops to make a big hunk of numbers beyond AIS's I want and then carve away. There are special rejects and special inclusions and then a final special case for when the final ais is added
## 9/21
cracked hexachords and nonachords today!
## 9/22
cracked pentachords!