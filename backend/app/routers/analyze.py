from fastapi import APIRouter
from app.models.prompt_schema import PromptRequest, AnalyzeResponse
from app.services.spacy_analyzer import parse_prompt
from app.services.prompt_scorer import score_prompt
from app.services.suggestion_generator import generate_suggestions
from app.services.model_responder import generate_model_response

router = APIRouter()

@router.post("/", response_model=AnalyzeResponse)
def analyze_prompt(data: PromptRequest):
    prompt = data.prompt
    api_key = data.api_key
    create_answer = data.create_answer

    tokens = parse_prompt(prompt)
    raw_score = score_prompt(prompt, api_key)

    scores = {
        "clarity": raw_score["clarity"],
        "control": raw_score.get("control") or raw_score.get("controllability", 0),
        "goal_specificity": raw_score.get("goal_specificity") or raw_score.get("specificity", 0),
        "ambiguity": raw_score["ambiguity"],
        "readability": raw_score["readability"]
    }

    suggestions = generate_suggestions(prompt, tokens, api_key)

    model_response = None
    if create_answer:
        model_response = generate_model_response(prompt, api_key)

    return {
        "tokens": tokens,
        "scores": scores,
        "reason": raw_score["reason"],
        "suggestions": suggestions,
        "model_response": model_response
    }
