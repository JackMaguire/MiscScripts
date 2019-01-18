NR==1 {
    for (i=1; i<=NF; i++) {
        ix[$i] = i
    }
}
NR==2 {
    for (i=1; i<=NF; i++) {
        ix[$i] = i
    }
}
NR>2 {
    print $ix[c1]
}
