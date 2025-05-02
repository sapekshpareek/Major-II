from flask import Flask, request, jsonify
from flask_cors import CORS
from model.retrieval import search_legal_text
from model.classifier import classify_intent
from model.preprocess import preprocess_text
from model.generator import generate_response

app = Flask(__name__)
CORS(app)

@app.route('/api/query', methods=['POST'])
def process_query():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        # Step 1: Preprocess the query
        preprocessed_data = preprocess_text(query)
        if not preprocessed_data:
            return jsonify({'error': 'Preprocessing failed'}), 500

        # Step 2: Classify the query intent
        classification = classify_intent(query)

        # Step 3: Search for relevant sections
        search_results = search_legal_text(preprocessed_data["processed_text"])

        # Step 4: Generate structured response
        response = generate_response(
            query_info=preprocessed_data,
            search_results=search_results,
            classification_result=classification
        )

        return jsonify({
            'success': True,
            'response': response
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
