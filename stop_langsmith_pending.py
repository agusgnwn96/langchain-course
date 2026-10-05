from datetime import datetime, timezone
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

client = Client()
now = datetime.now(timezone.utc)

project = client.read_project(project_name="ReAct Under The Hood")

for run in client.list_runs(project_id=project.id, is_root=True):
    if run.end_time is None:
        client.update_run(
            run.id,
            end_time=now,
            error="Interrupted manually (KeyboardInterrupt)",
        )
        print("Closed:", run.name, run.id)