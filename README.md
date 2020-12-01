# Von-Koch-Snowflake
> A simple example of generating von koch snowflakes using recursion

[![Build Status](https://travis-ci.com/gampu/Von-Koch-Snowflake.svg?branch=master)](https://travis-ci.com/gampu/Von-Koch-Snowflake)

## Purpose
The purpose of this effort is to get familiar with:
* Generating von koch snowflakes using recursion
* Building and testing the code on travis

## Example Output
![example](https://github.com/gampu/Von-Koch-Snowflake/blob/master/example.png)

## How does it work?
- Lines 24-26 specify that we intend to create snowflakes along the borders of a triangle. This justify's the usage of `right( 120 )` on line 26.
- Each call to the `solve` function, breaks the given line of length `len` into 4 parts, each of length `len/4`. The four parts are drawn in a manner that   represent: `_/\_`. This justifies the usage of turning commands on lines 13, 15 and 17 which turn the turtle to the left by 60 &deg;, to the right by 120 &deg; and again to the left by 60 &deg; respectively.
- The above step is performed recursively except for the base case, in which, we simply draw a straight line.
