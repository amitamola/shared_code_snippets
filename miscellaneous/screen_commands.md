# Some helpful Screen Commands for terminal

#### Create screen from Terminal  
```screen -S screen_name```

#### To see the list of screens  
```screen -ls```   
```screen -list```

#### To reattach to a particular screen that is already attached  
```screen -x screen_name```

#### To attach to a detached screen  
```screen -r screen_name```

#### To Terminate screen  
```ctrl + d```

#### To Detach the screen  
```ctrl + a + d```   
```screen -d```

#### To kill a screen from Terminal
```screen -X -S screen_name quit ```  
```screen -X -S screen_name kill```
