import datetime


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


now = datetime.datetime.now()
today_str = now.strftime("%Y%m%d")
formatted_date = now.strftime("%Y/%m/%d")
print(f"本日の日付は{today_str}です\n")

base = int(today_str + "0000")

limit = None
try:
    user_input = input(
        "取得する素数の個数を入力してください（制限なしの場合はそのままEnter）: "
    )
    if user_input.strip():
        limit = int(user_input)
except EOFError:
    print(
        "※入力がサポートされていない環境のため、制限なし（全件出力）で実行します。"
    )

primes = []

for hour in range(0, 24):
    for minute in range(0, 60):
        offset = hour * 100 + minute

        if offset % 2 == 0:
            continue

        if is_prime(base + offset):
            primes.append((base + offset, hour, minute))

            if limit is not None and len(primes) == limit:
                break
    if limit is not None and len(primes) == limit:
        break

print(f"\n=== 出力1：配列形式（合計 {len(primes)} 個） ===")
raw_prime_list = [item[0] for item in primes]
print(raw_prime_list)

print("\n=== 出力2：CSV形式（カンマ区切り） ===")
print("日付,時刻,12桁の素数")
for prime, h, m in primes:
    time_str = f"{h:02d}:{m:02d}"
    print(f"{formatted_date},{time_str},{prime}")
