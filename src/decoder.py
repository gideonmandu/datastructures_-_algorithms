from string import ascii_lowercase


def solution(x: str) -> str:
    abc = list(ascii_lowercase)
    zyx = list(reversed(abc))
    decoded = ""
    for i in x:
        if i == i.lower() and i in abc:
            index = abc.index(i)
            decoded += zyx[index]
        else:
            decoded += i
    return decoded



if __name__ == "__main__":
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
