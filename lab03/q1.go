package main

import (
"fmt"
 "runtime"
 "sync"
 "time"
 )

// var numCPU = runtime.NumCPU()

func main() 
{
    var wg sync.WaitGroup
    wg.Add(2)

    fmt.Println("Starting Go Routines")
    go func() {
    	defer wg.Done()

    	time.Sleep(1 *time.Microsecond)
    	for char := 'a'; char < 'a'+26; char++ {
    		fmt.Printf("%c ", char)
    	    		
    	    	}    	
    }()

    go func(){
    	defer wg.Done()

    	for i := 1; i < 27; i++ {
    		fmt.Printf("%d", i)
    		
    	}
    }()

    fmt.Println("Waiting To Finish")
    wg.Wait()

    fmt.Println("Terminating Program")
}