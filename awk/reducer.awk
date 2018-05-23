{
	if (prev == "") {
		prev = $0
		cnt = 1
	}
	else if ($0 != prev) {
		print prev, cnt
		prev = $0
		cnt = 1
	}
	else
		cnt += 1
}

END {
	print prev, cnt
}

