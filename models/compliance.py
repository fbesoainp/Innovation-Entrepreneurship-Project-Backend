from pydantic import BaseModel, Field


class ComplianceRequest(BaseModel):
    interview_transcript: str = Field(..., title="Interview Transcript")
    resume: str = Field(..., title="Resume")
    job_description: str = Field(..., title="Job Description")
    company_policy: str = Field(..., title="Company Policy")
    hiring_decision: str = Field(..., title="Hiring Decision")
    justification: str = Field(..., title="Justification")


class ComplianceResponse(BaseModel):
    score: int = Field(..., title="Compliance Score")
    explanation: str = Field(..., title="Compliance Explanation")
