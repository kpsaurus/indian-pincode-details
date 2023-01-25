# Indian Pincode Details 🇮🇳📍

A package for retrieving a list of details based on a given pincode.


## Quick start

- Install from PyPI

  ```
  pip install indian-pincode-details
  ```

- Import the function to get the details
    ```
    from indian_pincode_details import get_pincode_details
    ```
  
- Retrieve the pincode details by passing a pincode. If no result is found, an empty list will be returned.

  ```
  result = get_pincode_details(560034)
  ```
- The result will be:
  ```
  [{'office_name': 'Koramangala I Block S.O', 'pincode': 560034, 'taluk': 'Bangalore South', 'district': 'Bangalore', 'state': 'Karnataka', 'country': 'India'}, {'office_name': 'Koramangala S.O', 'pincode': 560034, 'taluk': 'Bangalore South', 'district': 'Bangalore', 'state': 'Karnataka', 'country': 'India'}, {'office_name': 'St. John"s Medical College S.O', 'pincode': 560034, 'taluk': 'Bangalore South', 'district': 'Bangalore', 'state': 'Karnataka', 'country': 'India'}, {'office_name': 'Agara B.O', 'pincode': 560034, 'taluk': 'Bangalore South', 'district': 'Bangalore', 'state': 'Karnataka', 'country': 'India'}]
  ```