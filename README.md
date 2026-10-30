# ORACLE-SWE

This is the source code of the paper [ORACLE-SWE](https://arxiv.org/abs/2604.07789).

## Repository Structure

```
|_./README.md
|_./pyproject.toml
|
|_src dir: codes to extract the five ORACLE information singals
|   |_src/pipeline is the complete extraction pipeline
|
|_fork dir
    |_SWE-agent-run-GT: rollout the agent with extracted signals
    |_SWE-agent-get-factor: get the five agent-extracted factors
    |_SWE-bench-Live: evaluate SWE-bench and SWE-bench-Live patches
    |_SWE-bench-Pro: evaluate SWE-bench-Pro patches
```

## Environment Setup

### For src dir

Just `pip install . ` at the root dir.

### For each forked project

Create a separate venv for each forked project. 

Follow the README in each forked sub-directory to install the dependencies. 

Remember that the swerex library in the venv of SWE-agent needs to be replaced by our modified version venv/lib/python3.12/site-packages/swerex.
