## Environment Setup

```bash
python3.12 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip && pip install --editable .

cp -r swerex venv/lib/python3.12/site-packages/swerex.

pip install openai azure-identity-broker --upgrade
```

## Run agent with extracted signals


### Rollout agent with ORACLE signals
```bash
# Rollout agent with ORACLE signals
nohup sweagent run-batch --config config/ablation_rep_cl.yaml --num_workers 1 --instances.type swe_bench --instances.subset dataset/live_50.jsonl > log_live_cl_rep.out 2>&1 &

nohup sweagent run-batch     --config config/multi/ablation_loc_rep.yaml     --num_workers 1     --instances.type swe_bench     --instances.subset data/pro/pyt/subset/api.jsonl  > log_pro_pyt_loc_rep.out 2>&1 &
```

### Rollout agent with agent-extracted signals
```bash
# Rollout agent with agent-extracted signals
nohup sweagent run-batch     --config config/forward/ablation_rep.yaml    --num_workers 1     --instances.type swe_bench     --instances.subset fork/SWE-agent-get-factor/dataset/forward_pro_pyt_gpt5.jsonl  > log_for_pro_rep_gpt5_to_gpt5.out 2>&1 &
```