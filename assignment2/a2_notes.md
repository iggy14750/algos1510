
Problem 1) Let A be the specified algorithm, which produces output A(I) for given input I.
CLAIM: Algorithm A solves the problem.
PROOF: Assume, to get a contradiction, that A does not solve the problem. That is, suppose that for some input I, A(I) is not optimal.
       Let Opt be an optimal solution that is most like A(I). They cannot be the same else A(I) would be optimal.
       
       Consider any region of difference (RoD) where A(I) differs from Opt. Within such a region, Opt must contain more intervals than A(I):
        1. If there are fewer, then A(I) has more disjoint intervals than Opt, contradicting optimality of Opt.
        2. If there are the same, then A(I) has the same cardinality as OPT, contradicting incorrectness of A(I).
        3. If there are more in this region but fewer in another, then either 1 or 2 still applies but over the entire solution, leading to the
           same contradictions. Alternatively, as claimed, there are more intervals within the arbitrary RoD we've selected.
           
       Because there are more intervals in Opt than A(I), we have the following within the RoD:
        1. There cannot exist any interval in Opt that is disjoint from all in A(I). This would contradict the algorithm, since A would have 
           chosen such an interval.
        2. There cannot exist any interval in Opt that has fewer overlaps than every interval in A(I). This would again contradict the
           algorithm, since A would have chosen such an interval, it having fewer overlaps.
        3. So every interval in OPT must have at least as many overlaps as the minimum overlapping interval in A(I), denoted min\{A(I)\}.
           That is, for all intervals x in Opt, overlaps(x) >= overlaps(min{A(I)}).
        
        Because there are strictly more intervals in Opt than A(I) and each has \textbf{at least} the number of overlaps as min\{A(I)\},
        it follows that, within the RoD, the total set of intervals in Opt overlaps more than the total set of intervals in A(I).
        That is, SUM(over x in Opt) of overlaps(x) > SUM(over y in A(I)) of overlaps(y).
        
        
        Because there are more overlaps in Opt than in A(I), there are necessarily fewer remaining intervals once those in OPT have been
        selected. In this case, there must be 0 remaining (else Opt would have selected more, contradicting its selection as optimal). Then
        because the selection of intervals in A(I) has overlapped (and hence eliminated) strictly fewer other intervals, there must be some
        nonzero number of intervals left for A to select. This contradicts algorithm A--if we included those leftover intervals in A(I), then
        A(I) would ultimately match the cardinality of Opt, once again contradicting the nonoptimality of A(I).
        
        In any case, we have derived a contradiction, proving that A does in fact solve the problem.
           
        