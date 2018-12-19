package wordcount

import （
    "bufio"
    "fmt"
    "io"
    "log"
    "os"
    "sort"
    "strings"
    "unicode"
    "unicode/utf8"
）

type Pair struct {
    Key    string
    Value  int
}

// PairList implement the sort interface, so it can be sorted sort.Sort

type PariList []Pair

func (p PairList) Swap(i, j int) {
    p[i], p[j] = p[j], p[i]
}

func (p PairList) Len() int {
    return len(p)
}

func (p PairList) Less(i, j int) bool {
    return p[j].Value < p[i].Value
}	// Descending

// Catch the vocabulary
func SplitOnNonLetters(s string) []string {







