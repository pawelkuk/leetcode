func minPartitions(n string) int {
	currMax := int32(0)
	for _, rune_ := range n {
		if currMax < rune_ {
			currMax = rune_
		}
	}
	return int(currMax-'0')
}

