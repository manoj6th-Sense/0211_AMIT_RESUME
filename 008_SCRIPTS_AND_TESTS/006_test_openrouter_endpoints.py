import os
import urllib.request
import json

api_key = os.environ.get('OPENROUTER_API_KEY')
models_to_test = [
    'deepseek/deepseek-v4.1-flash-1017',
    'inclusionai/ling-3.1-flash',
    'z-ai/glm-5.3-flash',
    'openai/gpt-6-astra'
]

for m in models_to_test:
    data = {
        'model': m,
        'messages': [{'role': 'user', 'content': 'Ping. Reply Pong with your model name.'}],
        'max_tokens': 300
    }
    req = urllib.request.Request(
        'https://openrouter.ai/api/v1/chat/completions',
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
        data=json.dumps(data).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            msg = res['choices'][0]['message']
            content = msg.get('content') or ''
            reasoning = msg.get('reasoning') or ''
            provider = res.get('provider', 'unknown')
            usage = res.get('usage', {})
            pt = usage.get('prompt_tokens', 0)
            ct = usage.get('completion_tokens', 0)
            print(f"OK: {m} (via {provider}) -> content='{content[:40]}' | pt={pt}, ct={ct}")
    except Exception as e:
        print(f"ERR: {m} -> {e}")
