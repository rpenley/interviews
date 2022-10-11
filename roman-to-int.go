package main

import (
    "fmt"
)

func romanToInt(s string) int {
    
    var sum int = 0
    r2i := make(map[string]int)
    r2i["I"] = 1
    r2i["V"] = 5
    r2i["X"] = 10
    r2i["L"] = 50
    r2i["C"] = 100
    r2i["D"] = 500
    r2i["M"] = 1000
    
    for i := len(s); i > 0; i-- {
        if i > 1 {
            if (s[i-1] == 'V' || s[i-1] == 'X') && s[i-2] == 'I' {
                sum += r2i[string(s[i-1])] - r2i[string(s[i-2])]
                i--
            } else if (s[i-1] == 'L' || s[i-1] == 'C') && s[i-2] == 'X' {
                sum += r2i[string(s[i-1])] - r2i[string(s[i-2])]
                i--
            } else if (s[i-1] == 'D' || s[i-1] == 'M') && s[i-2] == 'C' {
                sum += r2i[string(s[i-1])] - r2i[string(s[i-2])]
                i--
            } else {
                sum += r2i[string(s[i-1])]
            }
        } else {
            sum += r2i[string(s[i-1])]
        }
    }
    return sum;
}

func main() {
		var roman string
		fmt.Print("Please input valid roman numeral: ")
		fmt.Scanf("%s", &roman)
		fmt.Printf("Numeral Equivilant is %d\n", romanToInt(roman))
}
