import pandas as pd
import wandb

# This script was adapted from:
# https://docs.wandb.ai/guides/track/public-api-guide#export-metrics-from-all-runs-in-a-project-to-a-csv-file

api = wandb.Api()
entity, project = "entity", "project_name"
runs = api.runs(entity + "/" + project)

results = []

for run in runs:
    summary = run.summary._json_dict
    config = {k: v for k, v in run.config.items() if not k.startswith("_")}
    result = {**summary, **config}
    result["run_name"] = run.name
    results.append(result)

runs_df = pd.DataFrame(results)
print(runs_df.shape)
runs_df.to_csv(f"{project}.csv")
