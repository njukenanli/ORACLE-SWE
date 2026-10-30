## Environment Setup

```bash
python3.12 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip && pip install --editable .

cp -r swerex venv/lib/python3.12/site-packages/swerex.

pip install openai azure-identity-broker --upgrade
```

## Use agent to extract the five signals

```bash

nohup sweagent run-batch --config config/ablation_rep_cl.yaml --num_workers 1 --instances.type swe_bench --instances.subset dataset/live_50.jsonl > log_live_cl_rep.out 2>&1 &


```