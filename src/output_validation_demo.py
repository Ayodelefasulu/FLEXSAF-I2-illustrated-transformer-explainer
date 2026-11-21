from pydantic import BaseModel, ValidationError
from typing import Literal

class SupportResponse(BaseModel):

	category: Literal[
		"Technical Issue",
		"Billing Issue",
		"Account Access"
	]

	priority: Literal[
		"Low",
		"Normal",
		"High"
	]

	suggested_action: str


# simulated LLM response
llm_response = {
	"category": "Financial Complaint",
	"priority": "Urgent",
	"suggested_action": "Investigate the transaction."
}


try:

    validated_response = SupportResponse(**llm_response)

    print("Valid LLM response")
    print(validated_response.model_dump())

except ValidationError as error:

    print("Invalid LLM response")
    print(error)

