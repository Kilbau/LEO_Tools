### Creating Custom Vex Functions ###


## Modify input parameters and return them ##
```C
//create function with multiplier parameter
function void test(int in_a, in_b, multiplier)
{
    //no need to return those values
    //they automatically replace the input paramters
    in_a *= multiplier;
    in_b *= multiplier;
}
//create function w/o multiplier parameter
function void test(int in_a, in_b)
{
    in_a *= 2;
    in_b *= 2;  
}

//initialize variables to allow houdini to read/write
int user_a = 2;
int user_b = 4;

//houdini uses the function with the same paramters
//test(user_a, user_b);
test(user_a, user_b, 4);
//test(2,4,4) doesnt work. the first two variables are read only

i@a = user_a;
i@b = user_b;
```
## Save functions to file and read them in wrangles ##
* Save the vex functions in a new file "Filename.h"
* In a wrangle import functions from the file 
```C
#include PATH/TO/FILE/Filename.h
//e.g. #include "$LEO/vex/LEO_evalLSystems.h"
```
* Use the functions as normally
