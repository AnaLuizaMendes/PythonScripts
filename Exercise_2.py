# testing hackerrank challengings

# lists problem
if __name__ == '__main__':
    N = (raw_input())
    new_list = []
    i = 0

    while i <= N:
        try:
            x = str(raw_input())
        except EOFError:
            break

        word = list(x.split())

        if 'insert' in word:
            new_list.insert(int(word[1]), int(word[2]))

        if 'print' in word:
            print(new_list)

        if 'remove' in word:
            new_list.remove(int(word[1]))

        if 'append' in word:
            new_list.append(int(word[1]))

        if 'sort' in word:
            new_list.sort()

        if 'pop' in word:
            new_list.pop(-1)

        if 'reverse' in word:
            new_list.reverse()

        i += 1
