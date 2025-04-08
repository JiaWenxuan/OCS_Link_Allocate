import random
from typing import Dict, List, Tuple
from links import Links
from groups import Groups
from job import Job, Jobs


def allocate_test():
    group = Groups()
    jobs = Jobs()
    time = 0
    while jobs.has_more_jobs():
        free_job_arrive_time()
        while True:
            job = jobs.get_next_job()
            if job is None:
                break
            # link_demand : [(group_id_1, group_id_2, min_links, max_links), ...]
            link_demand: List[Tuple[int, int, int, int]] = gpu_allocate(job.gpu_count, group)
            if not link_demand:
                break
            b = logic_link_allocate(job.gpu_count, Links, a)
            if not b:
                break
            c = physical_link_allocate(job.gpu_count, Links, b)
            if not c:
                break
            print(f"Job {jobs.current_index} allocated at time {time}, remaining jobs: {jobs.get_remaining_jobs_count()}")
            jobs.current_index += 1
    time += 1


if __name__ == "__main__":
    allocate_test()
