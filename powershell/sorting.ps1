

function GenerateRandomIntArray {
    param( [int]$array_size )

    $arr = @()

    for($i = 0; $i -lt $array_size; $i++){
        $arr += Get-Random -Minimum 0 -Maximum 999
    }
    return $arr
}

function PrintArray { param( $arr)

    foreach($j in $arr){
        Write-Host $j
    }

}

function Selection-Sort { param ( $arr )
    Write-Host "Selection Sort:"
    Write-Host $arr
    for($i = 0; $i -lt $arr.Length; $i++){
        #Write-Host "Pass $($i+1)"
        $current_min = $i
        for($current_item= $i+1; $current_item -lt $arr.Length; $current_item++) {
            if($arr[$current_item] -lt $arr[$current_min]){
                $current_min = $current_item
            }
        }
        $temp = $arr[$i]
        $arr[$i] = $arr[$current_min]
        $arr[$current_min] = $temp
        #Write-Host $arr

    }

    return $arr
}

function Bubble-Sort { param ($arr)
    Write-Host "Bubble Sort:"
    Write-Host $arr

    $unsorted = $arr.Length
    
    for($i=1; $i -lt $unsorted; $i++){
        for($j=0; $j -lt $unsorted-1; $j++){
            if($arr[$j] -gt $arr[$j+1]){
                $temp = $arr[$j]
                $arr[$j] = $arr[$j+1]
                $arr[$j+1] = $temp
            }
            
        }
        Write-Host "Pass $i - $arr"
    }

    return $arr

}

function Test-Sorting {
    $a = GenerateRandomIntArray(10)
    #PrintArray($a)
    #$sorted = Selection-Sort($a)
    $sorted = Bubble-Sort($a)
    Write-Host $sorted
}




