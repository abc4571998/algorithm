let result = 0;
function calc(arr, index, current, target) {
    if(index === arr.length) {
        if(current === target) {
            result += 1;
        }
        return ;
    }
    //for(let i = index; i < arr.length-1; i++) {
    calc(arr, index+1, current+arr[index], target)
    calc(arr, index+1, current-arr[index], target)
    //}
}

function solution(numbers, target) {
    var answer = 0;
    // 1. 다음 원소를 더하거나 빼거나 경우
    // 2. 더하거나 뺀 결과 넘기기
    calc(numbers, 0, 0, target);
    return result;
}