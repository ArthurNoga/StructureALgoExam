def selection(a: list, reverse: bool = False) -> list:
	for i in range(0, len(a)):
		key = a[i]
		mini = i
		for j in range(i + 1, len(a)):
			if reverse:
				if a[mini] < a[j]:
					mini = j
			else:
				if a[mini] > a[j]:
					mini = j
		a[i] = a[mini]
		a[mini] = key
	return a


def insertion(a: list, reverse: bool = False) -> list:
	for i in range(1, len(a)):
		key = a[i]
		j = i - 1
		if reverse:
			while j >= 0 and key > a[j]:
				a[j + 1] = a[j]
				j = j - 1
		else:
			while j >= 0 and key < a[j]:
				a[j + 1] = a[j]
				j = j - 1
		a[j + 1] = key
	return a


def mergeSort(a: list, p: int, r: int, reverse: bool = False) -> list:
	if p >= r:
		return
	else:
		q = (p + r) // 2
		mergeSort(a, p, q, reverse)
		mergeSort(a, q + 1, r, reverse)
		fusion(a, p, q, r, reverse)
	return a


def fusion(a, p, q, r, revere: bool = False):
	n1 = q - p + 1
	n2 = r - q
	L = [None] * (n1 + 1)
	R = [None] * (n2 + 1)
	L[:n1] = a[p:q + 1]
	R[:n2] = a[q + 1:r + 1]
	i = 0
	j = 0
	if revere == True:
		L[n1] = R[n2] = -math.inf
		for k in range(p, r + 1):
			if L[i] > R[j]:
				a[k] = L[i]
				i += 1
			else:
				a[k] = R[j]
				j += 1
	else:
		L[n1] = R[n2] = math.inf
		for k in range(p, r + 1):
			if L[i] < R[j]:
				a[k] = L[i]
				i += 1
			else:
				a[k] = R[j]
				j += 1


def search(a: list, element: int, ordered: bool = False) -> list:
	if ordered:
		p = 0
		r = len(a) - 1
		while p <= r:
			q = (p + r) // 2
			if a[q] == element:
				return q
			elif a[q] > element:
				r = q - 1
			else:
				p = q + 1
		return -1
	else:
		for i in range(0, len(a) - 1):
			if a[i] == element:
				return i
		return -1

def tri_bulle(tab):
	n = len(tab)
	# Traverser tous les éléments du tableau
	for i in range(n):
		for j in range(0, n-i-1):
			# échanger si l'élément trouvé est plus grand que le suivant
			if tab[j] > tab[j+1] :
				tab[j], tab[j+1] = tab[j+1], tab[j]