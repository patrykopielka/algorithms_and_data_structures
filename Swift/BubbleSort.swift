import Foundation

public func bubbleSort(array: [Int]) -> [Int] {
    
    var arr = array
    let n = arr.count - 1
    
    for i in 0..<n {
        for j in 0..<n-i {
            if arr[j] > arr[j+1] {
                let tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
            }
        }
    }
    return arr
}
