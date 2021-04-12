func maximumWealth(accounts [][]int) int {
    currMax := 0
    var tmp int
    for _, accountsCustomer := range accounts{
        tmp = 0
        for _, account := range accountsCustomer{
            tmp += account
        }
        if tmp > currMax{
            currMax = tmp
        }
    }
    return currMax
}
