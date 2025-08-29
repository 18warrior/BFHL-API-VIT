from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data_input = request.json.get('data')

        if not isinstance(data_input, list):
            return jsonify({
                "is_success": False,
                "message": "Invalid input: 'data' must be a list."
            }), 400

        user_id = "john_doe_17091999" # As per example, replace with dynamic if needed
        email = "john@xyz.com" # As per example, replace with dynamic if needed
        roll_number = "ABCD123" # As per example, replace with dynamic if needed

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        numbers_sum = 0
        all_alphabets_concat = []

        for item in data_input:
            if isinstance(item, str):
                if item.isdigit():
                    num = int(item)
                    numbers_sum += num
                    if num % 2 == 0:
                        even_numbers.append(item) # Return as string as per instruction
                    else:
                        odd_numbers.append(item) # Return as string as per instruction
                elif item.isalpha():
                    alphabets.append(item.upper())
                    all_alphabets_concat.append(item)
                else:
                    special_characters.append(item)
            # Ignore other types as per examples, or add specific handling

        # Concatenation of all alphabetical characters in reverse order in alternating caps
        # Example A: ["a","R"] -> "Ra" (original order: a, R. reverse: R, a. alternating caps: R, a -> Ra)
        # Example B: ["a","y","b"] -> "ByA" (original order: a, y, b. reverse: b, y, a. alternating caps: B, y, A -> ByA)
        # Example C: ["A","ABcD","DOE"] -> "EoDdCbAa" (original order: A, ABcD, DOE. reverse: DOE, ABcD, A. alternating caps: E o D d C b A a -> EoDdCbAa)
        
        concat_string_list = []
        reversed_alphabets_for_concat = all_alphabets_concat[::-1]

        for char_group in reversed_alphabets_for_concat:
            for i, char in enumerate(char_group):
                if i % 2 == 0:
                    concat_string_list.append(char.upper())
                else:
                    concat_string_list.append(char.lower())
        
        concat_string = "".join(concat_string_list)


        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(numbers_sum), # Return sum as a string
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)