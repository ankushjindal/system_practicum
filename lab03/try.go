package main

import(
// "config"
"fmt")

c := make(chan string/*, config.Buffer_size*/)
 
num_cores := 1
for i:=0; i<num_cores; i++ {
    go func(c chan string) {
            <-c
        }
    }(c)
}
 
message := "x"
 
for i:=0; i<10000000; i++ {
    c <- message
}