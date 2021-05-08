func isIn(p , q []int) bool {
    return (p[0] - q[0])*(p[0] - q[0]) +  (p[1] - q[1])*(p[1] - q[1]) <= q[2]*q[2]
}

func countPoints(points [][]int, queries [][]int) []int {
    var arr []int
    for idx, q := range queries {
        arr = append(arr, 0)
        for _, p := range points {
            if isIn(p, q) {
                arr[idx]++
            }
        }
    }
    return arr
}
