import requests, re, json

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36h-site=cross-site'
}
playinfo_pattern = r'(?<=window.__playinfo__=)(.*?)(?=</script>)'
session = requests.session()


def get_audio_url(video_url):
    response = session.request("GET", video_url, headers=headers, data={})
    print(response.text)
    match = re.search(playinfo_pattern, response.text, re.DOTALL)
    if match:
        print(match.group(1))  # prints the JSON data
    else:
        print("No playinfo match found")
        exit(1)
    return json.loads(match.group(1))['data']['dash']['audio'][0]['base_url']


def download_audio(video_url):
    audio_url = get_audio_url(video_url)
    print('audio url:', audio_url)
    response = session.request("GET", audio_url, headers=headers, data={})
    with open('mp4_demo.mp4', 'wb') as fp:
        fp.write(response.content)


download_audio("https://www.bilibili.com/video/BV1v1421z7R2/?spm_id_from=333.788.top_right_bar_window_history.content.click")
