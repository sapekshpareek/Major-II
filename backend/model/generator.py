from typing import Dict, List

def generate_response(query_info: Dict, search_results: List[Dict], classification_result: Dict = None):
    """
    Generate structured response based on query analysis and search results
    Args:
        query_info (dict): Preprocessed query information
        search_results (list): Relevant BNS sections
        classification_result (dict): Query classification results
    Returns:
        dict: Structured response
    """
    try:
        # Initialize response
        response = {
            "query_understanding": {},
            "legal_advice": [],
            "relevant_sections": [],
            "next_steps": []
        }

        # Add query understanding
        if classification_result:
            response["query_understanding"]["category"] = classification_result["category"]
            response["query_understanding"]["confidence"] = classification_result["confidence"]

        # Add identified entities
        if query_info.get("entities"):
            response["query_understanding"]["identified_entities"] = query_info["entities"]

        # Process search results
        for result in search_results:
            section_info = {
                "section_number": result["section_number"],
                "name": result["name"],
                "relevance": result["similarity_score"],
                "description": result["description"],
                "punishment": result["punishment"]
            }
            response["relevant_sections"].append(section_info)

        # Add next steps based on the type of case
        if classification_result:
            if "Murder" in classification_result["category"]:
                response["next_steps"] = [
                    "File an FIR immediately at the nearest police station",
                    "Preserve any evidence related to the crime",
                    "Contact a criminal law attorney",
                    "Document all relevant details of the incident"
                ]
            elif "Theft" in classification_result["category"]:
                response["next_steps"] = [
                    "File a police complaint immediately",
                    "Make a list of stolen items with descriptions",
                    "Check for any CCTV footage in the area",
                    "Contact your insurance company if applicable"
                ]

        return response

    except Exception as e:
        print(f"Response generation error: {str(e)}")
        return None

if __name__ == "__main__":
    print(generate_response("My friend was murdered. What should I do?"))
