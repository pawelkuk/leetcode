func shuffle(nums []int, n int) []int {
    var newSlice []int
    for idx := range nums[:n] {
        newSlice = append(newSlice, nums[idx], nums[idx+n])
    }
    return newSlice
}
