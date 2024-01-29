import random
from typing import List
from fastapi import FastAPI
import numpy as np

app = FastAPI()


@app.get("/get_users_skills")
async def get_users_skills(num_users: int, num_all_skills: int):
    skill_scores = [20, 40, 60, 80, 100]
    num_user_skills = range(5, 16)

    users_skills = np.array([
        [
            random.choice(skill_scores) if j in random.sample(range(num_all_skills),
                                                              random.choice(num_user_skills)) else 0
            for j in range(num_all_skills)
        ]
        for _ in range(num_users)
    ])

    cos_similarity = np.apply_along_axis(
        lambda x: np.dot(x, users_skills.T) / (np.linalg.norm(x) * np.linalg.norm(users_skills, axis=1)),
        axis=1,
        arr=users_skills
    )

    sorted_users_skills = users_skills[np.argsort(-cos_similarity)].tolist()[0]

    return sorted_users_skills
