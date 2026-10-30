```bash
pip install datasets pandas
```


```python
from datasets import load_dataset
swebench = load_dataset('ScaleAI/SWE-bench_Pro', split='test')
```


Run the following commands to store modal credentials:
```
pip install modal
modal setup # and follow the prompts to generate your token and secret
```

After running these steps, you should be able to see a token ID and secret in  `~/.modal.toml`:
EG:
```
token_id = <token id>
token_secret = <token secret>
active = true
```

We store prebuilt Docker images for each instance. 

`jefzda/sweap-images:{repo_base}.{repo_name}-{repo_base}__{repo_name}-{hash}`

For example:

`jefzda/sweap-images:gravitational.teleport-gravitational__teleport-82185f232ae8974258397e121b3bc2ed0c3729ed-v626ec2a48416b10a88641359a169d99e935ff03`

Note that bash runs by default in our images. e.g. when running these images, you should not manually envoke bash. See https://github.com/scaleapi/SWE-bench_Pro-os/issues/6


```bash
python helper_code/gather_patches.py \
    --directory <path_to_pred_files> \
    --prefix <model_name> \
    --output <output_file>.json
```


```bash
python swe_bench_pro_eval.py \
    --raw_sample_path=swe_bench_pro_full.csv \
    --patch_path=<your_patches>.json \
    --output_dir=<output_directory> \
    --scripts_dir=run_scripts \
    --num_workers=100 \
    --dockerhub_username=jefzda
```


```bash
nohup python swe_bench_pro_eval.py  --raw_sample_path=/home/v-kenanli/workspace/ablation/data/pro/pyt/original_pro.jsonl --patch_path=/home/v-kenanli/workspace/ablation/fork/SWE-agent/trajectories/v-kenanli/ablation_rep_api__gpt-5-20250807__t-0.00__p-1.00__c-0.00___swe_bench_/home/v-kenanli/workspace/ablation/data/pro/pyt/subset/api.jsonl_dev/preds.json  --output_dir=logs/eval/pyt-rep-api --scripts_dir=run_scripts    --num_workers=10   --use_local_docker  --dockerhub_username=jefzda > log-pyt-rep-api.out 2>&1 &
```