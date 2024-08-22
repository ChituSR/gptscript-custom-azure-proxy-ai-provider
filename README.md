1. You must be having with the Azure Proxy endpoint and API_KEY


## Usage Example

```
gptscript --default-model='gpt-4-32k' examples/helloworld.gpt
```

## Development

Run using the following commands

```
python -m venv .venv
source ./.venv/Scripts/activate
pip install -r requirements.txt
./run.sh
```

```
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export GPTSCRIPT_DEBUG=true
gptscript --default-model=gpt-4-32k examples/bob.gpt
```
