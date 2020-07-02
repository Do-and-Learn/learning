import requests

if __name__ == '__main__':
    with open("token", "r", encoding="utf-8") as f:
        token = f.read().strip()

    message = "哈囉!"
    resp = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Bearer {token}"},
        data={"message": message}
    )

    print(resp.text)
