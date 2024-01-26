import random
from typing import List

from fastapi import FastAPI

app = FastAPI()


@app.get("/get_users_skills", response_model=List[List[int]])
async def get_users_skills(num_users: int, num_all_skills: int) -> List[List[int]]:
    skill_scores = [20, 40, 60, 80, 100]
    num_user_skills = range(5, 16)
    users_skills = [[random.choice(skill_scores)
                     if j in random.sample(range(num_all_skills), random.choice(num_user_skills)) else 0
                     for j in range(num_all_skills)]
                    for _ in range(num_users)]

    return users_skills
