#!/bin/bash
funWithParam(){
    echo "The first parameter is $1 !"
    echo "The second parameter is $2 !"
    echo "The tenth parameter is $10 !"
    echo "The tenth parameter is ${10} !"
    echo "The total number os parametres is $# !"
    echo "The eleventh parameters is ${11} !"
    echo "Outputs all parameters as a string $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
