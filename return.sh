#!/bin/bash
funWithReturn(){
    echo "This function will add the two numbers of the input...."
    echo "Enter the first number:"
    read aNum
    echo "Enter the second number:"
    read anotherNum
    echo "The two numbers are $aNum and $anotherNum!"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "The sum of the two numbers entered is $? !"

