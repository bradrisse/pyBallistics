# pyBallistics

A Python port of GNU Ballistics Library

Created by Derek Yates

Updated by Brad Risse

The pyBallistics Library is a port of the popular GNU Ballistics Library to solve exterior ballistics problems through numerical integration. It is a lightweight, optimized library for general purpose ballistics solutions. In general, it is targeted at small arms exterior ballistics at ranges under 50,000 yards.

This library supports the standard Drag Functions: G1, G2, G3, G5, G6, G7, and G8

It is possible to have dozens of solutions in memory at once for comparing loads or different scenarios, and using this library, it should be fairly easy to create an excellent end-user ballistic software GUI. The high speed solution and excellent accuracy are better than many commercial offerings.

Exterior Ballistics Primer for Small Arms
Exterior ballistic problems do not generally have algebraic solutions. The models are step-wise models, developed using complex doppler radar ranges. Exterior ballistic models attempt to describe how a projectile behaves at a particular velocity by relating it to a "standard" projectile, which was tested in depth.

The most common drag function in use is the G1 drag function. Virtually all published "ballistic coefficient" data in reloading manuals and product literature are G1 drag coefficients.
