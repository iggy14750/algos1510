Problem 4

A) Theorem: The fill-as-you-go (FAYG?) algorithm correctly solves the problem.
   Proof:   Assume, tgac, that algorithm FAYG is incorrect; that is, suppose that there exists some input I for 
            which FAYG produces a nonoptimal result. Call this output F(I).
            Let Opt(I) be the output of an optimal algorithm that solves this problem which is most similar to
            F(I); that is, from the beginning it agrees with F(I) for the most number of steps.
            
            -- Consider the first point of disagreement between Opt(I) and F(I). This would be a stop x_i where the
               two algorithms take different amounts of time filling up. Since FAYG always gets just enough fuel to
               make it to the next station, and Opt(x_i) != F(x_i), we know that Opt must take MORE time here than
               FAYG.
            -- Call the difference in time here d. Let's consider another output called Opt' which is identical to
               Opt in every way except the following changes:
                1. Let the time Opt'(x_i) be Opt(x_i) - d (which = F(x_i)); and
                2. Add the time d to the following stop, so Opt'(x_i+1) = Opt(x_i+1) + d.
                
            -- We can easily see now that Opt'(I) still solves the problem optimally because:
                1. There is still sufficient fuel to get from stop x_i to x_i+1, since the amount Opt' gets at that
                   point matches exactly how much FAYG gets which is by definition sufficient.
                2. Although this ^ gives a net decrease in fuel, that is made up for by adding the same amount to the
                   next stop (maybe include something about how if that exceeds fuel capacity it's okay, just distribute
                   through more stops?), so there is no problem getting to any of the remaining stops.
            -- Therefore the net time stopped with Opt' is the same as Opt. The only difference is that Opt' agrees with 
               FAYG for one more step than Opt. But this contradicts the fact that Opt agrees most with FAYG.
               
               QED