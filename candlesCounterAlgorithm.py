def birthdayCakeCandlesRecursive(candles, index=0, max_height=0, count=0):
    if index == len(candles):
        return count

    current = candles[index]

    if current > max_height:
        return birthdayCakeCandlesRecursive(candles, index + 1, current, 1)
    elif current == max_height:
        return birthdayCakeCandlesRecursive(candles, index + 1, max_height, count + 1)
    else:
        return birthdayCakeCandlesRecursive(candles, index + 1, max_height, count)

def birthdayCakeCandlesNonRecursive(candles):
    max_height = candles[0]
    count = 1

    for i in range(1, len(candles)):
        if candles[i] > max_height:
            max_height = candles[i]
            count = 1
        elif candles[i] == max_height:
            count += 1

    return count
def get_candles():
    n = int(input("Enter number of candles: "))
    candles = []

    for i in range(n):
        value = int(input(f"Candle {i+1} height: "))
        candles.append(value)

    return candles
def main():
    mode  = input("Enter the mode \n1 -- Recursive \n2 -- Non-Recursive: \n")
    if mode == "1":
        result = birthdayCakeCandlesRecursive(get_candles())
    elif mode == "2":
        result = birthdayCakeCandlesNonRecursive(get_candles())
    else:
        print("Invalid mode")
        return

    print("Number of tallest candles:", result)

main()