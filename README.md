# DBrush
A implementation of Chinese painting brush model

## Method

    |     |                    |     |
    |     |                    |     |
    |     |                    |     |
    |     |                    |     |
    |     |        ----->      |     |
    -------                     -----   
    (     )                       |
     (   )                        |
      ( )                         |
       !                          !


Let a soft line to represent the brush.
Every point in the soft line has its area, which is relative to the height of the point over the paper, denoted by z
The brush tip's root is h over the paper.
So when h-z>0, the brush point can not leave any ink in the paper. When h-z<0, the point coordinate is (x+(z-h)cos theta, y+ (z-h)sin theta), which means

        |     |
        |     |
        |     |
        |     |
        -------
           |
           |
           |
           |____       

The brush point's move will follow its upper point.