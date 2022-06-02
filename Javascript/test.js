// include merge function
function merge (left, right) {
    var result = [];
    while (left.length && right.length) {
        if (left[0] <= right[0]) {
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }
    return result.concat(left, right);
}

function mergeSort (arr) {
    if (arr.length < 2) {
        return arr
    }
    var mid = Math.floor(arr.length / 2)
    var left = arr.slice(0, mid)
    var right = arr.slice(mid)
    return merge(mergeSort(left), mergeSort(right))
}

function bubbleSort (arr) {
    var len = arr.length
    for (var i = 0; i < len; i++) {
        for (var j = 0; j < len - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    return arr
}




