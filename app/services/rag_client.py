import httpx
from app.core.config import settings

async def ask_rag(question: str, division_id: str, role: str):
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(
            f"{settings.RAG_SERVICE_URL}/query",
            json={
                "question": question,
                "division_id": division_id,
                "role": role
            }
        )
        resp.raise_for_status()
        return resp.json()
