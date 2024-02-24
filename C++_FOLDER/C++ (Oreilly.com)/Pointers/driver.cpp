// Nov 28, 2022
// Conditional If Statement

#include <iostream>

int main(){

    
    int x = 6;
    int y = 2;

    if(x > y){
        std::cout << "x is greater than y\n";
    }else if(y > x){
        std::cout << "y is greater than x\n";
    }else{        
        std::cout << "x and y are equal\n";
    }
    
    return 0;
}
