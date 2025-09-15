* arithmetic in bash is made with integers (below 0 is truncate)
* pipe formula to bc -l to operate with decimals
* use scale={value} to limit decimals (bc will truncate at this decimals)
* scale to value n+1 ; add +/- 5/(10^n+1) to result and truncate to the n decimal to do a round to nearest value.
  * ex : 17.7286 + 0.0005 = 17.7291 >>> trunc to n=3 >>> 17.729 (round of 17.7286)
  * ex : -14.4861 + -0.0005 = -14.4866 >>> trunc to n=3 >>> -14.486 (round of -14.4861)