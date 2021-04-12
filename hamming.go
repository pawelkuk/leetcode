package main

func merge(s1 set, s2 set) set {
	s := set{}
	for k := range s1 {
		s[k] = true
	}
	for k := range s2 {
		s[k] = true
	}
	return s
}

func intersect(s1 set, s2 set) bool {
	for k := range s1 {
		_, ok := s2[k]
		if ok {
			//fmt.Println(s1, s2, true)

			return true
		}
	}
	//fmt.Println(s1, s2, false)
	return false
}

func difference(s1 set, s2 set) int {
	res := 0
	for k := range s1 {
		_, ok := s2[k]
		if !ok {
			res++
		}
	}

	return res
}

type set map[int]bool

func minimumHammingDistance(source []int,
	target []int,
	allowedSwaps [][]int) int {
	var sets []set
	allInd := set{}
	notPresent := set{}

	//fmt.Println(allowedSwaps)
	for _, swap := range allowedSwaps {
		sets = append(sets, set{swap[0]: true, swap[1]: true})
		allInd[swap[0]] = true
		allInd[swap[1]] = true
	}
	for ind := range source {
		_, ok := allInd[ind]
		if !ok {
			notPresent[ind] = true
		}
	}
	var found bool
	var lastLen = 0
	for {
		found = false
		if lastLen == len(sets) {
			break
		} else {
			lastLen = len(sets)
		}
		for i, set1 := range sets {
			for j, set2 := range sets {
				if i != j && intersect(set1, set2) {
					sets = append(sets[:j], sets[j+1:]...)
					sets = append(sets[:i], sets[i+1:]...)
					newSet := merge(set1, set2)
					sets = append(sets, newSet)
					found = true
					break
				}
			}
			if found {
				break
			}
		}
	}
	res := 0

	for _, s := range sets {
		newSource := set{}
		newTarget := set{}
		for k := range s {
			newSource[source[k]] = true
			newTarget[target[k]] = true
		}
		res += difference(newSource, newTarget)
	}

	for k := range notPresent {
		if source[k] != target[k] {
			res++
		}
	}
	return res
}

func main() {
	source := []int{1, 2, 3, 4, 7, 9}
	target := []int{2, 1, 4, 5, 7, 10}
	allowedSwaps := [][]int{{0, 1}, {2, 3}}
	println(minimumHammingDistance(source, target, allowedSwaps))

	source = []int{5, 1, 2, 4, 3}
	target = []int{1, 5, 4, 2, 3}
	allowedSwaps = [][]int{{0, 4}, {4, 2}, {1, 3}, {1, 4}}
	println(minimumHammingDistance(source, target, allowedSwaps))
}
