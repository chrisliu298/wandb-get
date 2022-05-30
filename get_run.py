import json

import wandb

run_ids = ["run_id1", "run_id2"]

api = wandb.Api()


for id in run_ids:
    run = api.run(id)
    config = run.config
    summary = run.summary
    print(summary["avg_val_r2"])
    filename = id.split("/")[1]
    with open(f"{filename}.json", "w") as fp:
        json.dump(dict(run.config), fp)
