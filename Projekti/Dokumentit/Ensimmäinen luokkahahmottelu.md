```Mermaid
classDiagram
    class game{
        sizex: int
        sizey: int
        levels: Array
    }
    
    class level{
        platforms: Array
        enemies: Array
        Collectables: Array
        checkpoints: Array

    }
    class hahmo {
        #paikka: vector
        -nopeus: vector
        -kiihtyvyys: vector
        -max_nopeus: vector
    }
    class pelaaja{
        
    }
    class kerättävä
    class checkpoint
    class platform
    class vihollinen
    class valolähde
    
    hahmo --|> pelaaja
    hahmo --|> vihollinen
    pelaaja -- kerättävä :collision dedection
    hahmo -- platform :collision dedection
    pelaaja -- checkpoint :collision dedection
    vihollinen -- pelaaja :collision dedection
    hahmo --o valolähde
    checkpoint --o valolähde
    kerättävä --o valolähde
```