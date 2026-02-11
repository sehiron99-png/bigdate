def add(a, b):
    return a + b
print("현재 파일 이름", __name__)

def sub(a, b):
    return a - b


if __name__ == "__main__":  # 직접 호출시 main으로 나옴
    print(add(1, 4))        # import호출시 파일 이름으로 나옴
    print(sub(4, 2))