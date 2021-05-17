import Foundation

func insertionSort(array: [Int]) -> [Int] {
    
    let n = array.count
    var arr = array
    
    for j in 0..<n {
        let key = arr[j]
        var i = j - 1
        while i>=0 && arr[i] > key {
            arr[i + 1] = arr[i]
            i -= 1
        }
        arr[i + 1] = key
    }
    return arr
}
