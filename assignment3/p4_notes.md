Problem 4 -- ISAAC VERIFY THIS IS CORRECT AND ALSO THAT THIS COUNTS AS AN "EXCHANGE" ARGUMENT AS REQUESTED IN THE INSTRUCTIONS


A) THEOREM: The fill-as-you-go (FAYG?) algorithm correctly solves the problem.
   PROOF:   Assume, tgac, that algorithm FAYG is incorrect; that is, suppose that there exists some input I for 
            which FAYG produces a nonoptimal result. Call this output F(I).
            Let Opt(I) be the output of an optimal algorithm that solves this problem which is most similar to
            F(I); that is, from the beginning it agrees with F(I) for the most number of steps.
            
            - Consider the first point of disagreement between Opt(I) and F(I). This would be a stop x_i where the
               two algorithms take different amounts of time filling up. Since FAYG always gets just enough fuel to
               make it to the next station, and Opt(x<sub>i</sub>) \!= F(x<sub>i</sub>), we know that Opt must take *more* time here than
               FAYG.
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