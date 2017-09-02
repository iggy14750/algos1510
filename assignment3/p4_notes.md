Problem 4 -- ISAAC VERIFY THIS IS CORRECT AND ALSO THAT THIS COUNTS AS AN "EXCHANGE" ARGUMENT AS REQUESTED IN THE INSTRUCTIONS


A) THEOREM: The fill-as-you-go (FAYG?) algorithm correctly solves the problem.
   PROOF:   Assume, tgac, that algorithm FAYG is incorrect; that is, suppose that there exists some input I for 
            which FAYG produces a nonoptimal result. Call this output F(I).
            Let Opt(I) be the output of an optimal algorithm that solves this problem which is most similar to
            F(I); that is, from the beginning it agrees with F(I) for the most number of steps.
            
            - Consider the first point of disagreement between Opt(I) and F(I). This would be a stop x_i where the
               two algorithms take different amounts of time filling up. Since FAYG always gets just enough fuel to
               make it to the next station, and Opt(x<sub>i</sub>) \!= F(x<sub>i</sub>), we know that Opt must take *more* time here than
               FAYG. [They have obtained and burned exactly as much fuel up to this point].
            - Call the difference in time here d. Let's consider another output called Opt' which is identical to
               Opt in every way except the following changes:
                1. Let the time Opt'(x<sub>i</sub>) be Opt(x<sub>i</sub>) - d (which = F(x<sub>i</sub>)); and
                2. Add the time d to the following stop, so Opt'(x<sub>i+1</sub>) = Opt(x<sub>i+1</sub>) + d.
                
            - We can easily see now that Opt'(I) still solves the problem optimally because:
                1. There is still sufficient fuel to get from stop x<sub>i</sub> to x<sub>i+1</sub>, since the amount Opt' gets at that
                   point matches exactly how much FAYG gets which is by definition sufficient.
                2. Although this ^ gives a net decrease in fuel, that is made up for by adding the same amount to the
                   next stop (maybe include something about how if that exceeds fuel capacity it's okay, just distribute
                   through more stops?), so there is no problem getting to any of the remaining stops.
            - Therefore the net time stopped with Opt' is the same as Opt. The only difference is that Opt' agrees with 
               FAYG for one more step than Opt. But this contradicts the fact that Opt agrees most with FAYG.
               
               QED
               
               
              
        ISAAC ALSO CHECK THIS ONE TO MAKE SURE THIS IS A LEGIT COUNTEREXAMPLE       
         
B) CLAIM: The totally-full (TF?) algorithm does not correctly solve the problem; that is, it may produce an output without
          optimally minimal fill-up times.
   PROOF: Counterexample
            Consider the final stage of a trip. The TF algorithm will fill up entirely at whatever its last stop is, call it x_k.
            If our destination is at location x<sub>n</sub>, then we only need exactly (x<sub>n</sub> - x<sub>k</sub>)(F) liters of
            fuel to get to your destination (albeit on an empty tank). If that amount is *any* less than C, then there will be
            excess fuel, which means the time taken to fill up at the final stop (x<sub>k</sub>) could have been reduced.
            
            Thus the algorithm produces an inoptimal result and is incorrect.

6) Consider the contra, A(I), Opt(I), etc

We have some line l where A(I) and Opt(I) first differ.
They will differ because a word i will be on this line in A(I) and not in Opt(I).
This is because it is more optimal for this word to be on the next line, causing some other word to break.

Consider Opt'(I), where Opt'(I) is exactly the same as Opt(I), except that i is on line l.
This still satisfies all criteria, except that it may have more overall penalty than Opt(I).
First, on line l, we actually have w_i less penalty, 
but are a wash becuase there is w_i penalty on line l+1. But remember that we had to break some other word, j, onto line l+2. 
The same thing happens: line l+2 increases in penalty, but l+3 loses the same amount.

At some point, this process of line breaking has to end.
If it does not end by breaking to a final new line, then overall penalty has not changed.
This is because some word was moved onto a line big enough to fit it without breaking another word.
So, that word's penalty would either be on the upper or lower lines, but still there.

Now, if the line breaking ends by putting some word onto a new line all by itself, then there is the additional penalty of the unused space of that line.
If this were the case, Opt(I) could be equally or less optimal than A(I), and so this is not possible.

Thus, we have found a new solution, Opt'(I), which agrees with A(I) for (at least) one more line than does Opt(I), which contradicts the definition of Opt(I).

Thus, with this contradiction, we have that algorithm A is indeed correct.




